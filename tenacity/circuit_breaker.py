
"""

1. Problem:

    # situation

    - RAG app calls LLM API
    - the LLM is down
    - 100 user hit "Ask"
    - every Request:  # tenacity
        - wait
        - retries
        - timeout
    - worker get blocked, system slow down, Everting failling
    # THIS IS CALLED CASCADING FAILURE  

    Circuit breaker exists to answer ONE question:

        “If a dependency is sick, how do we stop hammering it?”


2. Real World Analogy
    circuit breaker at home:

        - Too much load → breaker trips
        - Electricity is CUT immediately
        - You don’t keep trying to power devices
        - After some time, you try again

    Software circuit breaker = same idea.

    

3. Circuit Breaker

    1. Closed(normal)
        - Every thing works
        - Request are allowed
        - failures are counted
    
    2. Open(fail fast)
        - too many failures
        - Requests are block immediately
        - No retries
        - No waiting
    
    3. Half-Open(test)

        - Cooldown time passed
        - Allow 1–2 test requests
        - If success → go back to CLOSED
        - If fail → go back to OPEN

        
4. Why Redis:

    # because
        - multiple workers
        - multiple process
        - possibly multiple machines
    
    # redis
        - shared memory
        - all workers see the same state
        - perfect for "global health flags"
        
"""

import time 
import redis


# connecting with redis
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


# values of threshold and cooldown
FAILURE_THRESHOLD = 5   # if serice fail 5 times mark as borken and stop calling it for 60 seconds
COOLDOWN_SECONDS = 60   


# redis key name
def circuit_key(service:str):
    return f"cb:{service}"

"""
example:

    circuit_key("llm") -> "cb:llm"
    cb:llm -> {state, failures, opened_at}
"""


def is_circuit_open(service:str) -> bool:
    # "hgetall" key_name is the name of the Redis key that holds the hash 
    data = redis_client.hgetall(circuit_key(service)) # Give me all stored info about this service’s circuit

    if not data:
        return False # If we’ve never seen failures → circuit is CLOSED
    

    # Has the circuit been marked OPEN?
    if data["state"] == "open":


        # Has enough time passed since we opened the circuit?
        openend_at = float(data["opened_at"])
        if time.time() - openend_at > COOLDOWN_SECONDS:

            # Allow ONE request to test if service recovered
            redis_client.hset(circuit_key(service), "state", "half-open")
            return False
        
        # Circuit is OPEN → block the call
        return True
    
    # Circuit is CLOSED → allow call
    return False


# Recording failures:

def record_failure(service: str):
    failures = redis_client.hincrby(key, "failures", 1)  # Increase failure count by 1

    if failures >= FAILURE_THRESHOLD:
        redis_client.hset(
            key,
            mapping={
                "state": "open",
                "opened_at": time.time()
            }
        )
        
def record_success(service: str):
    redis_client.delete(circuit_key(service))