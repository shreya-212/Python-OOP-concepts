class Bank:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
    
    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
            print(f"Amount {amt} has  been deposited to account{self.accno} ")
        else:
            print("Deposit amt must be positive")
        

    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f"Amount {amt} has been withdrawn from {self.accno} ")
        else:
            print("Insufficient balance")

    def show_bal(self):
        print(f"your balance is {self.balance}")

b=Bank(100,10000)
b.deposit(500)
b.withdraw(500)
b.show_bal()

c=Bank(200,2200)
c.deposit(400)
c.withdraw(200)
c.show_bal()
