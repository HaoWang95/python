"""
From the zip documentation by using help(zip), we can read that zip takes a '*iterables' as parameter. Which means zip is
a built-in function to deal with multiple iterables.
zip can process iterators in parallel.
zip has a limitation: the ideal scenario of using zip is the two lists share the same length, if the length is
different, then it will hold to the short one. zip will keep yielding tuples until any one of the wrapped iterators is
exhausted.
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


if __name__ == '__main__':
    # get_help_zip()
    test_zip()
