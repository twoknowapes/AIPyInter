# 装饰器的参数用法
class AAA:
    def bbb(self, ccc):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"Decorating parameter: {ccc}")
                print("Before functuion call")
                result = func(*args, **kwargs)
                print("After function call")
                return result
            return wrapper
        return decorator
    
# 示例化类
aaa = AAA()

# 使用装饰器
@aaa.bbb("example parameter")
def my_function():
    print("Inside my_function")

# 调用函数
my_function()