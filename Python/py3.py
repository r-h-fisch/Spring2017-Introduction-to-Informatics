import random
lyricsList= ["chang","chang","chang", "changitty","sha", "bop"]
while lyricsList:
    mysong= random.choice(lyricsList)
    print(mysong)
    lyricsList.remove(mysong)
    
song=0
print("Sha-")
while song<7:
    print("na")
    if song==6:
        print("yippity dip de doom")
        song+=1
    else:
        song+=1

##colorsList= ["black", "brown", "orange", "green", "blue", "purple", "yellow"]
##while colorsList:
##    myColor= random.choice(colorsList)
##    print(myColor)
##    colorsList.remove(myColor)
##    print(colorsList)

##number= 67
##guess=random.randint(1, 10);
##while int(guess) != number:
##    guess= input("Enter another guess")
##    try:
##        if int(guess)>number:
##            print("guess is too high")
##        elif int(guess)<number:
##            print("guess is too low")
##        else:
##            print("You guessed it!")
##    except:
##        print("Not a valid guess")
