import asyncio
from contextlib import asynccontextmanager


Max_concurrent = 10
Max_queue = 25

class SystemOverLoad(Exception):
    pass

class SlotManager:

    def __int__(self):
        self._semaphore = Max_concurrent
        self._waiting = 0
        self._lock = asyncio.Lock


    @asynccontextmanager
    async def Email_slot(self):

        async with self._lock:
            if self._waiting > Max_queue:
                raise SystemOverLoad("sendgrind Unavaiable,  try again later")
            self._waiting += 1

        try:

            async with self._semaphore():
                yield
        
        finally:

            async with self._lock:
                self._waiting -= 1


sendgrind_slot_mananger = SlotManager()