from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self,amt):
        pass
    @abstractmethod
    def check_bal(self):
        pass
class The_ATM(ATM):
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f"withdrawn {amt}")
        else:
            print("Insufficient balance")
        
    def check_bal(self):
        print(f"Current balance: {self.balance}")

user1=The_ATM(5000)
user1.check_bal()
user1.withdraw(2000)
user1.check_bal()