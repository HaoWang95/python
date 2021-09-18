"""
Python has two types that represent sequences of character data: bytes and str.
Instances of bytes contain raw, unsigned 8-bit values(which means, from our current understanding, bytes is more of a
lower-level representation of sequences of character-like data).

Then another concept we need to know is how we can transfer a str to a bytes. And how we can transfer a bytes into str.
Use the decode and encode method to achieve this.

If we have a str, then the builtin is encode, encode a str to bytes
If we have a bytes, then the builtin is decode, decode a bytes to str
"""


def test_bytes():
    my_bytes: bytes = b'hello world'  # bytes can start with a prefix b
    print(my_bytes)
    print(list(my_bytes))  # check what exactly my_bytes is
    print(list(b'abcdefg'))  # the number here is binary not hex or ox


def bytes_to_str(target_bytes: bytes):
    # check if the target_bytes is of type bytes
    if isinstance(target_bytes, bytes):
        return target_bytes.decode(encoding='utf-8')
    else:
        return target_bytes


def str_to_bytes(target_str: str):
    if isinstance(target_str, str):
        return target_str.encode(encoding='utf-8')
    else:
        return target_str


if __name__ == '__main__':
    test_bytes()
    print(bytes_to_str(b'hello world'))
    print(str_to_bytes('hello world'))
    print("This is a string".encode())
    print(b"This is bytes, now I will change it to str".decode())
