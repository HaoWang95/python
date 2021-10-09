from typing import Dict

"""
Walrus operator is a new syntax introduced in Python3.8 so solve a long-standing problem with the language that can 
cause code duplication.
Walrus: := 
"""


def test_operator():
    # str: int
    fruits: Dict[str, int] = {
        'apple': 10,
        'banana': 5,
        'cherry': 20,
        'pineapple': 3,
        'watermelon': 2,
    }
    # what if we want to get an element from dictionary
    apple = fruits.get('apple')  # assignment
    peach = fruits.get('peach')  # assignment
    if apple:  # check condition if apple => if apple is True
        print(apple)  # action
    if peach:
        print(peach)

    # If we know the walrus operator, the code above can be simplified as:
    if cherry := fruits.get('cherry'):  # := assignment and check condition can all be applied in one if statement
        print(cherry)

    if banana := fruits.get('banana'):
        print(banana)

    if (pine := fruits.get('pineapple')) > 3:
        print(pine)

    # if we do not need to assign an variable, we can still use the if check directly
    if fruits.get('pineapple') > 3:
        pass


if __name__ == '__main__':
    test_operator()
