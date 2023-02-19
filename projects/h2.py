from random import shuffle,randint,choice

cards={"Heart":["2","3","4","5","6","7","8","9","10","11","12","13","14"],
           "Spade":["2","3","4","5","6","7","8","9","10","11","12","13","14"],
           "Diamond":["2","3","4","5","6","7","8","9","10","11","12","13","14"],
           "Club":["2","3","4","5","6","7","8","9","10","11","12","13","14"]}

cards_list = []
for key,value in cards.items():
    for v in value:
        cards_list.append([key,v])

#پخش 5 کارت قبل حکم
player_hand = []
i=0
while i < 5:

    random_card = cards_list[randint(0,len(cards_list))]
    player_hand.append(random_card)
    cards_list.remove(random_card)
    i+=1
print(player_hand)
print(len(cards_list))

#تعیین حکم
c_Heart=0
c_Spade=0
c_Club=0
c_Diamond=0
for card in player_hand:
    if card[0]=="Heart":
        c_Heart+=1
    elif card[0]=="Spade":
        c_Spade+=1
    elif card[0]=="Club":
        c_Club+=1
    elif card[0]=="Diamond":
        c_Diamond+=1
        
print(c_Heart , c_Spade , c_Club , c_Diamond)



