#Mitratsb
a=input('Enter a string: ')
b=int(input('Enter an integer: '))
c=float(input('Enter a float: '))

# d=complex(input('value4: '))
# e=bool(input('value5: '))

# اگر سه مقدار ورودی بگیریم تایپ همه ی آنها رشته است. و نمیتوان رشته را به عدد صحیح یا اعشار تبدیل کرد
# مگر اینکه به کاربر بگوییم چه تایپی وارد کند و خودمان هم تغییر تایپ را به همان تایپ برسانیم
# در این صورت میتوان تایپ های مجزا را در خروجی دید

print(f'value1 is a {type(a)}\nvalue2 is a {type(b)}\nvalue3 is a {type(c)}')
