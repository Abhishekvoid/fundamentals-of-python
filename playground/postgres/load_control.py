import asyncio
from contextlib import asynccontextmanager



Max_concurrent = 5
Max_queue = 25
class SystemOverLoad(Exception):
    pass


class PostgresSlotManager:

    def __init__(self):
        self._semaphore = asyncio.Semaphore(Max_concurrent)
        self._waiting = 0
        self._lock = asyncio.Lock


    @asynccontextmanager
    async def postgres_slot(self):

        async with self.lock:
            if self._waiting >= Max_queue:
                raise SystemOverLoad("system overload, try again later")
            self._waiting += 1


        try:
            async with self._semaphore:
                yield

        finally: 
            async with self._lock():

                self._waiting -= 1


PostgresManager = PostgresSlotManager()