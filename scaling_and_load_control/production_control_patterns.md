

# Traffic Control Patterns

    1. Rate limiting (per user protection)
    2. concurrency limiting (global reaource protection)
    3. retry and backoff(transient failure handling)
    4. circuit breaker(persistent failure handling)
    5. graceful Degradation(fallback response)
    6. Queueing (buffer burst taffic)
    7. priority routing (perminum user protection)

# 1. If you set:

    Rate limit = 50 req/min per user
    Concurrency limit = 20 LLM calls

And suddenly 100 users hit at once.

    What happens?

        -> step 1: rate limiting  layer
        
        Each user send 1 request and limit is of 50 req/min means, Each user is under limit, so rate limiter allow them all.

        -> step 2: Concurrency layer

        Now 100 request try LLM call, but limit is 20 request.
            -> what will happen ?

                first 20 request allow, remaning 80 will wait, they do not fail, they wait in queue or blocked until slot is free.

                When one of the 20 finishes:
                → Slot frees.
                → Next waiting request proceeds.

                This is backpressure

                - system stay stable, latency increased

        What happen:

            1. increament in response time

                -> the first 20 uers get response in 1.5s, 2s (normal latency)

                next 80, wait in queue, each llm call takes 2s, batch size is 20

                batch 1 -> 2s
                batch 2 -> 4s
                ...  
                ... 
                   ...
                   ...
                batch 5 -> 10s 

                the last user wait for 10s

            Now you see the issue?

            Concurrency control protects system stability.
            But it increases tail latency (p95, p99).

            This is why AI infra teams obsess over:

            p95 latency
            tail behavior
            queue depth

            2. User Experience

            UX impact:

                Spinner shows longer
                Feels slow
                Some users may refresh (worse!)
                Some may abandon
            Now here’s the real production insight:
            You must surface state to the user.