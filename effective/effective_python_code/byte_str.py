"""
In python, there are two types that represent sequences of character data: bytes and str.
Bytes contains raw, unsigned 8-bit values, often in the ASCII encoding.
The bytes have a prefix of b'{content}', the letter b here represents bytes.
Importantly, python str do not have an associated binary encoding, and bytes instances do not have an
associated text encoding.

Task for this item:
Find out a mechanism that transfer bytes to string and verse visa.
The hint is to use the decode and encode method

Note: we can always use the + operator to add str to str, and bytes to bytes.
But we can not use them on bytes and str
"""
from typing import Union


def bytes_to_str(target_bytes: bytes) -> Union[str, bytes]:
    if isinstance(target_bytes, bytes):
        result = target_bytes.decode('utf-8')
        return result
    else:
        return target_bytes


def str_to_bytes(target_str: str) -> Union[bytes, str]:
    if isinstance(target_str, str):
        result = target_str.encode(encoding="utf-8")
        return result
    else:
        return target_str


#  write_bytes method shows how to write bytes into a file.
#  If we want to read or write bytes to/from a file, always open the file using a binary mode
def write_bytes(target_bytes: bytes):
    with open('mybytes.txt', 'wb') as file:
        file.write(target_bytes + b' nice to see you')


def read_bytes():
    with open("mybytes.txt", 'rb') as file:
        content = file.read()
        print(content, list(content))


if __name__ == '__main__':
    greeting: bytes = b'hello world'
    print(b'this is a bytes', list(b'this is a bytes'))
    print(bytes_to_str(greeting))
    print(str_to_bytes("hello world"))
    write_bytes(greeting)
    read_bytes()
