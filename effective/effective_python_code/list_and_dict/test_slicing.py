"""
In this file, we will test the slicing feature.
"""


def slicing_items() -> None:
    """
    Consider how to slice from the start of a sequence? When slicing from the start of a list/sequence, we can leave
    out the index zero, instead of using [0:end_index], we can use [:end_index]
    Consider how to slice to the end of a sequence?
    When slicing to the end of list/sequence, we can also leave the final index. Therefore, instead of
    using [index: end], we can use [index:] directly.
    Also, we need to know how to use the negative number when slicing a sequence in Python.

    :return:
    """
    test_sequence: str = 'This is the sequence we are going to slice'
    print(test_sequence[0:5], test_sequence[:5])
    assert test_sequence[0:5] == test_sequence[:5]
    print(test_sequence[5:len(test_sequence)], test_sequence[5:])
    assert test_sequence[5: len(test_sequence)] == test_sequence[5:]
    print(test_sequence[::-1])  # This trick is how to reverse a sequence


def test_striding() -> None:
    """
    ::2 means select every second item starting at the beginning.
    :return:
    """
    test_sequence: list = ['red', 'green', 'yellow', 'blue', 'purple', 'black', 'orange']
    odds = test_sequence[::2]  # [::2], first : means start=0, second : means end=len(test_sequence), stride=2
    even = test_sequence[1::2]  # [1::2] start from 1, end=len(test_sequence), stride=2
    what_is_this = test_sequence[::1]  # [::-1]
    what_is_this_2 = test_sequence[::-1]
    what_is_this_3 = test_sequence[::-2]
    what_is_this_4 = test_sequence[:1:-2]
    print(f'odds: {odds}')
    print(f'even: {even}')
    print(f'what_is_this ? -> {what_is_this}')
    print(f'what_is_this_2 ? -> {what_is_this_2}')
    print(f'what_is_this_3 ? -> {what_is_this_3}')
    print(f'what_is_this_4 ? -> {what_is_this_4}')


if __name__ == '__main__':
    # slicing_items()
    test_striding()
