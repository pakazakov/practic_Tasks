import re
file = open("test.txt",'r',encoding="utf-8")
maxi = c =0
list = list()
b = []
arr = file.read()
arr = arr.split("\n")
for i in range(len(arr)):
    arr[i]= arr[i].split(", ")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        b.append(arr[i][j])
b.sort(key = lambda x: x[1] )
print(*b)