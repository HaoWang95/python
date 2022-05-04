class Base:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(f'show value -> {self.value}')

    def __repr__(self):
        return f"Base with {self.value}"


class BaseChild(Base):
    def __init__(self):
        Base.__init__(self, 5)


if __name__ == '__main__':
    child = BaseChild()
    print(child)
    child.show_value()
