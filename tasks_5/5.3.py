from random import *

n = 1
s = randint(4,30)
print(f"Начало, у вас {s} камней")
while s>0:
    n+=1
    k = int(input())
    while k>3 or k<1:
        print("Вы ввели неверное количество камней\n")
        k = int(input('Попробуйте ещё разочек: '))
    s-=k
    if s <= 1:
        print("Вы победили, позравляю!!!")
        break
    print(f"Осталось {s} камней")
    m = randint(1,3)
    if s <= 4:
        print("К сожалению вы проиграли")
        break
    else:
        s-=m
        print(f'Бот убрал {m} камней\n Осталось {s}')