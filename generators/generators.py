

# 1. What problem do generators solve ?

"""

    # memory + control over execution 
      - insted of creating everything at once, generators produce values one at a time, only when needed.

"""

# List (eager execution)
nums = [x for x in range(5)]  # this will create all the values immediately and store in memory
print(nums)                 


# Genetor (lazy executions)
nums = (x for x in range(5)) # nothing runs yet and values produced on demands 


# 2. What is yield ?

# yields turns a functions into genetator function
def count_up_to(n):
    yield 1
    yield 2
    yield 3

# yield pauses the function instead of finishing it


# Compare with return

"""
# Return
    - Ends the function
    - functions is done forever

# yield

    - pauses the function
    - remembers its state
    - resumes next time
 
"""

# 3. Generator in action

def numbers():
    yield (f"you called the 1st yeild...."),
    yield (f"you called the 2nd yeild..."),
    yield (f"you called the 3rd yeild..."),

gen = numbers()

print(next(gen))  # it will execute the 1st yield and then the function pause
print(next(gen))  # it will resume the pasue and execute 2nd yeild and again pause 
print(next(gen))  # it will resume from the 2nd yeild and execute 3rd yield


"""
 1. Function starts
 2. Runs until frist yeild
 3. pauses
 4. Resumes from where it stopped
"""


# 4. Generator with loops

for value in numbers():   # 
    print(value)
    
"""
Python automatically:
    - call next()
    - stops at stopIteration
"""


# 5. Generator with logic

def even_numbers(limit):
    for i in range(limit):
        if i%2 == 0:
            yield i


for n in even_numbers(10):
    print(n)


# Real world use case

# 1. large data processing

def read_logs():
    for line in open("big.log"):
        yield line

def get_users():
    for user in user_db:
        print(user)