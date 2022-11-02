dictionary = {'Иванов': 20, 'Сидоров': 68, 'Петров': 26, 'Смирнов': 68,'Решетников': 78,'Искандеров': 70,'Логиновский': 22}
maximum = max(dictionary.values())
minimum = min(dictionary.values())
medium = sum(dictionary.values())/len(dictionary)

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

