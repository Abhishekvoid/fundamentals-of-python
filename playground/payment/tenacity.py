

import httpx
from tenacity import (

    retry,
    wait_exponential_jitter,
    retry_if_exception_type,
    stop_after_attempt,
)

from stripe import RateLimitError, APIConnectionError

errors = (
    RateLimitError, 
    APIConnectionError,
    httpx.TimeoutException,
    httpx.ConnectError,
)

@retry(


    retry= retry_if_exception_type(errors),

    wait = wait_exponential_jitter(initail=1, max = 10),

    stop = stop_after_attempt(5),
)
async def calling_stripe(method:str, endpoint:str, **kwargs) -> dict :

    async with httpx.AsyncClient(timeout=15) as client:

        resp  = await client.post(

            f"https://api.stripe.com/v1/{endpoint}",
            headers=headers, 
            data=kwargs,
        )
        resp.raise_for_status()
        return resp.json()