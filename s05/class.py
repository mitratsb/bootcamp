
# def add(a,b,c=None):
#     if c is None:
#         return a+b
#     else:
#         return (a+b)*c


# def sample_def(*arg,**kwarg):
#     print(type(arg))
#     print(type(kwarg))
#     print(f"a:{a}")
#     print(f"arg:{arg}")
#     print(f"kwarg:{kwarg}")
#     if len(arg)==1:
#         a = arg[0]
#         return a**2
#     elif len(arg)==2:
#         a,b = arg
#         return a**2,b**2 
#     elif len(arg)>2:
#         raise Exception("sample_def can run with <=2 argument")


# a,b = sample_def(1,2)

# pa = [2,3,4]
# kwa = {'age':20,'gender':'male'}

# sample_def(10,*pa,name="mohammad")
# sample_def(10,2,3,4,name="mohammad")
# sample_def(*pa,**kwa)


# def add(a,b):
#      return a+b
# def add(a,b,c):
#      return (a+b)*c

# print(add(1,2))
# print(add(1,2,3))

# def def1(x):
#     x = *x,10
#     # x.append(10)
#     print(id(x))
#     # x.append(10)
#     # print(x)

# def def2(x):
#     x+=1
#     print(id(x))

# from copy import deepcopy
# a = [2,[3,3]]
# c = a.copy()
# c[1][1]=0
# c[1]=0
# b = 2
# print(f"a: {id(a)}")
# print(f"b: {id(b)}")
# def1(a)
# def2(b)



import time
from time import (time,sleep)
from time import *


# def loop():
#     x=0
#     for i in range(1,1000000):
#         x += 1/i
#     print(x)

# def loop2():
#     x=0
#     for i in range(1,1000000):
#         x += 1/(i**0.5)
#     print(x)

# start_time = time()
# loop()
# end_time = time()
# print(end_time-start_time)

# start_time = time()
# loop2()
# end_time = time()
# print(end_time-start_time)



def time_decorator(f):
    def wrapper():
        start_time = time()
        f()
        end_time = time()
        print(end_time-start_time)
    return wrapper

@time_decorator
def loop():
    x=0
    for i in range(1,1000000):
        x += 1/i
    print(x)

# loop = time_decorator(loop)
# loop()
# loop2 = time_decorator(loop2)

loop()
