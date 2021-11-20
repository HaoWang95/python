"""
A generator iterates over a sequence(iterable), and for each time, it gives out a value.
Generators are produced by functions that uses a yield expressions. When called, a generator function does not actually
run but instead immediately returns an iterator. With each call to the next build-in function, the iterator advances the
generator to its next yield expression.
"""
from random import randint


def random_generator():
    for _ in range(100):
        yield randint(1, 1000)


if __name__ == '__main__':
    it = random_generator()
    for i in range(10):
        print(next(it))