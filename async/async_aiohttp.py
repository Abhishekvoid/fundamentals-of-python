
import aiohttp
import asyncio
import time  

async def fetch_swiggy_restauratns(session):

    print("fetching restaurants...")
    async with session.get('http://127.0.0.1:8000/api/registery/api/restaurants/') as resp:
        data =  await resp.json()
        return f"{len(data)} restaurants"
    
async def fetch_user_profile(session):

    print('fetching user profile')
    async with session.get('http://127.0.0.1:8000/api/registery/api/profile/') as resp:
        data = await resp.json()
        return f"User: {data['username']}"

async def fetch_gold_status(session):

    print('checking gold status...')
    async with session.get('http://127.0.0.1:8000/api/registery/api/gold-status/') as resp:
        data = await resp.json()
        return f"Gold Member: {data['is_gold']}"

async def main():
    
    start = time.time()

    async with aiohttp.ClientSession() as session:
        results =  await asyncio.gather(

            fetch_swiggy_restauratns(session),
            fetch_user_profile(session),
            fetch_gold_status(session)
        )

    print(f"total time: {time.time() - start:.2f}s")
    print("results", results)

asyncio.run(main())