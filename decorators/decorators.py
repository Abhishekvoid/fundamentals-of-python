
#  1. Decorator

"""
    A decorators is just a function that wraps another function
    to add behavior before or after it, without modifying the original.

    # Real-world relevance
        - Authetication( @login_required )
        - logging
        - timing functions
        - cachcing
        - permissions
        - Rate limiting
        - validation hooks
    
    if you want production backend code, decorators are non-optional.

"""


# 1. What a Decorator 
#    - A decorators is just a function that takes another function and returns a new functions

# 2. functions are object

def greet():
    print("hello")

x = greet
x()

"""
    functions can be:
        - passed
        - returned
        - stored
    decorators depend on this.
"""

# 3. A simple wrapper

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("after function")
    return wrapper

# use it manually

def say_hi():
    print("hii!")

say_hi = my_decorator(say_hi)
say_hi()

# output: 
#  Before function
#  hii!
#  after function

# now using @ syntax
# 4. same thing using '@'

def my_decorator(func):
    def wrapper():
        print("decorators... Summers !! 🍁🍁")
        func()
        print("decorators... winters !! ⛄❄️")
    return wrapper


@my_decorator # @my_decorator means: weather =  my_decorator(weather)
def weather():
    print("Mosoon !! ⛈️☂️")

weather()

# 3. Decorators with arugments
#    problem: functions takes arguments


@my_decorator
def add(a, b):
    return a + b

# solution: *args, **kwargs

def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# now works for ANY function



