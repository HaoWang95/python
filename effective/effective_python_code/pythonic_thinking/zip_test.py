from typing import List  # represents list

"""
From the zip documentation by using help(zip), we can read that zip takes a '*iterables' as parameter. Which means zip is
a built-in function to deal with multiple iterables.
zip can process iterators in parallel.
zip has a limitation: the ideal scenario of using zip is the two lists share the same length, if the length is
different, then it will hold to the short one. zip will keep yielding tuples until any one of the wrapped iterators is
exhausted.

Python typing: the typing module is used for type suggestions.
"""


def get_help_zip():
    help(zip)


def test_zip():
    names: list[str] = ['Maria', 'Harrison', 'Joe', 'William', 'Christopher']  # initialized name list
    # we need the length of each name into a list so that we can find the longest name here
    name_len: list[int] = [len(name) for name in names]  # based on the initialied name list, we can derive a len list
    # find out the longest name
    longest_name: str = None
    max_len = 0
    # based on the fact that the longest name in names:list  and the largest value in name_len have the same index
    for i, length in enumerate(name_len):
        if length > max_len:  # if this length is larger than max_len
            max_len = length
            longest_name = names[i]
    print(longest_name)
    # The code above works properly but has one problem, it's too complex and visual noisy
    # to iterate over these two lists, zip can help. Instead of iterate two lists separately, we can do it all-together
    flower_list: list[str] = ['vanilla', 'acacia', 'heather', 'Primrose flowers']
    flower_len: list[int] = [len(flower) for flower in flower_list]
    longest_flower: str = None
    max_flower_len = 0
    # using zip, the code below is a for each loop on both flower_list and flower_len
    for flower, lenth_flower in zip(flower_list, flower_len):
        if lenth_flower > max_flower_len:
            max_flower_len = lenth_flower
            longest_flower = flower
    print(longest_flower)
    # Now we know how we can use zip, we also need to know its limitations.
    zip1: list = [1, 2, 3, 4, 5]
    zip2: list = [1, 2, 3, 6, 7, 9]
    for zip1_item, zip2_item in zip(zip1, zip2):
        print(f'zip1: {zip1_item}, zip2: {zip2_item}')


def zip_review():
    names: List[str] = ['Joe', 'Jessie', 'Peter', 'John', 'Johnny', 'Tom', 'Johnathon']
    # list comprehension: use names to calculate the length
    names_length: List[int] = [len(name) for name in names]

    # Now we need to find the longest name and the corresponding length
    longest_name: str = None
    max_len: int = 0
    for i in range(len(names)):  # can be replaced with enumerate
        current_len: int = names_length[i]  # current temp length can be referenced via names_length
        if current_len > max_len:
            longest_name = names[i]
            max_len = current_len
    print(longest_name, max_len)

    # however, the code above is quite visual noisy. we can reduce the range(len(...)) to a enumerate
    longest_name_2: str = None
    max_len_2: int = 0
    for index, name_item in enumerate(names):
        temp_len: int = names_length[index]
        if temp_len > max_len_2:
            max_len_2 = temp_len  # if the current length is even longer, then the max length will be the current length
            longest_name_2 = name_item
    print(longest_name_2, max_len_2)

    # the code above can be iterated at the same time
    longest_name_3: str = None
    max_len_3: int = 0
    for name, name_len in zip(names, names_length):
        if name_len > max_len_3:
            max_len_3 = name_len
            longest_name_3 = name
    print(longest_name_3, max_len_3)


if __name__ == '__main__':
    # get_help_zip()
    # test_zip()
    zip_review()
