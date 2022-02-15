from collections import defaultdict


# In this section, we will use class as a functional interface.

class CountKeyMissing:
    """
    This class will count the missing keys in a dictionary
    """

    def __init__(self):
        self.counted = 0  # no __, so this is a public field

    def missing(self):
        print('The key does not exist, create and init a default value for the missing key')
        self.counted += 1
        return 0


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
        result[name] += score  # why +=
    print(result)
    """
    If the above code is executed successfully, it means we successfully insert data into our result dict.
    And it has managed to init our value
    WHY result[name] += score -> When a key is missing in the dictionary, our key error handling method returns/assigns
    the missing key by 0
    """
    print(f'Missing key count: {better_counter.count_missing}')
