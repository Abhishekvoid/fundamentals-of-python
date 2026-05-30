import asyncio

semaphore = asyncio.Semaphore(3)

async def generate_emebedding(doc_id: int) -> None:
    
    async with semaphore:
        
        print(f"processing document{doc_id}")
        await asyncio.sleep(2)
        print(f"finished document {doc_id}")
        
async def main() -> None:
    
    tasks = [
        
        generate_emebedding(i)
        for i in range(10)
    ]
    
    await asyncio.gather(*tasks)


asyncio.run(main())