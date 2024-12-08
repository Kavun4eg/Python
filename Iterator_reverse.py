class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

lst = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(lst)
for item in reverse_iter:
    print(item)
