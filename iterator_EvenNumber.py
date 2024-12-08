class EvenNumberIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.N:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

for number in EvenNumberIterator(10):
    print(number)
