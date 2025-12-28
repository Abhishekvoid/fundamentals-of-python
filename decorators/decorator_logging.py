from functools import wraps


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling... {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished... {func.__name__}")
        return result
    return wrapper

@logger
def movement_func(location, longitute, latitude  ):
    print(f"robot located at: {location}"
          f"(long = {longitute}, lat = {latitude})"
          )
    long_lat = longitute + latitude
    print(long_lat)

movement_func("warehouse", longitute=72.872287, latitude=12.9273)