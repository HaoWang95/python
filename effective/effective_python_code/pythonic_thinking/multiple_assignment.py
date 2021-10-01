"""
Multiple assignment unpacking over indexing.
Tuple: built-in type,(...items). For Python built-in type, we have a **built_in_type()** method.
For example,
tuple -> tuple()  # constructs a tuple
list -> list()  #  constructs a list,
...
A common usage of this built-in functions are to build the type from other types

Tuple type can be used to create immutable, ordered sequences of values. Once we created a tuple, we can not modify
the tuple by assigning a new value to an index.

Unpacking allows to assign multiple values in a single statement.
We can use _ to skip unnecessary items.(If we know the exact items)
We can use * to skip a number of items.

Take away note:
1. Python has special syntax called unpacking for assigning multiple values in a single assignment
2. Unpacking is generalized in Python and can be applied to any iterable(for something in ds/list/tuple/str), including
many levels of iterables within iterables
3. Reduce visual noise and increase code clarity by using unpacking to avoid explicitly indexing into sequences.
"""


def test_tuple():
    items: tuple = ('chips', 'peanuts', 'chicken')  # we initialized this tuple, called items
    print(f'this is the items tuple: {items}')
    snacks: dict = {
        'chips': 50,
        'peanuts': 100,
        'chicken': 2
    }
    # How can we convert a dict into a tuple
    snack_tuple: tuple = tuple(snacks.items())  # we convert the snacks dict into tuple
    print(f'this is the snack tuple: {snack_tuple}, length is {len(snack_tuple)}')
    print(f'The first element in snack tuple {snack_tuple[0]}')


def test_assignment():
    bag: tuple = ('item', 'widget', 'toy', 'comic book')
    # If we don't know about unpacking, we may iterate over the iterable to find the element
    for item in bag:
        print(f'do something with {item}')
    # Or we may use index
    item, widget, toy, comic_book = bag
    # print the above items to see whether we have fetched them correctly
    print(item, widget, toy, comic_book)
    # What if we know the items, but we would like to skip some of them, for example, we just want the last two
    _, _, third, fourth = bag  # _ is more like a convention, means skip something
    print(f'third: {third}, fourth: {fourth}')
    # or we just want the first two
    first, second, _, _ = bag
    print(f'first: {first}, second: {second}')
    # Now we come to a more complex situation, what if we don't know the exact elements? But say we still want to
    # use elements selectively?
    black_box: list = [1, 2, 3, 5, 6, 7, 23, 135, 3646, 546, 57553, 321515, 373462, 97593252, 638, 271, 358]
    # Now we have a block_box, what if we just want the first and the last?
    print(f'Initially we can use index -> black_box[0] = {black_box[0]}, black_box[-1] = {black_box[-1]}')  # list
    # index slicing
    # What if we want the values except the first one and the last one? -> how we can find the middle items
    # Hint: use the star *
    first_num, *middle_num, last_num = black_box  # advanced unpacking
    print(f'First element:{first_num}, middle elements:{middle_num}, last element:{last_num}')
    # Now what if we want all elements except the first one. -> (first_one , *rest)
    first, *rest = black_box
    print(first, rest)
    # What if we want all except the last one -> (*not_last, last)
    *first_part, last = black_box
    print(first_part, last)

    # for black box, if we want the first two and last two elements
    first, second, *mid, last_two, last_one = black_box
    print(first, second, mid, last_two, last_one)
    # *frontpart, midnum, *restpart = black_box  # This will fail, because Python can not make sure how long it is for
    # the frontpart and how long for the rest part.
    # how long is frontpart? we don't know. how long is restpart? we don't know


def test_unpacking():
    greeting = "Hello"
    # If we just want the first letter
    first_letter, *rest = greeting
    print(type(first_letter), type(rest))
    # If we want the last letter
    *first_part, last_letter = greeting
    print(first_part, last_letter)
    # first_letter, middle_part, last_letter


def test_():
    _ = 'This is a variable'
    print(_)
    for i in range(10):
        print(i)

    for _ in range(10):
        print(_)


def test_method(*args):
    # args is a tuple, immutable
    print(args, type(args))


if __name__ == '__main__':
    test_assignment()
    # test_tuple()
    # test_unpacking()
    test_method(1, 2, 3, 4, 5, 'albert', 'and', 'alan')
