from .tenacity import calling_postgres
from .circuit_breaker import postgres_circuit_breaker, CircuitBreaker
from .load_control import SystemOverLoad, PostgresSlotManager
import time
import logging

logger = logging.getLogger(__name__)
postgres_circuit_breaker = CircuitBreaker("service")


class PostgresUnavaible(Exception):
    pass


async def Postgres(query: str, *args):

    if postgres_circuit_breaker.is_open():
        logger.warning(f"postgres circuit is open")
        raise PostgresUnavaible(f"postgres, temporarily unavaiable")

    try:

        async with PostgresSlotManager.postgres_slot():
            response = await calling_postgres(query, *args)
            postgres_circuit_breaker.record_success()
            return response
    except SystemOverLoad:
        raise PostgresUnavaible(f"system underload, try again later")
    
    except Exception as e:

        postgres_circuit_breaker.record_failure()

        logger.exception(

            "Postgres call is failed",
            extra={

                "circuit_state":  postgres_circuit_breaker.state,
                "failures": postgres_circuit_breaker.failures,
            }

        )

        raise