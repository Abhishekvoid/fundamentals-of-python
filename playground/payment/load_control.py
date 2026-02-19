import asyncio
import time
from contextlib import asynccontextmanager


Max_concurrent = 10
Max_queue = 25

class SystemOverLoad(Exception):
    pass

class PaymentSlotManager:

    def __init__(self):
        self._semaphore = asyncio.Semaphore(Max_concurrent)
        self._waiting = 0
        self._lock  = asyncio.Lock()


    @asynccontextmanager
    async def payment_slot(self):

        

        async with self._lock:

            if self._waiting >= Max_queue:
                raise SystemOverLoad("system is overloaded try again")
            self._waiting += 1

        try:

            async with self._semaphore:
                yield

        finally:

            async with self._lock:
                self._waiting -= 1

