


file = open("file_3.txt","r")
arr_M = file.readlines()
file.close()
arr_M = list(map(lambda x: x.split(),arr_M))
file =  open("rez_3.txt","w")
for i in range(len(arr_M[0])):
    for j in range(len(arr_M)):
        file.write(arr_M[j][i] + " ")
    file.write("\n")
file.close()