#mitratsb
n=int(input())

if 1<=n<=20:
    a=1
    sum1=0
    for number in range(1,n+1):
        if 1<=number<=100:
            
            number=int(input())
            sum1=sum1+number
    
    print(sum1)
