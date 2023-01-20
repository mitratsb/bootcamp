#Mitratsb
a=int(input('Enter number a : '))
b=int(input('Enter number b : '))

#1
print("----Arithmetic Operators----")
x1=a+b
x2=a-b
x3=a*b
x4=a/b
x5=a%b
x6=a**b
print(f'{a}+{b}={x1} , {a}-{b}={x2} , {a}*{b}={x3} , {a}/{b}={x4} , {a}%{b}={x5} , {a}**{b}={x6}\n')
#باید محاسبات ریاضی را به عدد صحیح تبدیل کنیم که در قسمت های بعدی بتوان تغییر مبنا داد
r1=int(x1)
r2=int(x2)
r3=int(x3)
r4=int(x4)
r5=int(x5)
r6=int(x6)


#2
print("----Logical and Bitwise Operators----")
f1=a and b
f2=a or b
f3=a & b
f4=a | b
f5=a ^ b
print(f'{a} and {b} ={f1} , {a} or {b} ={f2} , {a} & {b} ={f3} , {a} | {b} ={f4} , {a} ^ {b} ={f5}\n')

#3
print("----Binary Forms----")
g1=bin(a)
g2=bin(b)
g3=bin(r1)
g4=bin(r2)
g5=bin(r3)
g6=bin(r4)
g7=bin(r5)
g8=bin(r6)
print(f'1){a} = {g1} \n2){b} = {g2} \n3){g1} + {g2} = {g3} \n4){g1} - {g2} = {g4}')
print(f'5){g1} * {g2} = {g5} \n6){g1} / {g2} = {g6} \n7){g1} % {g2} = {g7} \n8){g1} ** {g2} = {g8}\n')

#4
print("----Octal Forms----")
k1=oct(a)
k2=oct(b)
k3=oct(r1)
k4=oct(r2)
k5=oct(r3)
k6=oct(r4)
k7=oct(r5)
k8=oct(r6)
print(f'1){a} = {k1} \n2){b} = {k2} \n3){k1} + {k2} = {k3} \n4){k1} - {k2} = {k4}')
print(f'5){k1} * {k2} = {k5} \n6){k1} / {k2} = {k6} \n7){k1} % {k2} = {k7} \n8){k1} ** {k2} = {k8}\n')

#5
print("----Hexadecimal Forms----")
s1=hex(a)
s2=hex(b)
s3=hex(r1)
s4=hex(r2)
s5=hex(r3)
s6=hex(r4)
s7=hex(r5)
s8=hex(r6)
print(f'1){a} = {s1} \n2){b} = {s2} \n3){s1} + {s2} = {s3} \n4){s1} - {s2} = {s4}')
print(f'5){s1} * {s2} = {s5} \n6){s1} / {s2} = {s6} \n7){s1} % {s2} = {s7} \n8){s1} ** {s2} = {s8}\n')

