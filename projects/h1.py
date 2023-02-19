from random import randint,choice

class Player:
    our_side=False
    opp_side=False
    our_score=0
    opp_score=0
    is_hakem=False
    
    def __init__(self,num):
        self.num=num
        
    def give_team_score(self):
        #اگر بازیکن اول یا سوم برد یه امتیاز بریز تو متغیر امتیاز
        #ایف باید شرطش جزئی تر بشه
        if self.num==1 or self.num==3 :
            our_side=True
        
        elif self.num==2 or self.num==4 :
            opp_side=True
            
        if our_side:
            our_score+=1
            
        if opp_side:
            opp_score+=1
            


Zahra= Player(2)



class Game:
    j,Q,K,Ace=11,12,13,14
    cards={"Heart":["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"],
           "Spade":["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"],
           "Diamond":["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"],
           "Club":["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]}
    suits=["Heart","Spade","Diamond","Club"]
    nums=["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]
    
    
    @classmethod
    def level_0(cls):
        #تعیین حاکم
        player=1
        while True:
            if player==5:
                player=1
                
            random_num=choice(Game.nums)
            random_suit=choice(Game.suits)
            random_card=[random_num,random_suit]
            
            if random_card[0]=="Ace":
                if player==1:
                    print('You are Hakem.')
                    break
                elif player==2:
                    print("player2 is Hakem.")
                    break
                elif player==3:
                    print("player 3 (your partner) is Hakem.")
                    break
                elif player==4:
                    print("player4 is Hakem.")
                    break
            else:
                # Game.nums.remove(random_card[0])
                player+=1
            
            
        pass
    
    def level_1(self):
        #پخش کارت به هر نفر 5 تا
        pass
    
    def level_2(self):
        #تعیین حکم
        pass
    
    def level_3(self):
        #پخش بقیه کارت ها. به هر نفر 8 تا
        pass
    
    def level_4(self):
        #شروع راند 1
        pass
    

#ابجکت دهی
a1=Game()

#فراخوانی ها
a1.level_0()
