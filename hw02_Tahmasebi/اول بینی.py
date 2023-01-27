#mitratsb
a=int(input())
b=int(input())

output=""
n=a+1
while n<b:
    if n==2:
        output+=str(n)+","
    else:
        i=2
        is_prime=True
        while i<n and is_prime:
            if n%i==0:
                is_prime=False
            i+=1
        if is_prime:
            output+=str(n)+","
    n+=1
    
     
print(output[:-1])