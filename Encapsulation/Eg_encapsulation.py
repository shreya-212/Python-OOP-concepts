# Concept: Encapsulation
#  Encapsulation is the practice of hiding an object's internal data and restricting direct access. By using double 
# underscores , we make attributes private. The data can then only be viewed or modified safely 
# through public methods (like check_balance or add_funds), which act as security checkpoints

class DigitalWallet:
    def __init__(self,username,pin):
        self.username=username
        self.__pin=pin
        self.__balance=0
    
    def check_balance(self,entered_pin):
        if entered_pin==self.__pin:
            print(f"Access Granted. Current balance: ${self.__balance}")
        else:
            print("Incorrect PIN. Access Denied.")
    def add_funds(self,amt):
        if amt>0:
            self.__balance+=amt
            print(f"Deposited ${amt}")
       
mywallet=DigitalWallet("Sam",1234)
mywallet.check_balance(1234)
mywallet.add_funds(100)
mywallet.check_balance(1234)
mywallet.check_balance(1220)

