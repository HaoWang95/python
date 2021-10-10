from typing import TypeVar

T = TypeVar('T')


class Visits(dict):
    def __init__(self):
        super().__init__()
        self._data = dict()

    def __missing__(self, key):
        raise KeyError

    def __setitem__(self, key, value) -> None:
        self._data[key] = value

    def __getitem__(self, item) -> T:
        return self._data[item]

    def __repr__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)


class Sorter:
    def __init__(self, group):
        self._group = group
        self.found = False

    def __call__(self, x):
        if x in self._group:
            self.found = True
            return 0, x
        return 1, x


if __name__ == '__main__':
    pass
