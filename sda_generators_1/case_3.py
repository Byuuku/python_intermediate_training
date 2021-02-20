def iterator_ex_3(n):
    import sys
    iterator = SumIterator(n)
    print(f"Size of list in bytes: {sys.getsizeof(iterator)}")
    result = sum(iterator)
    print(f"Size of one number in bytes: {sys.getsizeof(result)}")
    print(result)


class SumIterator:
    def __init__(self, n):
        self.amount = n
        self.values_created = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.values_created >= self.amount - 1:
            raise StopIteration
        self.values_created += 1
        return self.values_created
