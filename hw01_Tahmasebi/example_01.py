#Mitratsb
from math import sqrt

a=float(input("a : "))
b=float(input("b : "))
c=float(input("c : "))

p1= (a+b+c)
p2 = (a+b+c)/2
s = sqrt(p2*(p2-a)*(p2-b)*(p2-c))

print(f'perimeter is : {p1}')
print(f'surveying is : {s}')

