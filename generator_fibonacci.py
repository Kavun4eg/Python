def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

for number in fibonacci_generator(10):
    print(number)
