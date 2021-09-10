import random
import time
import string
from threading import Thread, Lock

BAR = chr(9608)
BAR2 = '*'
BAR3 = '#'


def getProgressBar(progress, total, barwidth=40):
    """
    Use this method to generate the progress bar
    :param progress: the current downloading progress
    :param total: the total size of the file
    :param barwidth: barwidth param
    :return: returns a string that represents a progress bar that has barWidth bars and has progressed
    progress amount out of the total amount
    """
    progressBar = '['
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
    # calculate the number of bars to display
    numberOfBars = int((progress / total) * barwidth)
    progressBar += BAR3 * numberOfBars  # Append the rest of the bar
    progressBar += ' ' * (barwidth - numberOfBars)  # Add the empty space
    progressBar += ']'
    # calculate the completed percentage
    percentCompete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentCompete) + '%'
    progressBar += ' ' + str(progress) + '/' + str(total)
    return progressBar


def get_random_string(length):
    letter = string.ascii_lowercase
    result = ''.join(random.choice(letter) for _ in range(length))
    return result


def main():
    # print('Downloading, please wait...')
    downloaded = 0
    downloadSize = 10000
    while downloaded < downloadSize:
        downloaded += random.randint(0, 150)
        barStr = getProgressBar(downloaded, downloadSize)
        # We need not print a new line at the end, we need to flush the printed string to the screen
        print(f'Get {get_random_string(3)}-{get_random_string(10)}-{barStr}', end='', flush=True)
        time.sleep(0.15)
        print('\b' * (len(barStr) + 19), end='', flush=True)
        # print(f'{get_random_string(10)}', end='', flush=True)


def run_progress():
    # print(f'Downloading...')
    name = get_random_string(5)
    dowloaded = 0
    downloadSize = 10000
    while dowloaded < downloadSize:
        dowloaded += random.randint(0, 150)
        bar = getProgressBar(dowloaded, downloadSize)
        print(f'Downloading: {name} {bar} ,completed {get_random_string(5)}-{get_random_string(15)}')
        time.sleep(0.3)
    print(f'{name} download completed')


if __name__ == '__main__':
    t1 = Thread(target=run_progress)
    t2 = Thread(target=run_progress)
    t1.start()
    time.sleep(3)
    t2.start()
    # main()
