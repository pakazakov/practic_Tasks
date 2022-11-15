
def check(arr):
    for i in range(len(vect)):
        try:
            int(vect[i])
        except:
            print("Данные введены неверно !!!")
            return 0

def check_num(arr,num):
    if num > len(arr):
        print("Значение n больше числового вектора")
        return 0
    elif num < 0:
        print("Необходимо положительное значение ")
        return 0
def delite(arr,num):
    while num != 0:
        arr.pop(-1)
        num -= 1
    return arr

def made_string(arr):
    string = ''
    for i in range(len(arr)):
        string += str(arr[i]) + ','
    string = "{" + string[:-1:] + "}"
    return string

file = open("file_1.txt","r")
vect = file.readline().strip("{}").split(",")
file.close()

if check(vect) == 0:
    exit()
n = int(input("Введите n: "))
if check_num(vect,n) == 0:
    exit()
new_vect = delite(vect, n)
file = open("rez_1.txt","w")
file.write(made_string(new_vect))
file.close()




