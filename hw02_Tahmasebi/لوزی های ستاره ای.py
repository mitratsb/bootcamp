#mitratsb
n=int(input())

if n%2==1:
    a=1
    b=n
    while a<=n:
        print((b//2*" " + a*"*" + b//2*" " ) + ( b//2*" " + a*"*" + b//2*" "))
        a=a+2
        b=b-2

    a=n
    b=2
    while 1<=a<=n:
        print((b//2*" " + (a-2)*"*" + b//2*" " ) + ( b//2*" " + (a-2)*"*" + b//2*" "))
        a=a-2
        b=b+2
else:
    None


