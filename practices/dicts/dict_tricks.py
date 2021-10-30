from typing import TypeVar
from collections.abc import MutableMapping

T = TypeVar('T')


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        if self.data[key]:
            del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for k in keys:
            yield k

    def __len__(self):
        return len(self.data)


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


class DictHandleMissing(dict):
    def __missing__(self, key):
        self[key] = ''
        print(f'No {key} is found')
        return self[key]


class Sorter:
    def __init__(self, group):
        self._group = group
        self.found = False

    def __call__(self, x):
        if x in self._group:
            self.found = True
            return 0, x
        return 1, x


class Creature:
    def __init__(self):
        print('A creature is created')

    def behave(self):
        print('behave')


class Plant(Creature):
    def __init__(self):
        super().__init__()


class Animal(Creature):
    def __init__(self):
        super().__init__()

    def behave(self):
        print('Animal')


if __name__ == '__main__':
    my_dict = DictHandleMissing()
    print(my_dict['test'])
    animal = Animal()
    animal.behave()
