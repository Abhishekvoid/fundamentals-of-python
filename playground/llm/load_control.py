import asyncio
from contextlib import asynccontextmanager

MAX_CONCURRENT = 20
MAX_QUEUE = 100

class SystemOverLoad(Exception):
    pass

class LLMSlotManager:
    def __init__(self):
    
        self._semaphore = asyncio.Semaphore(MAX_CONCURRENT)
        self._waiting = 0
        self._lock = asyncio.Lock()

    @asynccontextmanager
    async def llm_slot(self):

        global _waiting

        async with self._lock:
            if _waiting >= MAX_QUEUE:
                raise SystemOverLoad("system is overloaded, try again")
            _waiting += 1

        try:

            async with self._semaphore:
                yield
        finally:
            async with self._lock:
                _waiting -= 1

slot_manager = LLMSlotManager()