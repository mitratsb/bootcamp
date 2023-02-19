#mitratsb
n=int(input())
m=int(input())


sum1=0
for i in range(-10,m+1):
    j=1
    for j in range(1,n+1):
        x=((i+j)**3)/(j**2)
        sum1+=x

print(sum1)