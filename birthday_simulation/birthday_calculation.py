"""
This is the second approach to test the birthday paradox. To differentiate from the approach we just completed.
1. We keep generating the random birthdays, until we find duplicates. When we find a duplicate, we record the number of
times we've used. For example, the times can be 10, 50, 23,40, 200, ...
2. Then based on the times data above, say we run the tests for 100000 times, we can calculate the average times it takes
to generate a birthday list with duplicates.
"""
from random import randint

ROUND_TIMES = 100000


def birthday_generation():
    birthday_list: list = []
    is_duplicate: bool = False
    while not is_duplicate:
        temp_birthday = randint(0, 364)
        # After generating the temp_birthday, we need to check whether this is a duplicate with elements in
        # birthday_list
        for birthday in birthday_list:
            if birthday == temp_birthday:
                is_duplicate = True
                break
        if is_duplicate:
            break
        birthday_list.append(temp_birthday)
    return len(birthday_list)


def process_average(times):
    generation_times: list = [birthday_generation() for _ in range(times)]
    print(
        f'Run times: {times}, avg generation times to have a duplicate birthday: {sum(generation_times) / len(generation_times)}')


if __name__ == '__main__':
    process_average(ROUND_TIMES)
