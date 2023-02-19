#mitratsb
from operator import itemgetter

unsorted_users_list=[]
find_counter=1
    
for n in range(100000):
    try:
            
        command=input().split()
        #unpacking destructure 
        #command,*data=input().split()
        #اینطوری عضو اول توی کامند میفته و بقیه توی بعدی
        #تعداد بیشتر بدون استار هم میتونیم بذاریم که اعضا دونه دونه بره تو اونا
        
        if command[0]=="Add":
            username=command[1]
            gender=command[2]
            age=command[3]
            id=command[4]
            #username,gender,age,userid=data
            user_list=[username,gender,age,id]
            unsorted_users_list.append(user_list)
            users_list = sorted(unsorted_users_list, key=lambda x:x[-1]) 
            print(users_list)
            print(f'User {id} added successfully')
            
    
        elif command[0]=="Find":
            input_id=command[1]
            # len_current_id=len(current_id)
            # have_result=False
            # for dict1 in users_list:
            #     g=0
            #     # if current_id[0:len_current_id]==dict1["userid"][0:len_current_id]:
            #     if dict1["userid"].startswith(current_id):
            #         print(find_counter,*dict1.values())
            #         g+=1
            #         have_result=True
                    
            res_names1=list(filter(lambda i: i[-1].startswith(input_id) ,users_list))
            res_names2=sorted(res_names1 , key=lambda x: x[-1])[:10]
            #الان ده تا اسم اول رو میده
            
            
            if res_names2==0:
                print(find_counter,"No user found")
                find_counter+=1
            else:
                for i in res_names2:
                    print(find_counter , i[0],i[1],i[2],i[3])
                    find_counter+=1
    
    except:
        break
            
            # if g==10:
            #     break
            # if have_result==True:
            #     find_counter+=1
            # else:
            #     print(find_counter,"No user found")
            #     find_counter+=1
                                    
    
    
    
    
    
        
        
    