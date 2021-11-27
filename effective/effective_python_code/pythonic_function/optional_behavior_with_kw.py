# Think about how we can improve this function
def remainder(number, divider):
    return number % divider


if __name__ == '__main__':
    """
    1. All normal arguments to Python functions can also be passed by keyword
    2. ** Positional arguments must be specified before keyword arguments **
    3. If we already have a dictionary, we can use its content in the dict. By using the **operator. This instructs Python
    to pass the values from the dictionary as the corresponding keyword arguments to the function.
    """
    assert remainder(number=20, divider=7) == 6
    assert remainder(25, 5) == 0
    # Positional arguments must be specified before keyword arguments
    assert remainder(number=20, divider=8) == 4

    kw_args: dict[str, int] = {
        "number": 30,
        "divider": 8,
    }
    remainder(**kw_args)  # remainder(number=kw_args.number, divider=kw_args.divider)
