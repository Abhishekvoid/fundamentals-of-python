import asyncio
import time
from collections import defaultdict, deque
from typing import Dict, Any, Optional, List
import uuid
import logging
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

logger = logging.getLogger(__name__)

class TrafficController:
    def __init__(self, max_concurrency: int = 20, rate_limit_rpm: int = 50):
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.user_requests: Dict[str, deque[float]] = defaultdict(deque)
        self.rate_limit_window = 60  # 1 minute
        self.rate_limit_rpm = rate_limit_rpm
        self.active_requests = 0
        self.circuit_open = False
        self.failure_count = 0
        self.last_failure = 0
        self.circuit_timeout = 30

    # 1. RATE LIMITING (Per user protection)
    def is_rate_limited(self, user_id: str) -> bool:
        """50 req/min per user - token bucket style"""
        now = time.time()
        window_start = now - self.rate_limit_window
        
        # Clean expired tokens
        while self.user_requests[user_id] and self.user_requests[user_id][0] < window_start:
            self.user_requests[user_id].popleft()
        
        if len(self.user_requests[user_id]) >= self.rate_limit_rpm:
            return True
            
        self.user_requests[user_id].append(now)
        return False

    # 2. CONCURRENCY LIMITING (Global resource protection)
    async def acquire_slot(self, request_id: str) -> bool:
        """Max 20 concurrent LLM calls"""
        if self.active_requests >= self.max_concurrency:
            return False
        async with self.semaphore:
            self.active_requests += 1
            return True

    async def release_slot(self):
        self.active_requests -= 1

    # 3. RETRY + BACKOFF (Transient failure handling)
    @retry(stop=stop_after_attempt(3), wait=wait_exponential_jitter(jitter=0.5))
    async def safe_call(self, func, *args, **kwargs):
        return await func(*args, **kwargs)

    # 4. CIRCUIT BREAKER (Persistent failure handling)
    async def circuit_breaker(self, func, *args, **kwargs):
        if self.circuit_open:
            if time.time() - self.last_failure > self.circuit_timeout:
                self.circuit_open = False
                self.failure_count = 0
            else:
                raise Exception("Circuit breaker OPEN")
        
        try:
            result = await func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure = time.time()
            if self.failure_count >= 5:
                self.circuit_open = True
            raise e

    # 5. GRACEFUL DEGRADATION (Fallback response)
    async def fallback_response(self, query: str) -> str:
        return f"Sorry, high traffic! Basic answer to '{query[:50]}...': Please try again in 30s."

    # 6. QUEUEING (Buffer burst traffic)
    def __init__(self):
        self.request_queue: deque = deque(maxlen=100)
        self.priority_queue: Dict[str, int] = {}

    async def enqueue(self, request_data: Dict) -> tuple[bool, str]:
        if len(self.request_queue) >= 100:
            return False, "Queue full"
        self.request_queue.append(request_data)
        return True, "Queued"

    # 7. PRIORITY ROUTING (Premium user protection)
    PRIORITY_MAP = {"premium": 3, "pro": 2, "free": 1}

    def get_priority(self, user_tier: str) -> int:
        return self.PRIORITY_MAP.get(user_tier, 1)

    async def process_request(self, user_id: str, query: str, user_tier: str = "free"):
        request_id = str(uuid.uuid4())
        
        # 1. Rate limiting
        if self.is_rate_limited(user_id):
            return {"error": "Rate limited", "retry_after": 60}
        
        # 2. Priority check
        priority = self.get_priority(user_tier)
        if priority < 2 and self.active_requests >= self.max_concurrency:
            queued, msg = await self.enqueue({"user_id": user_id, "query": query})
            if not queued:
                return {"error": "High traffic - queue full"}
            return {"queued": True, "position": len(self.request_queue)}
        
        # 3. Acquire concurrency slot
        if not await self.acquire_slot(request_id):
            return {"error": "Too many concurrent requests"}
        
        try:
            # 4. Circuit breaker protected call
            @self.circuit_breaker
            async def rag_call():
                
                await asyncio.sleep(2)  
                return f"RAG answer for: {query}"
            
            result = await self.safe_call(rag_call)
            return {"success": True, "data": result}
            
        except Exception as e:
            # 5. Graceful degradation
            fallback = await self.fallback_response(query)
            return {"degraded": True, "data": fallback}
        
        finally:
            await self.release_slot()

# USAGE EXAMPLE
async def demo():
    controller = TrafficController()
    
    async def simulate_users():
        tasks = []
        for i in range(100):  # 100 concurrent users
            user_id = f"user_{i}"
            tier = "premium" if i < 10 else "free"
            task = controller.process_request(user_id, f"query_{i}", tier)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(f"Results: {len([r for r in results if r.get('success')])} success")

if __name__ == "__main__":
    asyncio.run(demo())