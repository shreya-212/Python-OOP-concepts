class Bank:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
    
    def deposit(self,amt):
        self.balance+=amt
        print(f"Amount {amt} has  added to account{self.accno} ")

    def withdraw(self,amt):
        self.balance-=amt
        print(f"Amount {amt} has been withdrawn from {self.accno} ")

    def show_bal(self):
        print(f"your balance is {self.balance}")

b=Bank(100,10000)
b.deposit(500)
b.withdraw(500)
b.show_bal()

c=Bank(200,100)
c.deposit(20)
c.withdraw(10)
c.show_bal()