#mitratsb
from math import sqrt
  
n=int(input())

list1=[]

while n % 2 == 0: 
    list1.append(2)
    n = n / 2

for i in range(3, int(sqrt(n))+1, 2):
    while n % i== 0:
        list1.append(i)
        n = n / i 
        
if n > 2:
    list1.append(n)
   
list1.sort()  
# print(list1)

list2=[]

for x in list1:
    if x not in list2:
        list2.append(x)

# print(list2)

res1=""
for y in list2:
    if list1.count(y)==1:
        res=str(y)+"*"
        
    else:
        res=str(y)+"^"+str(list1.count(y))+"*"
    res1=res1+res
    
print(res1[:-1])


