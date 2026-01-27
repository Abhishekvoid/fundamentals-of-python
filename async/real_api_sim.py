import aiohttp
import asyncio

async def groq_api(prompt):
    """Real Groq LLM call simulation"""
    async with aiohttp.ClientSession() as session:
        # Simulate 2sec LLM delay
        await asyncio.sleep(2)
        return f"AI: {prompt.upper()}"

async def parallel_llm(prompts):
    tasks = [groq_api(p) for p in prompts]
    return await asyncio.gather(*tasks)

# 10 LLM calls → 2sec (not 20sec!)
prompts = [f"AI tutor question {i}" for i in range(10)]
results = asyncio.run(parallel_llm(prompts))
