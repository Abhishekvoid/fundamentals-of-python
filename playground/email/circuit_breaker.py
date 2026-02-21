import time
import redis

redis_client = redis.Redis(host="localhost", port=6249, decode_responses=True)

class CircuitBreaker:

    Failures_thershold = 5
    cooldown = 60

    def __init__(self, service: str):
        self.service = service
        self.key = f"cb:{service}"


    async def is_open(self) -> bool:

        data = redis_client.hgetall(self.key)

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
        if failures >= self.Failures_thershold:
            redis_client.hset(
                self.key,
                mapping={
                    "state": "open",
                    "failures": failures,
                    "opened_at": time.time(),
                }
            )
    
    def record_success(self):

        redis_client.delete(self.circuit_key(self.service))

sendgrind_circuit_breaker = CircuitBreaker("sendgrid")