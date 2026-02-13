"""
1. The Core Problem: "The Network is a Lie"
Junior engineers assume the network is reliable.
Senior engineers assume the network will fail.

# Scenario: You send a request. You don't get a response.

    Junior Dev Logic: "The server must be down. I'll throw an error."

    Senior Dev Logic: "Maybe the packet got lost? Maybe the server is blinking? Maybe the drone went behind a building?"

# We classify errors into two types:

    Permanent Failures (4xx):

        Example: "Wrong Password", "Bad Request", "404 Not Found".
        Strategy: Fail Fast. Do not retry. It won't magically work the second time.

    Transient Failures (5xx or Network Error):

        Example: "503 Service Unavailable", "Connection Timeout", "Socket Closed".
        Strategy: Retry. It might work in 2 seconds.

2. The Solution: Exponential Backoff & Jitter
If your API fails, and you retry immediately, you might make things worse.

The "Thundering Herd" Problem (Food Delivery Example):
Imagine it's New Year's Eve. Swiggy's payment server is struggling because 10,000 people are ordering Biryani at 8:00 PM.

    - Bad Approach (Immediate Retry): The server drops a connection. Your app immediately retries.  The server is already overloaded. Now you just hit it again. 10,000 users retry at once. The server crashes completely.

    - Good Approach (Exponential Backoff):

        Attempt 1 fails.
        Wait 2 seconds. Retry.
        Fail. Wait 4 seconds. Retry.
        Fail. Wait 8 seconds. Retry.
        Result: You give the server "breathing room" to recover.

Jitter (The Secret Sauce):
If everyone waits exactly 2 seconds, they all hit the server again at exactly 8:00:02 PM.
Solution: Add Randomness (Jitter).

    User A waits 2.1s
    User B waits 1.9s
    Result: The traffic is smoothed out.
"""


import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type
)

# Define which errors are "Transient" (Retry-able)

TRANSIENT_ERRORS = (

    openai.APITimeoutError,
    openai.InternalServerError,
    openai.RateLimitError
)

class AIclient:

    @retry (

        # 1. Stop after 3 failed attempts (Don't retry forever)
        stop=stop_after_attempt(3),

        # 2. Wait 2s, then 4s, then 8s... up to max 10s.
        #    Add jitter (randomness) automatically
        wait=wait_exponential_jitter(initial=2, max=10),

        # 3. ONLY retry on specific transient errors
        retry=retry_if_exception_type(TRANSIENT_ERRORS),
    )
    def generate_embedding(self, text:str):

        print(f'sending resquest to openAI')

        return openai.embeddings.create(input=text, model="text-embedding-3-small")
    
client = AIclient()
try:
    embedding = client.generate_embedding("hello_reelo")
except Exception as e:

    print(f"failed after retires: {e}")



"""
Idempotency: The "Robotics/Payments" Safety Net
This is critical for FlytBase (Robotics) and Payments.

Scenario (Robotics):

    - Operator sends command: Drone.move_forward(10_meters).
    - Drone receives it, starts moving.
    - Drone sends "ACK" (Acknowledgement) back, but the network drops.
    - Operator thinks command failed. Operator sends Drone.move_forward(10_meters) AGAIN.
    - Result: Drone moves 20 meters. CRASH. 💥

The Solution: Idempotency Keys
Every command gets a Unique ID (UUID). The receiver checks: "Have I seen this ID before?"

    - Request 1 (ID: abc-123): move_forward. Drone: "Executing."

    - Request 2 (ID: abc-123): move_forward. Drone: "Wait, I already have ID abc-123 in my 'Processed' list. I will ignore this command and just send back 'Success'."
"""

processed_command = set()

def handle_drone_command(command_id, action):

    if command_id in processed_command:
        print('duplicate command{command_id} detected. ignoring')
        return "Alredy done"
    
    # actual action logic
    execute_hardware_action(action)

    # marking as done 
    processed_command.add(command_id)
    return "sucess"
