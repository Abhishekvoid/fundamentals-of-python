
# problem 1
"""
Scenario: When you open Swiggy, it loads:

    1. Restaurant List (DB Query)
    2.Your Past Orders (DB Query)
    3. "Gold" Membership Status (External API)

If Swiggy did this one by one (Sync), the app would take 6 seconds to load. You would close it.
Instead, they fire all requests at once.

The Magic Function: asyncio.gather()
"""

import asyncio
import time

async def fetch_data(source, delay):
    print(f"starting to fetch from{source}...")
    await asyncio.sleep(delay)
    print(f"finished fetching from {source}")
    return f"data from {source}"

async def main():
    start = time.time()

    # Concurrent
    # asyncio.gather schedules all of them on the event loop immediately

    results = await asyncio.gather(

        fetch_data("reasturants (DB)", 2),
        fetch_data("User profile (DB)", 1),
        fetch_data("Gold status (API)", 3)
    )

    print(f"APP loaded total time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


