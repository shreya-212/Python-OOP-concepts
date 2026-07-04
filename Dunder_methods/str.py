# Concept: Dunder (Magic) Methods - __str__
#  Dunder methods are special built-in methods surrounded by double underscores 
# that run automatically in the background. The __str__ method dictates exactly how an 
# object should be represented as a string, making the output readable when you print() the object


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"Product -{self.name} is priced ${self.price}"

item=Product("Book",10)
print(item)