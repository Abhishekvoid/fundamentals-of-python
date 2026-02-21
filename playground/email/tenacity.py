
import httpx
import os
from sendgrid import SendGridAPIClient
from tenacity import (

    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type
)
from python_http_client.exceptions import TooManyRequestsError, InternalServerError


SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

ERRORS =(

    TooManyRequestsError,
    InternalServerError,
    httpx.TimeoutException,
    httpx.ConnectError,
)


@retry(
    retry=retry_if_exception_type(ERRORS),
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=2, max=30)  
)
async def sendgrid_request(payload: dict) -> dict:
    headers = {

        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content_Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=20.0) as client:

        resp = await client.post(

            "https://api.sendgrid.com/v3/mail/send",
            json=payload,
            headers=headers
        )
        resp.raise_for_status()
        return resp.json()
    