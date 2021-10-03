from typing import List, Dict

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
    nick_names: Dict[str:str] = {'cat': 'kitten', 'dog': 'puppy'}
    print(list(nick_names.keys()))
    print(list(nick_names.values()))
    print(list(nick_names.items()))


def kwargs_test(**kwargs):
    for index, (key, value) in enumerate(kwargs.items()):
        print(f'{index+1}: {key}:{value}')


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
