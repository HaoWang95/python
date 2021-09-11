import string
import random
import time
from threading import Thread

"""
In this file, we will implement a progress bar simulator.
Let's design a general format of our progress bar
  -> [                 ] 0% 0/filesize Downloading... xxx-xxxx
  -> [**               ] 1% 2/filesize Downloading... xxx-xxxx
  -> [*****            ] 5% 15/filesize Downloading... xxx-xxxx
Other formats can be
  -> [-----            ] 5% 15/filesize Downloading... xxx-xxxx
  -> [#####            ] 5% 15/filesize Downloading... xxx-xxxx
  -> [#####            ] 5% 15/filesize Unzipping/Processing/Decrypting... xxx-xxxx
We would make it dynamic, that means:
  1. The bar will keep changing [       ] -> [##       ] -> [#####      ] to show the current processing progress.
  2. The percentage number needs to keep changing as well.
  3. The filesize or the total workload amount remains the same, but the processed number will change as well.
  4. The processed content needs to change as well.
Based the technical requirements above:
  1. The bar will be influenced by the current processed number
  2. The percentage number is calculated from round((current/total)*100,1)
  3. The processed number will increase by a random number, starting from 0
  4. The processed content will be generated as a random string.
"""


# processed resource name
def generate_string(str_len):
    """
    This method will generate a random string, the length is str_len
    :param str_len: the length of the generated string
    :return: str
    """
    letters = string.ascii_lowercase
    random_str = ''.join(random.choice(letters) for _ in range(str_len))
    return random_str


def generate_bar(current_progress, total, task_name, barnumber=40):
    if current_progress > total:
        current_progress = total
    if current_progress < 0:
        current_progress = 0
    progress_bar = f'{task_name} ['
    numberOfBars = int((current_progress / total) * barnumber)  # based on current progress and total
    percentage = round((current_progress / total) * 100, 1)
    progress_bar += '#' * numberOfBars
    numberOfSpaces = barnumber - numberOfBars
    progress_bar += ' ' * numberOfSpaces
    progress_bar += ']'
    progress_bar += ' ' + str(percentage) + '%' + f' {current_progress}/{total} '
    progress_bar += 'Downloading... ' + f'{generate_string(4)}-{generate_string(8)}'
    print(progress_bar)


def run_bar():
    current = 0
    total = 10000
    print('Start processing...')
    task_name = generate_string(5)
    while current < total:
        generate_bar(current, total, task_name)
        current += random.randint(0, 150)
        time.sleep(0.5)
    print(f'{task_name} completed')


if __name__ == '__main__':
    # When we run the main entrance here, it generally means we created a running program -> process
    # In a process, we can use threading to create running threads.
    task_1 = Thread(target=run_bar)  # method/function as parameter
    # task_2 = Thread(target=run_bar)
    task_1.start()
    time.sleep(3)
    # task_2.start()
