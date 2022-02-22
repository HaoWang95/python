# **A more detailed usage of defining and using Class in Python**

### Use functions instead of classes for simple interfaces
The core concept of this item is **DO NOT OVER-THINK**. Many of Python's built-in APIs allow us to customize behavior by
passing in a function. These hooks are used by APIs to call back our code while they execute. For example, we can use the
**list type's sort method takes an optional key argument** that's used to determine each index's value for sorting.
```python
from typing import List

# Assume that we have a list that contains many strings.

names: List[str] = ["albert", "alan", "william", "this is one name", "this is just another name"]

name_len: List[int] = [len(x) for x in names]

# What if we want to sort the names list by the length of the string

if __name__ == '__main__':
    # we simply use the len as a functional parameter when we call the sort
    print(names)
    print(name_len)
    names.sort(key=len, reverse=True)
```
Now, let's extend it to another example. Say I want to customize the behavior of the **defaultdict** class. Our customized
data structure allows us to supply a function that will be called with no arguments each time a missing key is accessed.
The function must return the default value that the missing key should have in the dictionary. 
```python
from collections import defaultdict
def log_missing() -> int:
    print('The key is not present and is now added into the dict')
    # The returned value here will be applied as the default value
    return 0

current_grade = {
    "albert": 100, "joe": 75
}

incoming_grade = [
        ('alan', 0), ('william', 60), ('alice', 120)
    ]

grade_result = defaultdict(log_missing, current_grade)
# if in other programming language

    # log_missing attributes will take care of missing items, and current_grade dict will be our data storage
print("Before processing: ", dict(grade_result))
for name, grade in incoming_grade:
    grade_result[name] += grade
print('After: ', dict(grade_result))
print('Looking for John, ', grade_result['John'])
```

## Define __call__ method to use the class instance as a simple function
```python
from collections import defaultdict
# This class will illustrate how to use a class as a functional interface/method/function
class BetterCountMissingKey:
    def __init__(self) -> None:
        self.count_missing: int = 0

    def __call__(self) -> int:
        """
        For each time the class instance is called, this function will be executed
        :return:
        """
        print('The class instance of BetterCountMissingKey is called, create a new index in target dict')
        self.count_missing += 1
        return 0


if __name__ == '__main__':
    #counter = CountKeyMissing()  # A very basic approach to create an instance of CountKeyMissing class
    better_counter = BetterCountMissingKey()
    result: defaultdict = defaultdict(better_counter, {})  # init our dict with an empty dict {}
    incoming_data: list = [
        ('Albert', 95), ('Will', 85), ('Joe', 90), ('John', 70)
    ]
    for name, score in incoming_data:
        result[name] += score
    print(result)
    """
    If the above code is executed successfully, it means we successfully insert data into our result dict.
    And it has managed to init our value
    WHY result[name] += score -> When a key is missing in the dictionary, our key error handling method returns/assigns
    the missing key by 0
    """
    print(f'Missing key count: {better_counter.count_missing}')
```

## classmethod and @classmethod
The core concept is really simple.
* Python only supports a single constructor per class: __init__(self) method. (Java, C#, C++ supports multiple constructor)
* Use @classmethod to define alternative constructors for your class.

## Know how to use @staticmethod

## How to use super to initialize parent class(Inheritance)

## Consider composing functionality with Mixin class(Mixin Type)

## Prefer public attributes over private ones (__)

## Inherit from collections.abc for Custom Container Types
When we want to create our own data container(data structure), like an enhanced list(linked list), binary tree, or other
data structures, consider inherit from collections.abc.