def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_args_and_result
def add(a, b):
    return a + b

add(3, 5)
