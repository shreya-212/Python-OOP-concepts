#Polymorphism
class Payment:
    def pay(self,amt):
        print(f"Paying {amt}")
class CreditCard(Payment):
    def pay(self,amt):
        print(f"Paying {amt} using Credit card")

class UPI(Payment):
    def pay(self,amt):
        print(f"Paying {amt} using UPI")

def process_payment(payment_method,amt):
    payment_method.pay(amt)

process_payment(CreditCard(),500)
process_payment(UPI(),250)
