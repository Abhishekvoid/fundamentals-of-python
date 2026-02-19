import openai
from openai import AsyncOpenAI
from tenacity import (
    retry,
    wait_exponential_jitter,
    stop_after_attempt,
    retry_if_exception_type
)

ERRORS = (
    openai.RateLimitError,
    openai.APIConnectionError, 
    openai.InternalServerError,
)

@retry(
    retry=retry_if_exception_type(ERRORS),
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=2, max=10)
)
async def calling_LLM(text: str) -> dict:
    print(f"Sending request to OpenAI: {text[:50]}...")
    client = AsyncOpenAI()
    return await client.embeddings.create(
        input=text, 
        model="text-embedding-3-small"
    )
