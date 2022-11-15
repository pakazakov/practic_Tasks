
file = open("file_4.txt","r")
text = file.read().strip().split("\n")
file.close()

file = open("rez_4.txt","w")
file.write("Table of contents\n")
for i in range(len(text)):
    one_two = text[i].split()
    if len(one_two) == 2 and one_two[0] == "Chapter" and one_two[1].isdigit() == 1 :
        file.write(text[i]+'.'+text[i+1] + "\n")
file.close()