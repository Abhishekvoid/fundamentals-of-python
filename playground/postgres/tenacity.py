import os
import httpx
import asyncpg 
from tenacity import (

    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type,
)

POSTGRES_DSN = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/reelo")

POSTGRES_ERRORS = (

    asyncpg.PostgresConnectionError,
    asyncpg.CannotConnectNowError,
    asyncpg.TooManyConnectionsError,
    asyncpg.InterfaceError,
)


@retry(

    retry=retry_if_exception_type(POSTGRES_ERRORS),
    wait=wait_exponential_jitter(initial=2, max=10),
    stop=stop_after_attempt(5),

)
async def calling_postgres(query: str, *args) -> list:

    connection = await asyncpg.connect(POSTGRES_DSN)
    try:
        result =  await connection.fetch(query, *args)
        return result
    
    finally:
        await connection.close()