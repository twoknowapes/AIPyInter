from functools import wraps
import time


def log_time(func):
    """Decorator that logs the execution time of the decorated function.

    Args:
        func: The function to be decorated.

    Returns:
        wrapper: The wrapped function that logs execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Executing {func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper


def log_args(func):
    """Decorator that logs the arguments passed to the decorated function.

    Args:
        func: The function to be decorated.

    Returns:
        wrapper: The wrapped function that logs arguments.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"Executing {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_time
@log_args
def calculate_sum(a, b, multiplier=1):
    """Calculate the sum of two numbers and multiply by a coefficient.

    Args:
        a: First number to add
        b: Second number to add
        multiplier: Coefficient to multiply the sum by (default: 1)

    Returns:
        The result of (a + b) * multiplier
    """
    time.sleep(0.1)
    return (a + b) * multiplier


calculate_sum(1, 2, multiplier=2)
