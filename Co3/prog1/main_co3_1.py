from prog1.math_1 import rect
from prog1.math_1.advanced import triangle
from prog1.math_1 import arithmetic

print("ARITHMETIC OPERATION \n")
print("Sum : ",arithmetic.add(10,20))
print("Difference : ",arithmetic.diff(100,20))
print("Multiplication : ",arithmetic.multi(10,20))
print("Division : ",arithmetic.division(100,20))

print("\n RECTANGLE \n")

print("Area of Rectangle : ",rect.area(10,20))
print("perimeter of Rectangle : ",rect.peri(10,20))

print("\n TRIANGLE \n")

print("Area of triangle : ",triangle.area(10,20))
print("Perimeter of triangle : ",triangle.peri(10,20,10))

