#mitratsb
from math import floor

nums=input().split()

n=int(nums[0])
k=int(nums[1])

a=1
res=n
while a<k+1:
    res=res/2
    a+=1
    
print(floor(res))

