#mitratsb

list1=[]
a=1
while a<6:
    x=input()
    if ("HAFEZ" in x) or ("MOLANA" in x):
        list1.append(a)
        a+=1
    else:
        a+=1
        
if len(list1)==0:
    print("NOT FOUND!")
else:
    print(*list1)
