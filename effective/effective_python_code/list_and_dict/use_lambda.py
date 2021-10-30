"""
lambda function, we've used it in our sort key example that our_iterable.sort(key= lambda function).
"""


class Student:
    """
    Implementation of the student class
    """

    def __init__(self, student_name=None, student_age=None, student_score=None):
        self.student_name = student_name
        self.student_age = student_age
        self.student_score = student_score

    def __repr__(self):
        return f'Student(student_name={self.student_name}, student_age={self.student_age}, s' \
               f'tudent_score={self.student_score}) '

# class method
# static method
class Person:
    def __init__(self, name=None, age: int = None, address: str = None, career: str = None, ) -> None:
        self.name = name  # public
        self.__age = age  # private
        self.__address = address  # private
        self._career = career  # protected

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, new_addr) -> None:
        self.__address = new_addr

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age) -> None:
        self.__age = new_age

    @property
    def career(self) -> str:
        return self._career

    @career.setter
    def career(self, new_career) -> None:
        self._career = new_career


def test_lambda():
    person: Person = Person('John', 20, 'Melbourne', 'student')
    print(f'name is {person.name}')
    print(f'career is {person.career}')
    print(f'age is {person.age}')
    get_person_info = lambda something: (something.name, something.age, something.career)  # Anonymous function
    result = get_person_info(person)  # call the function
    print(result)


if __name__ == '__main__':
    test_lambda()
