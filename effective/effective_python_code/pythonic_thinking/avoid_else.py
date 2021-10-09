"""
Avoid else block after for and while loops.
Previously, what we use were try -> except -> else, and if -> elif -> else.

But Python loops have an extra feature as well. This feature is not available in most other programming languages: we
can put an else block immediately after a loops repeated interior block.
The else block runs immediately after the loop finishes.

Know how to use the else block.
"""


def test_else():
    for i in range(3):
        print(f'{i} -> printing number')
    else:
        print('completed')
    print('for and else are completed')

    index = 0
    while index < 3:
        print(f'{index} -> while printing number')
        index += 1
    else:
        # after the while loop, go to else
        print('while completed')
    print('while and else are completed')

    # However, the two examples above just shows perhaps else can be replaced with normal commands.
    for x in []:
        print(f'I hope this line will be executed, {x}')
    else:
        print('For else block is executed')


if __name__ == '__main__':
    test_else()
