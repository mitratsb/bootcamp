k=int(input())

i=1
s=0
is_finished=False

while not is_finished:
    s+=i
    j=1
    counter=0
    while j<=s:
        if s%j==0:
            counter+=1
        j+=1
    
    if counter>=k:
        print(s)
        is_finished=True
    
    i+=1
    
    
        
    


    
    
