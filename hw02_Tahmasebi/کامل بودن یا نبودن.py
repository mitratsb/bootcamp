#mitratsb
n=int(input())

sum1=0
for i in range(1,n):
    if n%i==0:
        b=i
        i=i+1
        sum1=sum1+b
    else:
        i=i+1
    
if n==sum1 :
    print("YES")
else:
    print("NO")

