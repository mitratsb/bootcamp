from random import randint

class Card:
    nums_dict={"2":2 , "3":3 , "4":4 , "5":5 , "6":6 , "7":7 , "8":8 ,
                "9":9 , "10":10 , "J":11 , "Q":12 , "K":13 , "Ace":14}
    Suits_list=["Heart","Club","Diamond","Spade"]
    is_hokm=True
    r_num=None
    r_suit=None
    
    def __init__(self,suit,num):
        self.suit=suit
        self.num=num
        
    def get_random_card(self):
        random_num=randint(2,14)
        random_suit=randint(0,3)
        for key,value in Card.nums_dict.items():
            if value==random_num:
                a=key
        
        Card.r_num=a
        Card.r_suit=Card.Suits_list[random_suit]
    
        print(Card.r_num,":",Card.r_suit)
        
        

Hokm_card=Card("Heart","7")
card2=Card("Club","J")

Hokm_card.get_random_card()

#اینو خودمون میدیم
# print(card1.suit)
# print(card1.num)

#اینو بازیکن های مجازی
print(Hokm_card.r_num)
# print(card1.r_suit)

#دو کارت رو بگیر اگر اولی بزرگتر بود عددش یه امتیاز به گروه 1 اضافه کن
gp1_wins=0
gp2_wins=0

if Card.nums_dict[Hokm_card.num] > Card.nums_dict[card2.num]:
    gp1_wins += 1
elif Card.nums_dict[Hokm_card.num] < Card.nums_dict[card2.num]:
    gp2_wins += 1
    
print(f'gp1:{gp1_wins} , gp2:{gp2_wins}')

#مرحله اول بازی
#تعیین حاکم

players=["player1","player2","player3","player4"]
for player in players:

    if Hokm_card.r_num=="Ace":
        print(f'Hakem : {player}')
        break
    
#نکته اینه که وقتی رندوم کارت میدی اون کارت رندوم از کل کارت ها کن میشه
# باید دیکشنری زد و رندومه رو ازش کم کرد








# while gp1_wins<=7 or gp2_wins<=7:
#     #start round
#     pass

