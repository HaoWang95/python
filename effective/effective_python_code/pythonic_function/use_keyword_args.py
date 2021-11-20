from typing import Dict


def remainder(number, divider):
    """
    Positional arguments, number and divider can be specified with the format of keyword arguments.
    Pay attention to the error: SyntaxError: positional argument follows keyword argument.
    :param number: number
    :param divider: divider
    :return: remainder
    """
    return number % divider


def print_params(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    my_kwargs: Dict[str, int] = {
        'number': 20,
        'divider': 6,
    }
    num_kwargs: Dict[str, int] = {
        'number': 1312,
    }
    divider_kwargs: Dict[str, int] = {
        'divider': 6
    }
    print(remainder(20, 6))
    print(remainder(number=20, divider=6))
    print(remainder(20, divider=5))
    print(remainder(**my_kwargs))
    print(remainder(**num_kwargs, **divider_kwargs))
    print_params(alpha=1.5, beta=0.9, gamma=1.2)
