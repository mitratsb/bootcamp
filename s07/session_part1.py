#تابع بازگشتی و مثالش روی فاکتوریل
# def factoriel(n):
#     if n==0:
#         return 1
#     else:
#         return n*factoriel(n-1)
# print(factoriel(5))

print("---------------------------------")
#دنباله ی فیبوناچی تا فلان عدد رو حساب کن با تابع بازگشتی
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# print(fibo(6))


#مدیریت فایل ها
#باز کردن فایل متنی با مود های مختلف
#
print("---------------------------------")

#r:read w:write a:append
#way1
# file = open("s07\data.txt","r")
# output = file.read()
# print(output)

print("---------------------------------")
#way 2
from pathlib import Path
# data_address= Path("s07\data.txt")
# file=open(data_address, "r")
# output= file.read()
# print(output)
# print(data_address.parent.resolve())
# #ادرس فایل های پوشه پرنت فایل دیتا بود رو میده
# for file1 in data_address.parent.iterdir():
#     # print(file)
#     d=open(file1,"r")
#     print(d.read())
    
print("--------------1-------------------")
data_address=Path("s07\data.txt")
f=open(data_address,"w")
f.write("this is a new text.")


print("---------------2------------------")
data_address=Path("s07\data.txt")
f=open(data_address,"r")
print(f.read())

print("---------------3------------------")
data_address=Path("s07\data.txt")
f=open(data_address,"a")
print(f.append(" append this."))

print("---------------4------------------")
