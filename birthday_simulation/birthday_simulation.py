from random import randint


# By using this method below, we can calculate the average number of person that two people share the same birthday
def birthday_generation():
    is_repeated: bool = False
    generated_birthday: list = []
    while not is_repeated:
        temp_birthday = randint(0, 354)
        # print(f'The generated birthday is {temp_birthday}')
        if len(generated_birthday) != 0:
            for birthday in generated_birthday:
                if birthday == temp_birthday:
                    is_repeated = True
                    break
        if is_repeated is False:
            generated_birthday.append(temp_birthday)
    # The length of the generated_birthday will be the number of selected people
    return len(generated_birthday)


# Another approach is between 0 - 364 or 1 - 365, we generate 23 different numbers, by running it for many times,
# we calculate the overall probability that the generated list contains two same number
def birthday_list():
    return [randint(0, 364) for _ in range(23)]


# How can we verify if the birthday list contains two same value
def verify_unique_birthday(birthday_list: list):
    unique_birthdays = set(birthday_list)
    total_birthdays = len(birthday_list)
    birthday_repeated = len(unique_birthdays) != total_birthdays
    return birthday_repeated


if __name__ == '__main__':
    people_number: list = []
    for i in range(1000000):
        random_people_number = birthday_generation()
        people_number.append(random_people_number)
    print(
        f'After running 100000 times, the average number of random people sharing the same birthday is '
        f'{int(sum(people_number) / len(people_number))}')

    num_repeated = 0
    for _ in range(100000):
        birthdays = birthday_list()
        if verify_unique_birthday(birthdays):
            num_repeated += 1
    print(f'The probability of in a group of 23 randomly chosen people that 2 share the same birthday is {num_repeated/100000}')