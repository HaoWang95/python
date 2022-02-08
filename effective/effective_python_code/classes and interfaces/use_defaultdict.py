from collections import defaultdict


# A very basic example of our use case
class SimpelGradeBook:
    def __init__(self):
        self.__data = {}

    def add_record(self, name: str, grade: int):
        self.__data[name] = grade
    # __str__ or __repr__


def handle_missing() -> str:
    return "The key is not present in the dict"


def log_missing() -> int:
    print('The key is not present and is now added into the dict')
    # The returned value here will be applied as the default value
    return 0


if __name__ == '__main__':
    grade_book = defaultdict(handle_missing)
    print(grade_book)
    # After printing the default dict, we can see it's a defaultdict object <defaultdict, {}>
    grade_book['albert'] = 90
    print('The grade for albert is ' + str(grade_book['albert']))
    print('The grade for alan is ' + grade_book['alan'])

    current_grade = {
        "albert": 100, "joe": 75
    }

    incoming_grade = [
        ('alan', 0), ('william', 60), ('alice', 120)
    ]

    # we cover the empty dict in defaultdict with our current_grade records
    grade_result = defaultdict(log_missing, current_grade)
    # log_missing attributes will take care of missing items, and current_grade dict will be our data storage
    print("Before processing: ", dict(grade_result))
    for name, grade in incoming_grade:
        grade_result[name] += grade
    print('After: ', dict(grade_result))
    print('Looking for John, ', grade_result['John'])
