import time
from random import randint

def buble_gum(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

arr = [randint(1, 100) for i in range(5000)]

print("Исхoдный массив:")
print(arr)

start_1 = time.time()
arr_1 = buble_gum(arr)
end_1 = time.time()

start_2 = time.time()
arr_2 = sorted(arr)
end_2 = time.time()

result_1, result_2 = end_1 - start_1, end_2 - start_2

print("Результаты сортировки методом пузырька:")
print("Отсортированный массив:")
print(arr_1)
print("Время выполнения сортировки:")
print(result_1,"sec")
print("Результаты сортировки встроенной функцией:")
print("Отсортированный массив:")
print(arr_2)
print("Время выполнения сортировки:")
print(result_2,"sec")