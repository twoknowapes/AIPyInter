def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y

print(add(3, 4))