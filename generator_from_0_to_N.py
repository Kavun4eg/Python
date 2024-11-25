def even_numbers_generator(N):
    for i in range(0, N + 1, 2):
        yield i

for number in even_numbers_generator(10):
    print(number)
