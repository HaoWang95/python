# Effective Python Part 2:  Know Python List and Dict
## Section 1: What is a .md file
A file that ends with .md means this is a markdown file. A markdown file is usually
provided in a project for documentation. Also, a markdown file can be used to take
notes.
### 1.1 Below are some markdown tricks
If we want to start a 'sub-section' to illustrate some ideas in further detail, we
can use '>' symbol to start a section.
> This is one of the subsection example
> How to use a markdown to label a list of items
> * Use star * to label an unordered list of items
> * This is item 1.
> * This is item 2.

### 1.2 How to insert bold text
This is a line of normal text.\
**This is a line of bold text**\
*This is a line of italic text*

### 1.3 How to insert code into markdown
```python
# Below are code snippet samples in markdown
from datetime import datetime
print(datetime.now())
```

## Section 2: Advanced features of Python list and dict
Python list and dict are two common data structures that we use in daily programming.
### 2.1 Know how to slice a sequence
Python has a special syntax called **slicing** which slice sequences into pieces. This feature has been borrowed by many 
other programming languages. A simple use case for slicing are for built-in types **list, str and bytes**. **What we don't
know is slicing can be extended to any Python class that implements the 'getitem' and 'setitem' special methods**.
**The basic format of slicing some_sequence[start: end]**
### 2.2 Skip the first and last index to reduce the visual noise
> Avoid being too verbose when slicing a Python sequence, don not supply 0 for the start index or the length of the seq
> for the end index.
```python
test_sequence: str = 'This is the sequence we are going to slice'
print(test_sequence[0:5], test_sequence[:5])
assert test_sequence[0:5] == test_sequence[:5]
print(test_sequence[5:len(test_sequence)], test_sequence[5:])
assert test_sequence[5: len(test_sequence)] == test_sequence[5:]
```
> Be aware of the negative value in slicing, especially -1

### 2.3 Avoid striding and slicing in a single expression
Python supports striding operation when slicing in the form of **test_sequence[start:end:stride]**. This feature allows
us to take every stride'th item when slicing a sequence.
```python
test_sequence: list = ['red', 'green', 'yellow', 'blue', 'purple', 'black', 'orange']
odds = test_sequence[::2]  # [::2], first : means start=0, second : means end=len(test_sequence), stride=2
even = test_sequence[1::2]  # [1::2] start from 1, end=len(test_sequence), stride=2
what_is_this = test_sequence[::1]  # [::-1]
what_is_this_2 = test_sequence[::-1]
what_is_this_3 = test_sequence[::-2]
what_is_this_4 = test_sequence[:1:-2]
print(f'odds: {odds}')
print(f'even: {even}')
print(f'what_is_this ? -> {what_is_this}')
print(f'what_is_this_2 ? -> {what_is_this_2}')
print(f'what_is_this_3 ? -> {what_is_this_3}')
print(f'what_is_this_4 ? -> {what_is_this_4}')
```
The point here is the stride part of the slicing syntax can be extremely confusing because we are facing with many :::.
Having three numbers with some :: in the brackets is hard to read because of its comprehension density. Therefore, pls 
know that Python supports another syntax called striding. And we just need to know some basic striding like [::-1], 
[::-2], [::2], and [1::2]. And always avoid complex striding because it is very confusing to understand