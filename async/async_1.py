import asyncio

"""

async is a lib to write concurrent code using the async/wait syntax

this is the foundation of multiple python asynchronous frameworks that provide high-performance network and wev-servers, database connection libraries, distribuyed task, queues and etc

Asyncio provides a set of high-level APIs to:
    - run Python coroutines concurrently and have full control over their execution
    - perform network IO and IPC
    - control subprocess
    - distribute task via queues
    - synchronize concurrent code
also low-level APIs for libraries and frameworks:

    - creating and managing even loops, providing asynchronous APIs for networking, runing subprocess
    - implement efficient protocols using transports;
    - bridge callback-based libraries and code with async/await syntax.
"""

async def func():
    print("hello!")
    await asyncio.sleep(2) # this will pause the execution for 2 seconds without blocking
    print("how are you")

asyncio.run(func())

# async def: defines an asynchronous function.
# await: pauses execution until the awaited function completes.


# Running Multiple Tasks Simultaneously
# With the help of async, multiple tasks can run without waiting for one to finish before starting another.

import time

# 1. DEFINITION
async def say_hello(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)  # I/O simulation
    print(f"Done {name}")
    return f"Hi {name}!"

# 2. RUNNING
async def main():
    # Sequential
    await say_hello("Rahul")
    
    # Parallel (KEY!)
    tasks = [say_hello(f"User{i}") for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
"end"


# 3.

async def fetch_menu():
    print("fetching menu...")
    await asyncio.sleep(2)
    print("Menu recevied")
    return "menu data"

async def fetch_offers():
    print("fetching offers...")
    await asyncio.sleep(2)
    print("offers recevied")
    return "offer data"

async def main():

    start = time.time()

    menu = await fetch_menu()
    offers = await fetch_offers()

    print(f"done in {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


    