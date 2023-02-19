#mitratsb
from datetime import date,datetime

Users_list=[]
Car_plates_list=[]
user_car_dict={}
car_license_dict={}
user_account_dict={}
car_penalty_dict={}
penalty=0
account=0

list_all_odds=[]
a=0
for month in range(1,13):
    list_odd=[]
    while a<30:
        a+=2
        list_odd.append(a)
        a+=2
        list_odd.append(a)
        a+=2
        list_odd.append(a)
        a+=1
    a+=2
    list_odd.append(a)
    a=-(month*2)
    list_odd.sort()
    for i in list_odd:
        if list_odd[0]<1:
            list_odd.remove(list_odd[0])
        if list_odd[-1]>30:
            list_odd.remove(list_odd[-1])
    list_all_odds.append(list_odd)


list_all_evens=[]
b=0
for month in range(1,13):
    list_even=[]
    while b<30:
        b+=1
        list_even.append(b)
        b+=2
        list_even.append(b)
        b+=2
        list_even.append(b)
        b+=2
    b+=2
    list_even.append(b)
    b=-(month*2) 
    list_even.sort()
    for i in list_even:
        if list_even[0]<1:
            list_even.remove(list_even[0])
        if list_even[-1]>30:
            list_even.remove(list_even[-1])
    list_all_evens.append(list_even)
    
    
    
def Register():
    username=command[1]
    if username in Users_list:
        print("INVALID USERNAME")
    else:
        Users_list.append(username)
        user_account_dict.update({username:account})
        
        print("REGISTER DONE")


def Register_car():
    username=command[1]
    car_plate=command[2]
    
    if username not in Users_list:
        print("INVALID USERNAME")
        
    if car_plate in Car_plates_list:
        print("INVALID CAR PLATE")
        
    if username in Users_list and car_plate not in Car_plates_list:
        print("REGISTER CAR DONE")
        Car_plates_list.append(car_plate)
        if username not in user_car_dict.keys():
            user_car_dict.update({username:[car_plate]})
        else:
            user_car_dict[username].append(car_plate)
        car_penalty_dict.update({car_plate:penalty})

def New_record():
    car_plate=command[1]
    timestamp=command[2]
    d = datetime.strptime(timestamp, "%Y/%m/%d")
    day = int(d.strftime('%d'))
    month = int(d.strftime('%m'))
    
    if car_plate not in Car_plates_list:
        print("INVALID CAR PLATE")
    elif (((day in list_all_odds[month-1]) and (int(car_plate)%2==0)) or ((day in list_all_evens[month-1]) and (int(car_plate)%2==1))) and (day not in car_license_dict.values()):
        print("PENALTY RECORDED")
        # global penalty
        # penalty+=100
        car_penalty_dict[car_plate]+=100
    else:
        print("NORMAL RECORDED")


def Buy_license():
    username=command[1]
    car_plate=command[2]
    length=int(command[3])
    timestamp=command[4]
    d = datetime.strptime(timestamp, "%Y/%m/%d")
    day = int(d.strftime('%d'))
    
    if username not in Users_list:
        print("INVALID USERNAME")
    if car_plate not in user_car_dict[username]:
        print("INVALID CAR PLATE")
    global account
    if length*70 > user_account_dict[username]:
        print("NO ENOUGH MONEY")
    else:
        user_account_dict[username] -= length*70
        days_allowed=list(range(day+1 , day+length+1))
        #if 
        car_license_dict.update({car_plate:[days_allowed]})
        print("BUY LICENSE DONE")
        


def Add_balance():
    username=command[1]
    amount=int(command[2])
    
    if username not in Users_list:
        print("INVALID USERNAME")
    else:
        user_account_dict[username] += amount
        print("ADD BALANCE DONE")


def Get_balance():
    username=command[1]
    if username not in Users_list:
        print("INVALID USERNAME")
    else:
        print(user_account_dict[username])
 
 

def Get_penalty():
    username=command[1]
    if username not in Users_list:
        print("INVALID USERNAME")
    else:
        for car_plate in user_car_dict[username]:
        # car_plate=user_car_dict[username]
            if car_plate in car_penalty_dict.keys():
                if car_penalty_dict[car_plate]>0:
                    print(car_penalty_dict[car_plate])



def Get_license_deadline():
    car_plate=command[1]
    timestamp=command[2]
    d = datetime.strptime(timestamp, "%Y/%m/%d")
    day = int(d.strftime('%d'))
    if car_plate not in Car_plates_list:
        print("INVALID CAR PLATE")
    else:
        if car_plate in car_license_dict.keys():
            last_day=car_license_dict[car_plate[-1]]
            d = datetime.strptime(last_day, "%Y/%m/%d")
            day = int(d.strftime('%d'))
            day+=1
            if len(str(day))==1:
                deadline=last_day[0:8]+"0"+str(day)
                print(deadline)
            else:
                deadline=last_day[0:8]+str(day)
                print(deadline)
                
        else:
            day+=1
            if len(str(day))==1:
                deadline_tomorrow=timestamp[0:8]+"0"+str(day)
                print(deadline_tomorrow)
            else:
                deadline_tomorrow=timestamp[0:8]+str(day)
                print(deadline_tomorrow)
        
        
        


#------------------------------------------

while True:
    command=input().split()

    if command[0]=="REGISTER":
        Register()
    elif command[0]=="REGISTER_CAR":
        Register_car()
    elif command[0]=="NEW_RECORD":
        New_record()
    elif command[0]=="BUY_LICENSE":
        Buy_license()
    elif command[0]=="ADD_BALANCE":
        Add_balance()
    elif command[0]=="GET_BALANCE":
        Get_balance()
    elif command[0]=="GET_PENALTY":
        Get_penalty()
    elif command[0]=="GET_LICENSE_DEADLINE":
        Get_license_deadline()
    elif command[0]=="END":
        break
    
        
