word = list(str(input()))
steck = []
bob = 1
if len(word)%2 == 0:
    a  = len(word)//2
    while(a  != len(steck)):
        steck.append(word.pop(0))
    while(len(steck) != 0):
        if steck.pop() != word.pop(0):
            print("Не полиндром")
            bob = 0
            exit()

elif len(word)%2 != 0:
    a = (len(word)-1)//2
    while(a != len(steck)):
        steck.append(word.pop(0))
    word = word[1:]
    while(len(steck) != 0):
        if steck.pop() != word.pop(0):
            print("Не полиндром")
            bob = 0
            exit()
if bob == 1:
    print("Полиндром")