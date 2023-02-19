# class Date:
    
#     def __init__(self,year,month,day) -> None:
#         self.year=year
#         self.month=month
#         self.day=day
        
#     def __add__(self,obj):
#         pass
        
        
# date1=Date(1370,1,4)
# date2=Date(1440,3,5)

# date3=Date(10,1,3)
# #میخوایم تاریخ اولی رو با سومی جمع کنیم


class Card:

    _hokm = 0
    _suit2num = {'♥':0,'♦':1,'♣':2,'♠':3}
    _num2suit = {0:'♥',1:'♦',2:'♣',3:'♠'}
    

    def __init__(self,number,suit):
        self.number = number
        self.suit =suit
    
    @classmethod
    def number_to_suit(cls,number):
        return cls._num2suit[number]
    
    @classmethod
    def suit_to_number(cls,suit):
        return cls._suit2num[suit]

    def __gt__(self):
        if isinstance(card1,Card):
            

    def __lt__(self,other):
        pass
    

card1=Card()

