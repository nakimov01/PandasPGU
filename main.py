import random

List = [round(random.uniform(-99.999, 100), 2) for x in range(10)]  # Создание списка из 10 элементов случайными числами
Avg__Val = round(sum(List) / 10, 2)  # Среднее значение списка из 10 элементов
print(List)
print(Avg__Val)
List.insert(0, Avg__Val)  # Добавление среднего значения в начало списка
print(List, "\n")

N, M = 5, 5
Matr = [[round(random.uniform(-99.999, 100), 2) for i in range(N)] for j in range(M)]  # Создание матрицы 5x5
for Row in Matr: print(*Row)
