# Concept: Abstraction
# Abstraction hides the complex background details and shows only the essentials. Using Abstract Base Classes (ABC),
# we create a strict blueprint that forces any child class to implement specific methods (using @abstractmethod), while preventing 
# anyone from creating an object directly from the incomplete parent blueprint.

from abc import ABC,abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self,amount):
        print(f"Processing credit card transfer of ${amount}")

class PaypalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing paypal transfer of ${amount}")

#TypeError
# brokenPayment=PaymentProcessor()
# brokenPayment.process_payment()

Credit=CreditCardPayment()
Credit.process_payment(50)

paypal=PaypalPayment()
paypal.process_payment(100)
        


