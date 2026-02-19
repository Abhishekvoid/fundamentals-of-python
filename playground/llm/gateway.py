from .circuit_breaker import CircuitBreaker
from .tenacity import calling_LLM
from .load_control import SystemOverLoad, slot_manager
from openai import AsyncOpenAI
from contextlib import asynccontextmanager

import logging

logger = logging.getLogger(__name__)
circuit_breaker = CircuitBreaker("service")


class LLMunavailable(Exception):
    pass

async def ask_llm(text: str):

    if not circuit_breaker.Is_open:

        logger.warning("Circuit OPEN - blocking request")
        raise LLMunavailable("LLM temporarily unavailable")
    
    
    try: 
        
        async with slot_manager.llm_slot():
            response = await calling_LLM(text)  
            circuit_breaker.record_success()
            return response
    except SystemOverLoad:
        raise LLMunavailable("system under heavy load")
    
    except Exception as e:

        circuit_breaker.record_failure()

        logger.exception(
            "LLM call is failed",
            extra = {
                "circuit_state":  circuit_breaker.state,
                "failures": circuit_breaker.failures,
            }
        )

        raise