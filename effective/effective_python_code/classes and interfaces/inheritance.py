import math


# base class
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'MyNumber value -> {self.value}'

    def multiply_two(self):
        self.value *= 2

    def show(self):
        print(f'I guess this will be inherited, current instance value -> {self.value}')

    @classmethod
    def from_value(cls, value):
        return cls(value)


# child class
class MyValue(MyNumber):
    def __init__(self, value):
        MyNumber.__init__(self, value)

    def my_value_behavior(self):
        print(f'{self.value}, this is a customized behavior in my value child class only')


class Student:
    def __init__(self, name, address, email, id):
        self.__name = name  # private
        self.__address = address
        self.__email = email
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __repr__(self):
        return f'Student {self.__id}: {self.__name} - {self.__email}'


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def area(self):
        # we define a property called area, which returns the length*width
        return self.__length * self.__width

    @property
    def perimeter(self):
        return self.__length * 2 + self.__width * 2


class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError('Radius must be larger than 0')
        else:
            self.__radius = new_radius

    # circumference -> 2 * math.pi * radius
    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

    # area -> math.pi * radius * radius
    @property
    def area(self):
        return math.pi * self.__radius * self.__radius


if __name__ == '__main__':
    five = MyValue(5)  # instance of MyValue
    ten = MyValue(10)  # instance of MyValue
    print(f'Value of five is -> {five}')
    print(f'Value of ten is -> {ten}')
    eight = MyValue.from_value(8)
    print(eight)
    ten.show()

    albert = Student('Albert', 'Melbourne', 'albertding@school.com', 1)
    print(albert.name)
    albert.name = "ALBERT"
    print(albert.name)

    albert_rectangle = Rectangle(5, 5)
    print(albert_rectangle.area)
    print(math.pi)
    test_circle = Circle()
    print(f'test_cricle -> circumference: {round(test_circle.circumference, 3)}, area: {round(test_circle.area, 3)}')
    test_circle.radius = 4
    print(f'test_circle, new radius -> circumference: {test_circle.circumference}, area: {test_circle.area}')
    # f-string to display 2-digits float
    print(f'circle: radius: {test_circle.radius:.2f}, circumference: {test_circle.circumference:.3f}, \n'
          f'area: {test_circle.area:.3f}')

    test_circle.radius = -5
    print(f'test_circle -> {test_circle.radius: .2f}')
