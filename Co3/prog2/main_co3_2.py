# Importing individual modules
from graphics import rectangle,circle
from graphics.threedgraphics import cuboid,sphere

print("Rectangle area:",rectangle.area(10,50))
print("Rectangle perimeter:",rectangle.perimeter(13,21))

print("Circle area:",circle.area(7))
print("Circle perimeter:",circle.perimeter(7))

print("Cuboid area:",cuboid.area(2,3,4))
print("Cuboid perimeter:",cuboid.perimeter(2,3,4))

print("Sphere area:",sphere.area(7))
print("Sphere perimeter:",sphere.perimeter(7))