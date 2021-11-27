# Pythonic Functions
> The very first tool programmers use in Python is the function. It is the very first basic concept that we learned to
> use the keyword 'def' to define a function. Functions can break a large program into small, reusable pieces of code. Also,
> Python functions have some extra features(might be unique to Python) we can use to make our programming life easier.
### Section 1.1 Never unpack more than three variables when function return multile values
```python
item1, item2, item3 = (1, 2, 3)
```
### Section 1.2 Use Positional arguments flexibly.
Functions that accept *args are best for situations where you know the number of inputs in the argument list will be
small.
We should note that when using *args, we can not add new positional arguments to a function in the future without changing
every caller.(Because after a new positional arguments is included, existed function calls needs to be migrated to keep
consistent with the argument list.)
> Functions can accept a variable number of positional arguments by using *args in the def statement.
> We can use the items from a sequence as the positional arguments for a function with the * operator.
> Using the * operator with a generator may cause a program to crash.
> Adding new positional parameters to functions that accepts *args can introduce hard to detect bugs.

### Raise an exception instead of returning None
When we write utility functions, it's quite likely to simply return Nothing, or return a None. This seems to make sense
in some cases.
```python
def divide(a, b):
    return a / b 
```
The code snippet above seems to work properly under some conditions. But we can do some different modifications to this
functions to improve its error handling capabilities.

### Provide optional behavior with keyword arguments
### Use None and Docstrings to specify module and function documentation
Docstrings is a general description of the function.(It's quite straightforward to provide a docstring in pycharm)
> Using None for default argument values is especially important when the argument is mutable.