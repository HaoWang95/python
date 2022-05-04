"""
__getattr__ is only invoked if the attribute wasn't found for the usual ways. It's good for a fallback
implementation.
__getattribute__ is invoked before looking at the actual attributes on the object, so it can be tricky to implement
correctly.
"""


class BasicRecord:
    def __init__(self):
        self.basic = 1

    def __getattr__(self, item):
        value = f'Key for {item}'
        setattr(self, item, value)
        return value


class ValidatingRecord:
    def __init__(self):
        self.exists = 1

    def __getattribute__(self, item):
        print(f'* ValidatingRecord __getattribute__({item!r}) is called')
        try:
            value = super().__getattribute__(item)
            print(f'Found {item!r}, returning {value!r}')
            return value
        except AttributeError:
            value = f'Value for {item}'
            print(f'* Setting {item!r} to {value!r}')
            setattr(self, item, value)
            return value


class Creature(type):
    def __new__(mcs, *args, **kwargs):
        print(f'* Running {mcs}.__new__ with {args} and {kwargs}')
        return type.__new__(mcs, args, kwargs)


if __name__ == '__main__':
    basic_record = BasicRecord()
    print(f'Init: {basic_record.__dict__}')
    print(f'getattr for score: {basic_record.score}')
    print(f'After get: {basic_record.__dict__}')

    validating_record = ValidatingRecord()
    print(f'Validating init: {validating_record.__dict__}')
    print(f'Get exists: {validating_record.exists}')
    print(f'Get score: {validating_record.score}')
    print(validating_record.__dict__)