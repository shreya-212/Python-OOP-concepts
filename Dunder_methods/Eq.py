# Concept: Dunder (Magic) Methods - __eq__
#  The __eq__ method overrides Python's default '==' operator behavior. 
# By default, '==' checks if two objects occupy the same memory space.


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"Product -{self.name} is priced ${self.price}"
    
    def __eq__(self,other):
        return self.name==other.name and self.price==other.price

item1=Product("Pen",2)
item2=Product("Book",10)
item3=Product("Book",10)

print(item2==item3)
print(item1==item2)