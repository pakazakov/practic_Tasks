dictionary = {'Ивановa': 20, 'Сидоровa': 68, 'Петровa': 67, 'Джигорханян': 68,'Решетниковa': 78,'Искандеров': 70,'Логиновский': 22}
print("Хотите добавить данные ? \n 1) Да \n 2) Нет")
k = input()
if k in "1 да Да ":
    while not k in "нет Нет 1":
        print("Введите фамилию учащегося:")
        key =str(input())
        print("Введите колличество баллов учащегося:")
        val = int(input())
        dictionary[key] = val
        print("Хотите еще добавить данные ? \n 1) Да \n 2) Нет")
        k = (input())

minimum = min(dictionary.values())
medium = sum(dictionary.values())/len(dictionary)
maximum = max(dictionary.values())
print(f"\nУчастники, балл которых выше среднего ({medium} - средний балл):")

for key, val in dictionary.items():
    if val > medium:
        print(key)

print(f"\nУчастники, которые получили максимальный балл ({maximum} - максимальный балл):")
for key, val in dictionary.items():
    if val == maximum:
        print(f"{key}: {val}")

print(f"\nУчастники, которые получили минимальный балл ({minimum} - минимальныйй балл):")
for key, val in dictionary.items():
    if val == minimum:
        print(f"{key}: {val}")

