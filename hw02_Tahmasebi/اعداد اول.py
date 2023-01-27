#mitratsb
a=int(input())
b=int(input())

# for i in range(a,b+1):
#     if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%9==0 or i%11==0 or i%13==0 or i%17==0 or i%19==0 or i%23==0 or i%29==0 or i==1:
#         pass
#     else:
#         print(i)
#     if i==2 or i==3 or i==5 or i==7:
#         print(i)

a=int(input())
b=int(input())

if a==1:
    a=2
n=a
while n<=b:
    if n==2:
        print(n)
    else:
        i=2
        is_prime=True
        while i<n and is_prime:
            if n%i==0:
                is_prime=False
            i+=1
        if is_prime:
            print(n)
    n+=1
    
     
# a=int(input())
# b=int(input())

# if a==1:
#     a=2
    
# n=a
# while n<b:
#     if n==2:
#         print(n)
#     else:
        
#         i=2
#         while i<n:
#             if n%i==0:
#                 print(n)
#             break
            
#         i=+1
#     n+=1
        

    
        
    

        
