def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

divide(5, 0)  # Викличе виняток
