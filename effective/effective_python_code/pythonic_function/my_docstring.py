"""
This is a quick remainder that a Python file can be treated as an importable module.
"""


def test_function(param1: str, param2: float, *args) -> dict[int, str]:
    """
    This is a test function to illustrate the docstring
    :param param1: an explanation of param1
    :param param2: an explanation of param2
    :param args: an explanation of param3
    :return: dict[int: str]
    """
    pass


class TestDoc:
    """
    This is a test doc class, for detailed explanation, refer to the manual below
    .....
    """

    def __init__(self, value=None) -> None:
        """
        this is the initializer of test doc class
        :param value: init value
        """


if __name__ == '__main__':
    # what is the hidden behavior of __doc__ ?
    print(__doc__)
    # what is the hidden behavior of function.__doc__ ?
    print(test_function.__doc__)
    print(TestDoc.__doc__)
    import datetime
    print(datetime.datetime.__doc__)
    import subprocess
    print(subprocess.__doc__)
