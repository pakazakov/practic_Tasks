dictionary = {'привет': 'hello',
       'мир': 'world',
       'ты': 'you',
       'я': 'i',
       'сделал': 'made',
       'словарь': 'dictionary',
       'умею': 'can',
       'переводить': 'translate',
       'слова': 'words'}
k = 'х'
print("Хотите пополнить словарь ? \n 1) Да \n 2) Нет")
ans = str(input())
if ans in "1 Да да":
       while not k in "2 нет Нет":
              print("Введите слово на русском:")
              word = str(input())
              print("Введите перевод слова:")
              trans = str(input())
              dictionary[word] = trans
              print("Хотите еще пополнить словарь ?\n 1) Да \n 2)Нет")
              k = str(input())
              print(k)

text = str(input('Введите текст: ')).lower().split()

arr = []
for i in range(len(text)):
       if text[i] in dictionary:
              arr = arr + [dictionary[text[i]]]
       else:
              arr = arr + ["***"]
print(*arr)