import random

List = [round(random.uniform(-99.999, 100), 2) for x in range(10)]  # Создание списка из 10 элементов случайными числами
Avg__Val = round(sum(List) / 10, 2)  # Среднее значение списка из 10 элементов
print(List)
print(Avg__Val)
List.insert(0, Avg__Val)  # Добавление среднего значения в начало списка
print(List, "\n")

N, M = 5, 5
Matr = [[round(random.uniform(1, 5)) for i in range(N)] for j in range(M)]  # Создание матрицы 5x5

res_sum = 0
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end = ' ')
    print()
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if i == j:
            res_sum += Matr[i][j]
            print(Matr[i][j])
print(res_sum)
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if j == (4-i):
            print(Matr[i][j])
            Matr[i][j] = 0
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end = ' ')
    print()