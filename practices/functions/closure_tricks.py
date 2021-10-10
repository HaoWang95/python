from typing import List, Optional
from datetime import datetime
import json


def sort_priority(values: List, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority2(values: List, group):
    found: bool = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group):
        self._group = group
        self.found = False

    def __call__(self, x):
        if x in self._group:
            self.found = True
            return 0, x
        return 1, x


def log(message: str, when=None):
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


def decode(data, default=None):
    """
    Load json data from a string
    :param data: Json data to decode
    :param default: Defaults to an empty dict
    :return:
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


def log_typed(
        message: str,
        when: Optional[datetime] = None
) -> None:
    """
    A typed log method
    :param message: the log message
    :param when: the log time
    :return: None
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


if __name__ == '__main__':
    log("This is a testing message")
    log("This is a debug message")
