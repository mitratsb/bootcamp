#mitratsb
n=int(input())
m=int(input())

total=0
for i in range(-10,m+1):
    j=1
    sum1=0
    while j<n+1:
        x=((i+j)**3)/(j**2)
        sum1+=x
        j+=1
    total+=sum1
    
print(total)