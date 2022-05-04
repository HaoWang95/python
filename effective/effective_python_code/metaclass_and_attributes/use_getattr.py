from random import randint

"""
What is __getattr__
"""


class BasicRecord:
    def __init__(self):
        self.exists = 1  # note that now self.exists is just a simple public attribute

    # What if we want to get a new attribute dynamically
    # If an attribute is not in the object, we can assign it with a value in __getattr__
    def __getattr__(self, item):
        value = randint(0, 100)
        # what the BasicRecord object is going to do when we are trying to find an item dynamically
        print(f"* Called __getattr__({item})")
        # setattr(self, item, value)  # what if we want to customize our own setattr
        self.__setattr__(item, value)
        return value

    # we can define our customized logic for setattr()
    def __setattr__(self, key, value):
        print(f'* Called __setattr__({key}, {value})')
        if value < 60:
            print('You failed and the score will be recorded!!!!')
        super().__setattr__(key, value)


# Now we take a check to see how to use __getattribute__
class ValidateRecord:
    def __init__(self):
        self.exists = 'record!'

    # as long as __getattribute__ is implemented, any fetching to public attributes will lead to __getattribute__
    # Everytime a public attribute is accessed on an object(including missing ones), __getattribute__ will be called
    def __getattribute__(self, item):
        """
        If we implement this method directly, it is very likely that a RecursionError is returned.
        The right solution to implement this method is to use super().__getattribute__ method to fetch values from
        the instance attribute dictionary
        :param item: the attribute name to be accessed
        :return: item value
        """
        print(f'Called __getattribute__({item})')
        try:
            # when the item exists
            attribute = super(ValidateRecord, self).__getattribute__(item)
            print(f'* Found {item} with value {attribute}')
            return attribute
        except AttributeError as e:
            # when the item does not exist
            print(f'{item} is not in the object dictionary')
            return e


if __name__ == '__main__':
    basic_record = BasicRecord()
    print(f'Init BasicRecord: {basic_record.__dict__}')
    print(f'Fetch exists: {basic_record.exists}')
    print(f'Fetch score: {basic_record.score}')
    print(f'After fetch score: {basic_record.__dict__}')
    print(f'Fetch score again: {basic_record.score}')

    validating_record = ValidateRecord()
    print(validating_record.exists)
    print(validating_record.score)
