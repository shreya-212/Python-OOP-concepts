# Concept: Multilevel Inheritance
# A chain where a class inherits from a parent, which inherits from a grandparent.


class Device:
    def __init__(self,brand):
        self.brand=brand
    
    def turn_on(self):
        print(f"The {self.brand} is turning on")

class Computer(Device):
    def __init__(self,brand,ram_size):
        super().__init__(brand)
        self.ram_size=ram_size

    def open_browser(self):
        print(f"Open the browser on {self.brand} with {self.ram_size} of ram size")

class Laptop(Computer):
    def __init__(self,brand,ram_size,weight):
        super().__init__(brand,ram_size)
        self.weight=weight
        
    def fold(self):
        print(f"Fold the {self.brand} device of  {self.weight} and put it in bag")


product=Laptop("Dell",5,"3 lb")

product.turn_on()
product.open_browser()
product.fold()



