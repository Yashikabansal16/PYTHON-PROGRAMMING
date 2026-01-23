# input three sides of triangle
a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

# calculate semi perimeter
s = (a+b+c)/2

# area using Heron's formula
area = (s * (s-a) * (s-b) * (s-c))**0.5

# print result
print("The area of triangle is: ",area)