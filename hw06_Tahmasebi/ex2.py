# list1=[-3,-5,-4,-7,-5,3,5,7,5,6,8,9,3,5,33,44,55,6]

# list1.sort()
# for i in list1:
#     if list1[0]<1:
#         list1.remove(list1[0])
#     if list1[-1]>30:
#         list1.remove(list1[-1])
# print(list1)

# a=0
# while a<len(list1):
#     if list1[0]<1:
#         list1.remove(list1[0])
#     if list1[-1]>30:
#         list1.remove(list1[-1])
#     a+=1
# print(list1)

# name="ali"
# d={}
# d.update({name:["678767"]})

# d["ali"].append(333333)
# print(d)

# "1400/03/03"="%Y/%m/%d"

from datetime import date,datetime

# print(date(1400,3,2))
# print(list(range(date(1400,3,2),date(1400,3,6))))

start="1400/01/01"
start=start.split("/")
# print(start[2])
length=30
start_day=int(start[2])
days_allowed=[]

a=0
next_day=start
while a<length:
    day=int(next_day[2])
    month=int(next_day[1])
    
    if start_day+length <= 30:
        day+=1
        next_day="1400/"+str(month)+"/"+str(day)
        days_allowed.append(next_day)
        next_day=next_day.split("/")
        a+=1
    else:
        distance=30-start_day
        new_month_days=length-distance
        month+=1
        next_day="1400/"+str(month)+"/"+str(new_month_days)
        
        print(next_day)
        days_allowed.append(next_day)
        next_day=next_day.split("/")
        a+=1
        
print(days_allowed)



# from datetime import datetime

# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%Y-%m-%d")
#     d2 = datetime.strptime(d2, "%Y-%m-%d")
#     return abs((d2 - d1).days)

# print(days_between("1400/01/01","1400/01/11"))



# from datetime import date

# def diff_dates(date1, date2):
#     return abs(date2-date1).days

# def main():
#     d1 = date(2013,1,1)
#     d2 = date(2013,9,13)
#     d3 = date(2013,9,9)
#     print(d3)
    
#     result1 = diff_dates(d2, d1)
#     print (f'{result1} days between {d1} and {d2}')

# main()
