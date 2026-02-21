import time
import redis


redis_client = redis.Redis(host="localhost", port=6379 , decode_responses=True)

class CircuitBreaker:

    FAILURE_THRESHOLD  = 5
    cooldown = 60

    def __init__(self, service:str):
        self.service = service
        self.key = f"cb:{service}"

    def is_open(self) -> bool:

        data = redis_client.hgetall(self.circuit_key(self.key))

        if not data:
            return False
        
        if data.get("state") == "open":
            opened_at = float(data.get("opened_at"))
            if time.time() - opened_at > self.cooldown:
                redis_client.hset(self.key, "state", "half-open")
                return False
            return True
        return False
    
    def record_failure(self):

        failures = redis_client.hincrby(self.key, "failures", 1)
        if failures > self.FAILURE_THRESHOLD:
            redis_client.hset(
                self.key,
                mapping={
                    "state": "open",
                    "failures": failures,
                    "opened_at": time.time(),  

                }
            )
    def record_sucess(self):

        redis_client.delete(self.circuit_key(self.service))
    
postgres_circuit_breaker = CircuitBreaker("postgres")