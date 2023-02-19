#try - except 
 
# while True:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     try:
#         print(a/b)
#     except:
#         pass
#اینجا اگر تقسیم به هر اروری بخوره رد میشه و میره اول حلقه


#ورودی های مختلف میتونیم داشته بتشیم و اگر بخوایم میتونیم بهش مقدار بدیم
# def add(a,b,c=None):
#     if c is None:
#         return a+b
#     else:
#         return (a+b)*c
    
# #tuple unpacking
# a=(3,46,6,4,6,578,8,86,7)
# first_num , *others = a
# first_num , *others = a
# first_num , *others = a

# def func(a,b,/,*args,c=8,v=8,key=5,**kwargs):
#     return [a,b,args,c,v,key,kwargs]

# print(func(2,4,6,7,8,name="mitra",family="tsb"))
 
# from copy import deepcopy
 
# a=[3,5,6,7]
# # b=copy(a)
# b1=a.copy()

# c=deepcopy(a)
# # c1=a.deepcopy()
# print(b1,c)

def my_decorator(my_input):
    pass
    return wrapper

from time import time
time() #در اون لحظه تایم بگیریم
