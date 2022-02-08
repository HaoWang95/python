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

