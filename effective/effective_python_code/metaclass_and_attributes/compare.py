class Record:
    def __init__(self):
        self.exists = 1

    def __getattr__(self, item):
        """
        We only need to implement the fallback logic when the attribute/item is missing
        :param item:
        :return:
        """
        pass


class ValidatingRecord:
    def __init__(self):
        self.exists = 2

    def __getattribute__(self, item):
        """
        We need to implement all the fetch logic,
        1. When the attribute, for example self.exists, does exist in our object
        2. When the attribute is missing from the object
        :param item:
        :return:
        """
        pass
