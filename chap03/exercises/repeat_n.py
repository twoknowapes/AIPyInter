from functools import wraps
import time


def repeat_n(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                print(f"Result of iteration: {result}")
            return result
        return wrapper
    return decorator


@repeat_n(3)
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
