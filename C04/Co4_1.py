class rectangle:
    def __init__(self,lenth,breadth):
       self.length=lenth
       self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

rectangle1=rectangle(4,5)
rectangle2=rectangle(6,7)

print("Area of first rectangle=",rectangle1.area())
print("Area of second rectangle=",rectangle2.area())

print("Perimeter of first rectangle=",rectangle1.perimeter())
print("Perimeter of second rectangle=",rectangle2.perimeter())