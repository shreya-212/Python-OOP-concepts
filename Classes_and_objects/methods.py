# Concept: Methods in Object-Oriented Programming.
# Methods are functions inside a class that define what an object can DO.

class Beverage:
    def __init__(self,drink_type):
        self.fill_level=100
        self.drink_type=drink_type

    def takeSip(self,siplevel):
        if self.fill_level>=siplevel:
            self.fill_level-=siplevel
            print(f"Took sip of {self.drink_type}, now the cup is {self.fill_level} level full")
        elif self.fill_level>0:
            print(f"Finished the last contents of {self.drink_type}")
            self.fill_level=0
        else:
            print("The cup is completely empty")

    def refill(self):
        self.fill_level=100
        print(f"{self.drink_type} is now full!")

Water_cup=Beverage("Water")


Water_cup.takeSip(50)
Water_cup.takeSip(50) #cup empties 
Water_cup.takeSip(30) #No water

Water_cup.refill()




              

    