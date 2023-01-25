#mitratsb
n=int(input())
word1=input()
word2=input()

if len(word1)==len(word2)==n:
    if word1==word2:
        print(0)
    else:
        mistakes=0
        for letter in range(0,n):
            if word1[letter] == word2[letter]:
                pass
            else:
                mistakes=mistakes+1
            total_mistakes=mistakes
        print(total_mistakes)
        

        
    


