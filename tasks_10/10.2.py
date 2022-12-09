def buble_gum(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1].count("а") < arr[j].count("а"):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

file = open("file 10_2.txt","r", encoding="utf-8")
str_s = list(map(lambda x: x.strip("\n"),file.readlines()))
file.close()
str_s = list(reversed(buble_gum(str_s)))
file = open("rez 10_2.txt","w", encoding="utf-8")
for i in range(len(str_s)):
    file.write(str_s[i]+ "\n")
file.close()