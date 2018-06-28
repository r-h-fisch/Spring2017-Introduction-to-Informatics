import random
sentance= "*sen *noun"
startsen= ["Have you seen my", "Where is the", "Look its a", "Don't touch that" ]
noun=["slice of pizza", "car", "hat", "spoon", "balloon"]
sentance= sentance.split()

index = 0
index2 = 0
for word in sentance:
    if word == "*sen":
        newstart = random.choice(startsen)
        sentance[index] = newstart
    index += 1
    if word == "*noun":
        newnoun = random.choice(noun)
        sentance[index2] = newnoun
    index2 += 1
    

st = ""
for word in sentance:
    st += word + " "
print(st)
##Yes, you can do this for more parts of speech
