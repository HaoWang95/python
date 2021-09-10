import time
from threading import Thread


def countdown(n):
    print()
    print('T-minus ', end=' ', flush=True)
    while n > 0:
        n -= 1
        print('\b' + f'{n}', end='', flush=True)
        time.sleep(1)


if __name__ == '__main__':
    temp_thread = Thread(target=countdown, args=(10,))
    temp_thread_2 = Thread(target=countdown, args=(11,))
    temp_thread.start()
    temp_thread_2.start()
