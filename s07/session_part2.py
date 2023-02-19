#دیتای هر خط رو بخون و جدا کن و بریز توی یه لیست
with open("s07\data2.txt","r") as f:
    f1=f.read()
    list_of_lines=f1.split("\n")
    id,name,age=list_of_lines[0].split(",")
    
    for line in list_of_lines[1:]:
        words_in_line=line.split(",")
        print(words_in_line)

import sys
i=100_000_000
b=range(i)
print(sys.getsizeof(b))

