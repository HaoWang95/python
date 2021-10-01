from typing import List


class Tool:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


if __name__ == '__main__':
    print(sorted([2, 1, 4, 6, 3], reverse=True))
    print([2, 1, 4, 6, 3].sort())
    tool_list: List[Tool] = [Tool('hammer', 4.5), Tool('sissor', 3.0)]
    print(tool_list)
