

import time
from .tenacity_1 import AIclient

class SimpleCircuitBreaker:

    def __init__(self, failure_threshold=3, cooldown=30):

        self.failure_thershold = failure_threshold
        self.cooldown = cooldown
        self.failures = 0
        self.state = "closed"
        self.opened_at =    None

    def is_open(self):

        if self.state == "open":

            if time.time() - self.opened_at > self.cooldown:
                self.state = "half-open"
                return False
            return True
        return False
    
    def record_failure(self):

        self.failures += 1
        if self.failures > self.failure_thershold:
            self.state = "open"
            self.opened_at = time.time()

    def record_sucess(self):

        self.state = "closed"
        self.failures = 0
        self.opened_at = None



# using this in RAG 

cb = SimpleCircuitBreaker()

async def call_llm_with_cb(prompt):

    if cb.is_open():

        return "AI services temporarily unaviable, please try again later"
    
    try:

        result = await AIclient(prompt)   # calling tenacity 
        cb.record_sucess()
        return result
    except Exception:
        cb.record_failure()
        raise


# 3. Graceful degradation
# Circuit breaker alone is not enough
# You must decide what the user sees


async def get_answer(query):

    try:
        return await call_llm_with_cb(query)
    except Exception:
        cached = get_cached_answer(query)
        if cached:
            return cached
        return "Ai is temporarily unavilable, please try again later"
    
"""
Now your system:

    - Protects itself
    - Protects dependencies
    - Protects user experience
"""