"""
Much of programming in Python is defining classes that contain data and describing how such objects relate to each other.
In this class/file, we will define a data container class called FrequencyList that can calculate frequencies of elements
inside the list.
"""


class FreqList:
    def __init__(self):
        # we will use the elements list to calculate frequencies
        self.elements = []

    # The cal_frequencies method will calculate the element frequency.
    def cal_frequencies(self):
        pass


# Another approach is we define our own data structure to implement the feature
class FrequencyList(list):
    def __init__(self, memebers):
        # super is a quick approach to init the parent class
        super().__init__(memebers)

    def calculate_frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


if __name__ == '__main__':
    alphabet = FrequencyList(['a', 'a', 'b','b', 'c','f'])
    print(alphabet.calculate_frequency())