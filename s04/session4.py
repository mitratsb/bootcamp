#list
# list1=["mohamad","sara",44,True,8.9]
# print(list1[0:2:1])

# my_family=["alireza","mansoure","mohammad","mahdi"]
# #show list variables with for and while
# for i in my_family:
#     print(i)
    
# a=0
# while a<len(my_family):
#     print(my_family[a])
#     a+=1

#size of
# import sys
# print(sys.getsizeof(my_family))


# #sum of 1 to 100
# sum1=0
# for i in range(0,101):
#     sum1+=i
# print(sum1)


# #factoriel of an input number
# n=int(input())
# sum1=1
# for i in range(1,n+1):
#     sum1*=i
# print(sum1)

# #عدد ورودی چند رقمی بگیرید و اعدادش رو جمع کنید
# sum2=0
# m=input()
# for i in m:
#     j=int(i)
#     sum2+=j
    
# print(sum2)

# l=[1,2,3,"mitra",70]
# l.append("reza")
# print(l)

# l.remove("reza")
# print(l)

# l.pop()
# print(l)

# a=l.pop()
# print(a)

# l.pop(1)
# print(l)

# l.insert(0,"mum")
# print(l)

#کاربر بتواند تعدادی اسامی را در دفترچه تلفن لیستی مشخص کند
#با حلقه ی فور نمیشه چون تعداد مشخصی وروئی نداریم و نمیتونیم محدوده ذو مشخص کنیم

# for a in list1: no no no
#     a=input("what's the name? : ")
#     if a=="exit":
#         break
#     else:
#         list1.append(i)
# print(list1)

# #way1
# list1=[]
# is_finished=False
# while not is_finished:
#     name=input()
#     if name != "exit":
#         list1.append(name)
#     else: 
#         is_finished=True
#         print(list1)
        
# #way2 with break
# list2=[]
# while True:
#     name=input()
#     if name=="exit":
#         print(name)
#         break
#     else:
#         list2.append(name)
# else:
#     print("loop else")

# #tuple and set
# tuple1=(1,2,3)

# set1={1,2,3}

#کاربر به تعداد دلخواه اسم و شماره تلفن اضافه کنه و با اگزیت خارج بشه

# phonebook={}

# while True:
#     a=input("name : ")
#     if a!="exit":
#         b=input("phone number : ")
#         phonebook.update({a:b})
#     else:
#         break
    
# for key,value in phonebook.items():
#     print(key,":",value)
    
#قابلیت اضافه و جستجو و حذف و نمایش به دفترچه تلفن بده
phonebook={}
while True:
    command = input("Enter your command(add/remove/search/show/exit) : ")
    if command=="add":
        name=input("Enter name : ")
        phone_number=input(f"Enter {name}'s phone number : ")
        phonebook.update({name:phone_number})
        print(f"{name} was added.")
    elif command=="remove":
        name=input("who do you want to remove? : ")
        phonebook.pop(name)
        print(f'{name} was removed.')
    elif command=="search":
        name=input("Enter a name to search : ")
        print(name,":",phonebook[name])
    elif command=="show":
        if len(phonebook)==0:
            print("phone book is empty")
        else:
            for key,value in phonebook.items():
                print(key,":",value)
    elif command=="exit":
        break
    

        
        
    
    

    
