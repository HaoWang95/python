"""
String formatting is the process of combining predefined text with data values into a single human-readable message that
's stored as a string. Python has four different ways of formatting strings that are built into the language and
standard library.

The syntax for format specifiers comes from C's printf function. This is one of the most basic usage.
But there are four problems with it.
1. If you change the type or order of data values in the tuple on the right side of a formatting expression, we can get
type errors due to type conversion incompatibility.
2. C-style formatting expressions will become very difficult to read. It will also become very hard to change.
3. If you want to use the same value in a format string multiple times, you have to repeat it in the right side tuple.
Therefore, we have a new solution with dictionary.

The format Built-in and str.format.
Python 3 added support for advanced string formatting that is more expressive than the old C-style format strings that
use the % operator. For individual Python values, this new functionality can be accessed throught the format build-in
function.
, represents thousands operator
^ for centering string value
"""


def my_printf():
    key = 'this is a my variable'
    value = 3.14
    formatted = '%s = %.2f' % (key, value)
    print(formatted)
    formatted_2 = '%10s = %.2f' % (key, value)
    print(formatted_2)
    # c-style formatting can be difficult to read
    # c-style formatting can be hard to make small changes
    pantry: list = [
        ('avocados', 1),
        ('bananas', 2),
        ('apples', 4)
    ]
    # For now, it seems just complicated, but wait
    for index, (fruit, count) in enumerate(pantry):
        print('# %d: %-10s -> %d' % (index, fruit, count))
    # It is now becoming a little bit hurtful to read
    for index, (fruit, count) in enumerate(pantry):
        print('# %d: %-10s -> %d' % (index + 1, fruit.title(), round(count)))
    my_name: str = 'alan'
    age: int = 25
    template: str = '%s is %d years old, %d years ago, %s was born'
    formatted_str = template % (my_name, age, age, my_name)
    cook: str = '%s loves food, see %s cook' % (my_name, my_name)
    print(formatted_str)
    print(cook)


# An alternative to replace the initial string format is to replace tuple with dictionary
def my_printf_dict():
    my_name: str = 'alan'
    template: str = '%(name)s loves food, see %(name)s cook' % {'name': my_name}
    print(template)
    pantry: list = [
        ('avocados', 1),
        ('bananas', 2),
        ('apples', 4)
    ]
    for index, (fruit, count) in enumerate(pantry):
        print("#%(index)d: %(fruit)-10s %(count)d" % {'index': index, 'fruit': fruit, 'count': count})


def test_format():
    pi = 3.14
    val = 1234.5678
    greeting: str = 'Hello world'
    print(format(pi, '.4f'))
    print(format(val, ',.2f'))
    print(format(greeting, '^20s'))


if __name__ == '__main__':
    a = 0b10111011
    b = 0xc
    print("For value a, the decimal value of binary a is %d" % a)
    print("For value b, the decimal value of hex b is %d" % b)
    # my_printf()
    my_printf_dict()
    test_format()
