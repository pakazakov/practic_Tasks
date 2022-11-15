from datetime import datetime

def buble_gum(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print("Введите массив целых чисел:")
arr = list(map(int,input().split()))

print("Исхoдный массив:")
print(arr)

start_1 = datetime.now()
arr_1 = buble_gum(arr)
end_1 = datetime.now()

start_2 = datetime.now()
arr_2 = sorted(arr)
end_2 = datetime.now()

result_1, result_2 = end_1 - start_1, end_2 - start_2

print("Результаты сортировки методом пузырька:")
print("Отсортированный массив:")
print(result_1)
print("Время выполнения сортировки:")
#print(result_1,"\n")

print("")



print()