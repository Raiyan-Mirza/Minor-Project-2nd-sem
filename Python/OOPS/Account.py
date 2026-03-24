class Account:
    def __init__(self,accnum,balance):
        self.bal= balance
        self.acc=accnum

    def debit(self,amount):
        self.bal -= amount
        print(f"You({self.acc}) deducte {amount}, and your new balance is: Rs.{self.bal}")

    def credit(self,amount):
        self.bal += amount
        print(f"You added {amount}, and your new balance is: Rs.{self.bal}")

user1=Account(5286,500000)
user1.credit(10000)

