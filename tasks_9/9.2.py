def split_strings(_str_):
    arr = []
    s = ''
    for i in range(len(_str_)):
        s += _str_[i]
        if _str_[i] in ".!?":
            arr += [s]

            s =''
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr

def gluing_sentences(str_s):
    s = ""
    arr = []
    for i in range(len(str_s)):
        for j in range(len(str_s[i])):
            s += ' '+str(str_s[i][j])
        arr += [s]
        s = ''
    return(arr)
file = open("file_3.txt")
sentences = file.read()
file.close()

num = int(input("Введите n:"))
sentences = gluing_sentences(list(filter(lambda x: len(x) > num, split_strings(sentences))))

file = open("rez_2.txt","w")
for i in range(len(sentences)):
    file.write(str(sentences[i])+"\n")