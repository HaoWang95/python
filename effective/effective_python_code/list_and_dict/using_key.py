"""
The list built-in type has a sort method for ordering the items.
By default, sort will order a list's content by the ascending order of the items.
Lambda:
Actually, Lambda is one way to use Anonymous function, the syntax of Python Lambda is:
    lambda Python_Arguments: expression
    x = lambda a: a+10 # After defining this line, x is a anonymous function
    print(x(5)) => 5+10
"""


def use_sort():
    numbers: list[int] = [93, 100, 50, 60, 56, 34, 45, 67, 21]
    numbers.sort()
    print(numbers)
    float_numbers: list[float] = [12.27, 2.0, 10.23, 3.14, 2.13]
    float_numbers.sort()
    print(float_numbers)
    number_list: list = [66.66, 55.55, 99.99, 88.88, 20, 50, 100, 10, 45]
    number_list.sort()
    print(number_list)


def use_lambda():
    add_lambda = lambda x, y: x + y
    print(add_lambda(5, 10))


class WorkingTool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool(name: {self.name}, weight {self.weight})'


# A more advanced example compared with WorkingTool
class Car:
    def __init__(self, name=None, speed=None, price=None, owner=None):
        self.name = name  # public
        self.speed = speed  # public
        self.price = price  # public
        self.__owner = owner  # private

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def __repr__(self):
        return f'Car(name={self.name}, speed={self.speed}, price={self.price}, owner={self.__owner})'


def use_workingtool() -> None:
    my_tool_box: list[WorkingTool] = [
        WorkingTool('Screwdriver', 0.2),
        WorkingTool('Hammer', 4.0),
        WorkingTool('Wrench', 1.5),
        WorkingTool('Ladder', 4.5)
    ]
    # Now consider how we can sort my_tool_box
    # Lambda: anonymous function, think it like a function call, but the function has no name
    # Anonymous function, callback function (JavaScript)
    print(f'Unsorted tool box: {my_tool_box}')
    my_tool_box.sort(key=lambda variable: variable.weight)
    print(f'Sorted tool box: {my_tool_box}')


def use_cars():
    owner_str: str = 'Albert'
    albert_garage: list[Car] = [
        Car(name='BMW', speed=180, price=150000, owner=owner_str),
        Car(name='Fiat', speed=210, price=170000, owner=owner_str),
        Car(name='Mustang', speed=190, price=155000, owner=owner_str)
    ]
    # Consider, how to solve your garage by car's speed
    albert_garage.sort(key=lambda car_variable: car_variable.speed, reverse=True)
    print(f'Sort garage by speed: {albert_garage}')
    # Consider, how to sort your garage by car's speed, but from low to high
    albert_garage.sort(key=lambda car: car.speed, reverse=False)
    print(f'Sort garage by speed: {albert_garage}')
    # Consider, how to sort your garage by car's price, following the default order
    albert_garage.sort(key=lambda car: car.price)
    print(f'Sort garage by price: {albert_garage}')
    # Consider, how to sort your garage by car's price, but start from high to low
    albert_garage.sort(key=lambda x: x.price, reverse=True)
    print(f'Sort garage by price(from high to low): {albert_garage}')
    # Sort your garage by the length of car's name
    albert_garage.sort(key=lambda car: len(car.name), reverse=True)
    print(f'Sort garage by name length: {albert_garage}')


if __name__ == '__main__':
    use_sort()
    use_workingtool()
    use_lambda()
    use_cars()
