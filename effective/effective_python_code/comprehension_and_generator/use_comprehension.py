from typing import List

"""
In this file, we will compare the differences of using Python comprehension and using map and filter.
Example, for a given number list, we want to make each item to be squared.
There are several different approaches we can achive this. 
1. Use the old, east for loop to iterate over the target list and square each item one by one.
2. Use the comprehension(which we know before) as a one-liner Python.
3. Use map function, map + lambda function.
"""


# This is the common way
def basic_iteration(number_list: List):
    """
    :param number_list: A list that contains the origin numbers
    :return: None
    """
    result_numbers: List = []  # Container to hold the squared numbers
    for num in number_list:
        result_numbers.append(num ** 2)
    print(f'In basic iteration -> {result_numbers}')


def basic_comprehension(number_list: List):
    """
    :param number_list: A list that contains the origin numbers
    :return: None
    """
    result_numbers: List = [x ** 2 for x in number_list]
    print(f'In basic comprehension -> {result_numbers}')


def check_map_definition():
    help(map)


def check_filter_definition():
    help(filter)


def square(num):
    return num ** 2


def is_even(num):
    return num % 2 == 0


def basic_map(number_list: List):
    """
    map(func, *iterables)
    func -> operation
    *iterables -> items
    So the logic of map is to map each single item in items to perform the operation.
    In our case, we map each number to perform the square operation.
    :param number_list: origin numbers
    :return:
    """
    result_numbers: List = list(map(square, number_list))  # what we got here is a map object
    print(f'In basic map -> {result_numbers}')


def basic_lambda_map(number_list: List) -> None:
    result_numbers: List = list(map(lambda x: x ** 2, number_list))
    print(f'In basic lambda map -> {result_numbers}')


def even_number_square_comprehension(number_list: List):
    # comprehension with filtering
    even_squares: List = [num ** 2 for num in number_list if num % 2 == 0]
    print(f'In even number square comprehension: {even_squares}')


def even_number_square_basic(number_list: List):
    even_squares: List = []
    for num in number_list:
        if num % 2 == 0:  # Filtering
            even_squares.append(num ** 2)
    print(f'In even number square basic: {even_squares}')


def even_number_square_map_filter(number_list: List):
    # map with filtering
    even_squares = list(map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, number_list)))
    even_squares_alt = list(map(square, filter(is_even, number_list)))
    print(f'In even number square map_filter: {even_squares}')


if __name__ == '__main__':
    example = [1, 2, 3, 4, 5, 6, 7, 8]
    basic_iteration(example)
    basic_comprehension(example)
    basic_map(example)
    basic_lambda_map(example)
    even_number_square_basic(example)
    even_number_square_comprehension(example)
    even_number_square_map_filter(example)
