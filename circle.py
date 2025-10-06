class Circle:
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        area=(22/7)* self.rad**2
        return area
    
    def perimeter(self):
        return 2*(22/7)*self.rad
    
c1=Circle(21)
print(c1.area())
print(c1.perimeter())