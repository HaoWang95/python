from typing import List
from datetime import datetime


def sort_priority(values: List, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority2(values: List, group):
    found: bool = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group):
        self._group = group
        self.found = False

    def __call__(self, x):
        if x in self._group:
            self.found = True
            return 0, x
        return 1, x


def log(message: str, when=None):
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


if __name__ == '__main__':
    log("This is a testing message")
    log("This is a debug message")
