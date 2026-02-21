from .tenacity import sendgrid_request
from .circuit_breaker import sendgrind_circuit_breaker, CircuitBreaker
from .load_control import SystemOverLoad, sendgrind_slot_mananger

import logging
logger = logging.getLogger(__name__)
sendgrind_circuit_breaker = CircuitBreaker("sendgrid")

class SendgridUnavaiable(Exception):
    pass


async def send_email(paylaod: dict) -> dict:

    if sendgrind_circuit_breaker.is_open():
        logger.warning("spendgrid is aviable, Circuit is open ")
        raise SendgridUnavaiable("stripe temporarily avaiable")
    
    try:

        async with sendgrind_slot_mananger.Email_slot():
            response = await sendgrid_request(payload)
            sendgrind_circuit_breaker.record_sucess()
            return response
    except SystemOverLoad:
        raise SendgridUnavaiable("system under heavy load")

    except Exception as e:

        sendgrind_circuit_breaker.record_failure()

        logger.exception("SendGrid call failed", extra={"error": str(e)})  
        raise

        