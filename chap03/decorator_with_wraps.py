# 使用 @wraps(func) 保持函数签名
def log_execution(func: Callable) -> Callable:
    """Decorator to log the execution of a function."""
    @wraps(func)