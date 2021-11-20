"""
Use a positional arguments can make a function call clearer and reduce visual noise.(These positional arguments are often
called varargs for short, or star args, in reference to the conventional name for the parameter *args).

"""
from random import randint


def log(message, value) -> None:
    """
    This is an initial implementation of our log method. It should be noted, to use this function, we must provide both
    of the arguments. Or it will return TypeError: log() missing 1 required positional argument 'value'.
    Also, having to pass an empty list when I have no values to log is quite cumbersome and visually noisy for our python
    code.
    :param message: the log message
    :param value: the log value
    :return: None
    """
    if not value:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in value)
        print(f'{message}: {values_str}')


def log_v2(message, value=None) -> None:
    """
    This is a version 2 implementation of the log method, in this method, we provide a default None to value argument,
    now the default is None, we can use this function without providing further arguments.
    However, in this case, we are still assuming that the value parameter is a list, because there are no further arguments
    after value.
    :param message: the log message
    :param value: the log value
    :return: None
    """
    if not value:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in value)
        print(f'{message}: {values_str}')


def num_generator():
    for _ in range(10):
        yield randint(1, 100)


def log_v3(message, *values) -> None:
    """
    *values will be treated as optional arguments, they are always turned into a tuple. Because there is a very funny
    but important concept in Python called generator, by combing a generator, it means that if the caller of a function
    uses the * operator on a generator, it will be iterated until it's exhausted.
    Functions that accepts *args are best for situations where you know the number of inputs in the argument list will be
    reasonably small. *args is ideal for functions calls that pass many literals or variable names together. It's
    primarily for the convenience of the programmer and the readability of the code.
    Another issue that we have to think and consider is that with *args, we can not add new positional parameters/
    argumets to a function in the future without migrating every function call. If we try to add a new positional argument
    in the front of the argument list, existing function calls will have subtle erroors if they are not updated.
    :param message: the log message
    :param values: the log value
    :return: None
    """
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')


if __name__ == '__main__':
    log("This is a test log", [])  # the parameter here is a message
    log("This is my value", [1, 2, 3])  # message is a str and value is alist
    log_v2("This is log_v2 test message")
    log_v2("This is log_v2 message", [1, 2, 3, "hello world"])
    log_v3("This is a log_v3 message")
    log_v3("This is a log_v3 message", "value 1", "value2", [1, 2, 3])
    my_values = [{"age": 15}, {"hobby": "programming python"}, {"food": "shrimp"}]
    log_v3("This is my values ", "This is my sequence", my_values)
    log_v3("This is my values ", *my_values)
    gen = num_generator()
    log_v3("This is a generator", gen)
    log_v3("This is a generator", *gen)
