#mitratsb

a=int(input())
b=int(input())
c=int(input())

list1=[a,b,c]
list1.sort()
a1=list1[0]
b1=list1[1]
c1=list1[2]

if (a1**2)+(b1**2)==(c1**2):
    print("YES")
else:
    print("NO")

