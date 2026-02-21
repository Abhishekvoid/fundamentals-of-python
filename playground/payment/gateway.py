
from .tenacity import calling_stripe
from .circuit_breaker import payment_circuit_breaker, CircuitBreaker
from .load_control import SystemOverLoad, slot_mananger
import time
import logging

logger = logging.getLogger(__name__)
payment_circuit_breaker = CircuitBreaker("payment")

class PaymentUnavaible(Exception):
    pass

async def payment(method:str, endpoint:str, **kwargs):


    if payment_circuit_breaker.is_open:

        logger.warning("Stripe not aviable, Circuit is open")
        raise PaymentUnavaible("stripe temporarily avaiable")
    

    try:

        async with slot_mananger.payment_slot():
            response = await calling_stripe(method, endpoint)
            payment_circuit_breaker.record_sucess()
            return response
    except SystemOverLoad:
        raise PaymentUnavaible("system under heavy load")
             

    except Exception as e:

        payment_circuit_breaker.record_failure()


        logger.exception(
            "stripe call is failed",
            extra = {
                "circuit_state":  payment_circuit_breaker.state,
                "failures": payment_circuit_breaker.failures,
            }
        )

        raise

    