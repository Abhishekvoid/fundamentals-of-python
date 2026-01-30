
import aiohttp
import asyncio
import time  

async def fetch_swiggy_restauratns(session):

    print("fetching restaurants...")
    async with session.get('https://api.spoonacular.com/recipes?apiKey=YOUR_KEY') as resp:
        data =  await resp.json()
        return f"{len(data['results'])} restaurants"
    
async def fetch_user_profile(session):

    print('fetching user profile')
    async with session.get('https://jsonplaceholder.typicode.com/users/1') as resp:
        user = await resp.json()
        return user['name']

async def fetch_gold_status(session):

    print('checking gold status...')
    async with session.get('https://httpbin.org/delay/3') as resp:
        return 'gold active'

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