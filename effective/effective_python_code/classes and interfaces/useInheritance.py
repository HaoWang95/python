class Base:
    """
    In Base class, to create an instance of Base class, we just provide a value, and the base class has an implemented
    behavior called show_value
    """

    def __init__(self, value):
        print("Base class is initialized")
        self.value = value

    def show_value(self):
        print(f"Base class: {self.value}")


class ValueBase:
    def __init__(self, value):
        print("ValueBase is initialized")
        self.value = value

    def minus_one(self):
        self.value -= 1
        print(f"ValueBase: the value is deducted by 1, {self.value}")


class BaseChild(Base, ValueBase):
    def __init__(self, value):
        Base.__init__(self, value)
        ValueBase.__init__(self, value)
        # super

    def add_one(self):
        self.value += 1


if __name__ == '__main__':
    base = Base(10)  # base class instance
    base_child = BaseChild(20)  # base child instance
    base.show_value()  # This makes sense, as Base class has a behavior called show value

    base_child.show_value()  # This also makes sense as Base Child will inherit everything from base

    # child class can add extra behavior that Base class does not have
    base_child.add_one()
    base_child.show_value()
    base_child.minus_one()
    base_child.show_value()
