
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


# problem 2
"""
We have an AI endpoint that takes 5 seconds to generate a summary. We also need to fetch the user's profile from the DB (0.5s) and check their subscription status (0.5s). How do you optimize this endpoint?
"""



async def generated_summary():
    print("AI: starting summary generation...")
    await asyncio.sleep(5)
    print("AI: finished generating summary")
    return "summaryyyy..."


async def fetch_user():
    print("fetching user data...")
    await asyncio.sleep(0.5)
    print("finished fetching the user")
    return {"username": "Abhishek", "id": 1}


async def check_subscription():
    print("checking user subscription")
    await asyncio.sleep(0.5)
    print("user subscription is active")
    return True


async def main():


    start_time = time.time()


    results = await asyncio.gather(
        generated_summary(),
        fetch_user(),
        check_subscription(),
)


    summary, user, is_subscribe = results


    end_time = time.time()
    total_time = end_time - start_time 


    print(f"total time taken: {total_time:.2f} seconds")
    print(f"Result: User {user['username']} (Subscribed: {is_subscribe}) got summary.")


if __name__ == "__main__":
    asyncio.run(main())