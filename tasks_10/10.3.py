with open("file 10_3.txt", "r", encoding="utf-8") as f:
    text = list(map(lambda x: tuple(x.split()), f.read().strip().split("\n")))

text.sort(key=lambda x: x[0])

with open("3_result_1.txt", "w") as f:
    print(*list(map(lambda x: " ".join(x), text)), sep="\n", file=f)

text.sort(key=lambda x: x[1], reverse=True)

with open("3_result_2.txt", "w") as f:
    print(*list(map(lambda x: " ".join(x), text)), sep="\n", file=f)

