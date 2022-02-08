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