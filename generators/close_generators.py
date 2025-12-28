
def drinks():
    yield f"-------- Drinks ---------"
    yield "hot-chocolate"
    yield "expersso"

def sandwich():
    yield f"-------- Sandwich ---------"
    yield "croissant sandwich"
    yield "flat-bread sandwich"

def full_menu():
    yield from drinks()
    yield from sandwich()

for items in full_menu():
    print(items)


def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, No more chaii")

        """
            so the generator:
                - catches generatorExit
                - Execute the print
                - Terminate clearly
            
            # output
            - stall closed, no more chaii
        """


# 1. what does .close() do?
    # .close() raises a GeneratorExit exception inside generator

# This is how python tells the generator:
    # stop immediately. clean up if needed


"""
    when you call stall.close python raise GeneratorExit internally, That exception is thrown at the point where the generator is paused (at yield).
"""


stall = chai_stall()

print(next(stall))  # start generator
stall.close()       # close it


# 7. Mental model
"""
    next() -> "Do next task"
    yield  -> "pause here"
    close() -> "Stop working, clean up"
    stopIteration -> "Work finsihed"
"""

# 8. Real-World analogy
"""
    next(stall) -> customer arrives
    yield -> waiting a counter
    close() -> shop closing time
    GeneratorExit -> shutter down
"""