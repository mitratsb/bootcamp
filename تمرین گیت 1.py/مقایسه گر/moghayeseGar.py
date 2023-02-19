#mitratsb

def compare(string1,string2):
    list1=[]
    list1.append(string1)
    list1.append(string2)
    list1.sort()
    string1=list1[0]
    string2=list1[1]
    while len(string1)>0 and len(string2)>0:
            if string1[0]==string2[0]:
                string1=string1[1:]
                string2=string2[1:]
            else:
                string1=string1[1:]
            
            string1=string1[::-1]
            string2=string2[::-1]
            
            list2=[string1,string2]
            list2.sort()
            string1=list2[0]
            string2=list2[1]
        
    if len(string1)==0:
        print(string2)
    elif len(string2)==0:
        print(string1)
    elif len(string1)==0 and len(string2)==0:
        print("Both strings are empty!")
    
compare(input(),input())


        
            
            
            
        
