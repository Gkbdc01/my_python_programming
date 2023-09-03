#calculation of heron's formula for area of triangle .
a = float(input("enter the firt side of triangle : "))
b = float(input("enter the second side of triangle : "))
c = float(input("enter the third side of triangle : "))
s = (a+b+c)/2
area = (s*(s+a)*(s+b)*(s+c))**0.5
print("the area of triangle using heron's formula is :",area)
