#mitratsb
from operator import itemgetter

unsorted_users_list=[]
find_counter=1

while True:
    command=input().split()
    #unpacking destructure 
    #command,*data=input().split()
    #اینطوری عضو اول توی کامند میفته و بقیه توی بعدی
    #تعداد بیشتر بدون استار هم میتونیم بذاریم که اعضا دونه دونه بره تو اونا
    
    if command[0]=="Add":
        username=command[1]
        gender=command[2]
        age=command[3]
        userid=command[4]
        #username,gender,age,userid=data
        user_dict={"username":username , "gender":gender , "age":age , "userid":userid}
        unsorted_users_list.append(user_dict)
        users_list = sorted(unsorted_users_list, key=itemgetter('userid')) 
        print(f'User {userid} added successfully')

    elif command[0]=="Find":
        current_id=command[1]
        len_current_id=len(current_id)
        have_result=False
        for dict1 in users_list:
            g=0
            # if current_id[0:len_current_id]==dict1["userid"][0:len_current_id]:
            if dict1["userid"].startswith(current_id):
                print(find_counter,*dict1.values())
                g+=1
                have_result=True
                
            if g==10:
                break
        if have_result==True:
            find_counter+=1
        else:
            print(find_counter,"No user found")
            find_counter+=1
                             





    
    
