"""
This is a birthday paradox simulation.
The approach is to randomly generate a list that contains 23 randomly chosen
birthdays. For each time a birthday list is generated,(the length should be 23), we check if the current list contains
two same values, if these two values exist, we can add true into the statistics, or we can add a repeated_times variable
by 1.

Implementation plan,
1. Generate a birthday list that contains 23 randomly chosen birthday, please note the range of the birthday is between
0 - 364 or 1 - 365. To test this method, we can print out the generated list when it's done.

2. We need to validate if this generated birthday_list contains the same birthday value. This part may sound a little
bit of tricky, but it can be solved by using Python basic data structure that we already know(set).
Why using set? Because element in set is not repeatable. If we use the generated birthday_list, and turn into a set,
repeated element in the list will be reduced and that means the length of the birthday_list and birthday_set is different.

3. With these two methods completed, we can generate and then validate the birthday list. Now what we need to do if we
need to perform the tests for 10000 or 100000 times? We need a processing method that keeps running the above process
for 10000 times. (Decorator)
"""
from random import randint

GROUP_NUMBER = 23
TEST_ROUNDS = 100000


# This method is implementation plan section 1,
def list_generation_v1(people_number):
    birth_list: list = []
    for _ in range(people_number):
        temp_birth = randint(0, 364)  # randint(0, 364)  x >= 0  and x <= 364
        birth_list.append(temp_birth)
    print(birth_list)
    return birth_list


# This is the second, one-line implementation of the generation of birthday_list
def list_generation_v2(people_number):
    return [randint(0, 364) for _ in range(people_number)]


def birthdaylist_validation(birthday_list: list):
    birthday_set = set(birthday_list)
    # By converting to a set, we can check if there are duplicates
    # If there are no duplicate, the set and the list will have the same length or their lengths are different.
    if len(birthday_set) != len(birthday_list):
        return True
    return False


def process(round_number):
    duplicate_times = 0
    prev_index = 0
    for index in range(round_number):
        birthday_list = list_generation_v2(GROUP_NUMBER)
        is_repeated = birthdaylist_validation(birthday_list)
        if is_repeated:
            duplicate_times += 1
        if index == 1000 and prev_index == 0:
            prev_index = 1000
            print('1000 tests completed, running....')
        if (index - prev_index) == 1000:
            prev_index = index
            print('1000 tests completed, running....')

    print(f"""After running the test for {round_number} times, 
            the probability of 23 people that two of them have the same birthday is {(duplicate_times / round_number) * 100}%""")


if __name__ == '__main__':
    print(f'The simulation starts....')
    process(TEST_ROUNDS)
