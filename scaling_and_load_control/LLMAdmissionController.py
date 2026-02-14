import asyncio
from contextlib import asynccontextmanager

MAX_CONCURRENT = 20
MAX_QUEUE = 100

_semaphore = asyncio.Semaphore(MAX_CONCURRENT)
_waiting = 0
_lock = asyncio.Lock()

class SystemOverloaded(Exception):
    pass


@asynccontextmanager
async def llm_slot():
    global _waiting

    async with _lock:
        if _waiting >= MAX_QUEUE:    # if queue is too big -> reject
            raise SystemOverloaded("System overloaded. try again later")
        _waiting += 1

    try:

        async with _semaphore:   # wait for semaphore slot
            yield
    finally:
        async with _lock:
            _waiting -= 1


"""
    1. If queue is too large → reject immediately.
    2. Otherwise → wait for semaphore slot.
    3. Once finished → decrement waiting count.

    prevent:

        infinte queue
        memory explosion
        llm overload
"""