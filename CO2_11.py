area_square = lambda side: side * side
area_rectangle = lambda length,width: length * width 
area_triangle = lambda base,height: 0.5 * base * height

side = float(input("enter side of square:"))
print("area of square:",area_square(side))

length = float(input("enter length of rectangle:"))
width = float(input("enter width of rectangle:"))
print("area of rectangle:",area_rectangle(length, width))

base = float(input("enter base of triangle:"))
height = float(input("enter height of triangle:"))
print("area of triangle:",area_triangle(base, height))                                                                  