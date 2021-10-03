from typing import List, Dict, Set
from collections import defaultdict

"""
It's uncommon to have a defined natural ordering using special methods for objects. 
"""


class Tool:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


def test_dict_order():
    nick_names: Dict[str, str] = {'cat': 'kitten', 'dog': 'puppy'}
    print(list(nick_names.keys()))
    print(list(nick_names.values()))
    print(list(nick_names.items()))


def kwargs_test(**kwargs):
    for index, (key, value) in enumerate(kwargs.items()):
        print(f'{index + 1}: {key}:{value}')


def test_default_dict() -> None:
    visits: Dict[str, Set[str]] = {
        'Japan': {'Tokyo'},
        'China': {'Shenzhen'},
    }  # Initialize a visits dictionary
    if (australia := visits.get('Germany')) is None:
        visits['Australia'] = australia = set()
    australia.add('Sydney')
    if (germany := visits.get('Germany')) is None:
        visits['Germany'] = germany = set()
    germany.add('Berlin')
    visits.setdefault('China', set()).add('Beijing')  # This is a more concise usage
    print(visits)


class Visits:
    def __init__(self):
        self.data: Dict[str, Set[str]] = {}

    def add(self, country, city):
        # the implementation of the Visits.add method still isn't ideal
        # It constructs a new set instance on every call, regardless of whether the given country was already
        # present in the data dictionary
        self.data.setdefault(country, set()).add(city)

    def __len__(self):
        return len(self.data)


class VisitsCountry:
    def __init__(self):
        self.data: Dict[str, Set[str]] = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    print(sorted([2, 1, 4, 6, 3], reverse=True))
    print([2, 1, 4, 6, 3].sort())
    tool_list: List[Tool] = [
        Tool('hammer', 4.5),
        Tool('chisel', 3.0),
        Tool('screwdriver', 1.0),
        Tool('handle', 1.0),
        Tool('drill', 4.5)
    ]
    print(f'Unsorted: {repr(tool_list)}')
    tool_list.sort(key=lambda tool: (tool.weight, tool.name))  # using the key to sort the tool_list
    print(f'Sorted: {tool_list}')
    test_dict_order()
    for item in tool_list:
        for k, v in item.__dict__.items():
            print(f'{k} = {v}')

    kwargs_test(kangaroo='joey', goose='gosling')
    test_default_dict()
