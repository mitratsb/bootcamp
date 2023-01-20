#Mitratsb
# spot1=x1,y1   spot2=x2,y2

from math import sqrt

x1=int(input("x1: "))
y1=int(input("y1: "))

x2=int(input("x2: "))
y2=int(input("y2: "))


# distance = sqrt((x2**2 - x1**2) + (y2**2 - y1**2)) 
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'distance is {distance}cm')

# فرمول کامنت شده اشتباه داده شده بود که فرمول صحیح جایگزین شده است
