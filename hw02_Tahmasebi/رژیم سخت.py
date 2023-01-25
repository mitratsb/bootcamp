#mitratsb
tag=input()

if len(tag)==5:
    
    reds=tag.count("R")
    yellows=tag.count("Y")
    greens=tag.count("G")
    
    if reds>=3 or (reds>=2 and yellows>=2) or reds+yellows==5 :
        print("nakhor lite")
    else:
        print("rahat baash")





