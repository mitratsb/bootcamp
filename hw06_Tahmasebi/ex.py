# import time
 
# print(time.strftime('%Y%m%d'))

from datetime import date,datetime

# d =date(2022,10,12)
# print(d)   

my_date="1400/01/04"
d = datetime.strptime(my_date, "%Y/%m/%d")
day = int(d.strftime('%d'))
print(day) 
print(type(day))

print("-------------")

list_all_odds=[]
a=0
for month in range(1,13):
    list_odd=[]
    while a<30:
        a+=2
        list_odd.append(a)
        a+=2
        list_odd.append(a)
        a+=2
        list_odd.append(a)
        a+=1
    a+=2
    list_odd.append(a)
    a=-(month*2)
    list_odd.sort()
    for i in list_odd:
        if list_odd[0]<1:
            list_odd.remove(list_odd[0])
        if list_odd[-1]>30:
            list_odd.remove(list_odd[-1])
    list_all_odds.append(list_odd)


print("---------------n--------------")

list_all_evens=[]
b=0
for month in range(1,13):
    list_even=[]
    while b<30:
        b+=1
        list_even.append(b)
        b+=2
        list_even.append(b)
        b+=2
        list_even.append(b)
        b+=2
    b+=2
    list_even.append(b)
    b=-(month*2) 
    list_even.sort()
    for i in list_even:
        if list_even[0]<1:
            list_even.remove(list_even[0])
        if list_even[-1]>30:
            list_even.remove(list_even[-1])
    list_all_evens.append(list_even)
    
timestamp="1400/01/07"
d = datetime.strptime(timestamp, "%Y/%m/%d")
day = int(d.strftime('%d'))
month = int(d.strftime('%m'))

if day in list_all_odds[month-1]:
    print("yes")