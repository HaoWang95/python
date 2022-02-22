"""
How many init method can a Python class have? 1 __init__
@classmethod decorator, enables us to have another way to define a constructor/init
"""


class Creature:
    def __init__(self, type_description: str):
        """
        self represents the instance
        """
        self.type = type_description

    @classmethod
    def from_data(cls, type_description: str):
        """
        cls: = Creature class
        :param type_description:
        :return:
        """
        return cls(type_description=type_description)  # == Creature(type_description = type_description)

    def __repr__(self):
        return f'The creature type is {self.type}'


class Bank:
    def __init__(self, balance: int, bank_name: str):
        self.__balance = balance  # private fileds
        self.__bank_name = bank_name  # private fileds

    @property  # getter
    def balance(self):
        return self.__balance

    @balance.setter  # setter
    def balance(self, new_balance: int):
        self.__balance = new_balance

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, new_bank_name: str):
        self.__bank_name = new_bank_name

    # Create an __init__ alternative
    @classmethod
    def create_bank(cls, balance: int = 0, bank_name: str = ""):
        return cls(balance, bank_name)

    @staticmethod
    def cal_interest(current_balance, interest_rate, year=1) -> float:
        """
        Assume that the interest rate is 4%
        :return:
        """
        print("To calculate interest for a bank")
        return (current_balance + (current_balance * interest_rate)) * year

    def change_balance(self, amount, increase=True):
        if increase:
            self.__balance = self.__balance + amount
        else:
            self.__balance = self.__balance - amount

    def __repr__(self):
        return f'Bank {self.__bank_name}: {self.__balance}'


if __name__ == '__main__':
    plant = Creature(type_description="Plant")  # We use Creature.__init__()
    germ = Creature.from_data(type_description="Germ")  # We use our classmethod to define an instance,
    print(f'Creature -> {plant}')
    print(f'Creature -> {germ}')

    albert_bank_au = Bank(balance=10000, bank_name="ABB_AU")
    albert_bank_au.change_balance(10000, increase=True)
    print(albert_bank_au)
    blank_bank_au = Bank.create_bank()
    blank_bank_au.bank_name = "ALB AU NEW PTY LMT"
    blank_bank_au.balance = 1000000
    blank_bank_au.change_balance(50000, increase=False)
    print(blank_bank_au)

    albert_interest = albert_bank_au.cal_interest(albert_bank_au.balance, 0.04, year=1)
    blank_interest = blank_bank_au.cal_interest(blank_bank_au.balance, 0.04, year=1)

    print(f'albert bank 1 yr interest: {albert_interest - albert_bank_au.balance}')
    print(f'blank bank 1 yr interest: {blank_interest - blank_bank_au.balance}')

    interest = Bank.cal_interest(10000, 0.04, 10)
    print(f"10000 - 4% - 10 yrs -> {interest}")
