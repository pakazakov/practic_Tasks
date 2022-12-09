s = list(str(input()))
steck = list()
while len(s) != 0:
    steck.append(s.pop(0))
while len(steck) != 0:
    s.append(steck.pop())
print(''.join(s))