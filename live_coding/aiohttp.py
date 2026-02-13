
import aiohttp
import asyncio
import time

async def chucking(session):

    print(f"start chucking...")
    async with session.get("hhtp/chunking.com") as resp:

        data = await resp.json()
        return f'chucked data {data}'

async def Vector(session):

    print(f"vectorizing the data...")
    async with session.get("qdrant.6333") as resp:

        vector_data = await resp.json()
        return f'qdrant vectoe {vector_data}'

async def Embedding(session):

    print(f"embedding the data...")
    async with session.get("goole.embedding_004.6333") as resp:

        embedded_data = await resp.json()
        return f'qdrant vectoe {embedded_data}'

async def Calling_LLM(session):
    print(f"calling llm...")
    async with session.get("API key") as resp:

        llm_model = await resp.json()
        return f'qdrant vectoe {llm_model}'
    
async def main():


    start_time = time.time()

    async with aiohttp.ClientSession as session:

        results = await asyncio.gather(

            chucking(session),
            Vector(session),
            Embedding(session),
            
            Calling_LLM(session),
            return_exceptions=True
        )

    print(f"Results: {results}")
    print(f"Total time: {time.time() - start_time:.2f}s")
            

asyncio.run(main())