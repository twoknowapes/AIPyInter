from functools import wraps
import time


class CallLimitExceededError(Exception):
    pass


def call_limit(max_calls: int):
    if max_calls <= 0:
        raise ValueError("max_calls must be a positive integer")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.call_count = getattr(wrapper, "call_count", 0) + 1
            if wrapper.call_count >= max_calls:
                raise CallLimitExceededError(
                    f"Function {func.__name__} has been called {max_calls} times.")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
            

@call_limit(3)
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

calculate_sum(1, 2, multiplier=1)
calculate_sum(1, 2, multiplier=2)
calculate_sum(1, 2, multiplier=3)
calculate_sum(1, 2, multiplier=4)

