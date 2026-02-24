
import asyncio
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

MAX_CONCURRENT = 3
MAX_QUEUE = 5
class OverLoadError(Exception):
    pass


class SimulationSlotManager:
    

    async def __init__(self):
        self._semaphore = asyncio.Semaphore(MAX_CONCURRENT)
        self._waiting = 0
        self._lock = asyncio.Lock

    @asynccontextmanager
    async def slot_manager(self):

        async with self._lock:
            if self._waiting >= MAX_QUEUE:
                raise OverLoadError ("system overloaded, try again later")
            self._waiting += 1

        try:

            async with self._semaphore:
                yield

        finally:

            async with self._lock:
                self._waiting -= 1


SimulationManager = SimulationSlotManager()


