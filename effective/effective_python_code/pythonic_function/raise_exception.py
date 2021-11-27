def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        print(error)
        return None


def divide_v2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def divide_v3(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        raise ValueError(error)  # raise an error


def careful_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid value input")


if __name__ == '__main__':
    if (val := divide(1, 0)) is not None:
        print(val)
    else:
        print("Something wrong with the division")

    success, result = divide_v2(100, 10)
    print(success, result)
    print(divide_v2(10, 100))
    print(divide_v3(100, 0))
