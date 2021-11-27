from time import sleep
from datetime import datetime
from typing import Optional


def log(message, when=None):
    """
    Log a message with current timestamp
    :param message: the message to print
    :param when: datetime of when the message occurred. Defaults to the present time
    :return: None
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


def log_typed(message: str, when: Optional[datetime] = None) -> None:
    """

    :param message: 
    :param when:
    :return:
    """
    if when is None:
        when = datetime.now()
    print(f'{message}：{when}')


if __name__ == '__main__':
    log("Test")
    sleep(1)
    log("Import and run a python module")
    print(log.__doc__)
