import random
from collections import Counter

List = [round(random.uniform(-99.999, 100), 2) for x in range(10)]  # Создание списка из 10 элементов случайными числами
Avg__Val = round(sum(List) / 10, 2)  # Среднее значение списка из 10 элементов
print("Список:", List, '\n', "Среднее значение списка: ", Avg__Val)
List.insert(0, Avg__Val)  # Добавление среднего значения в начало списка
print("Добавление среднего значения в начало списка: ", List, "\n")

N, M = 5, 5
print('______________________________________________________________________________')
Matr = [[round(random.uniform(-100, 100)) for i in range(N)] for j in range(M)]  # Создание матрицы 5x5

res_sum = 0
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end=' ')
    print()
print('______________________________________________________________________________', '\n')
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        res_sum += Matr[i][j]
print("Сумма элементов матрицы: ", round((res_sum), 2), "\n")

for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if i == j:
            res_sum += Matr[i][j]
            print(Matr[i][j])
print('\n', "Среднее значение: ", round((res_sum / 5), 2), "\n")

for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if j == (len(Matr[i]) - i - 1):
            print(Matr[i][j])
            if Matr[i][j] < 0:
                Matr[i][j] = 0
print()
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end=' ')
    print()
print('______________________________________________________________________________', '\n')
MyDict = {'5702-323241': 'Портнов И.П.', '5702-434451': 'Светлов К.И.', '5702-432441': 'Акимов Н.М.',
          '5702-430141': 'Акимов Н.М.', '5702-439901': 'Медведев Д.С.',
          input("Введите паспорт: \n"): input("Введите фамилию с инициалами: \n")}
print(MyDict,'\n')

passport = str(input("Введите паспорт который хотите изменить: "))
if passport in MyDict:
    MyDict[passport] = input("Изменить ФИО на: ")
else:
    print('Паспорт не найден')
print(MyDict)

print('______________________________________________________________________________', '\n')
print('Есть ли полные совпадения в списке всех владельцев паспортов: ', '\n')

List_of_names = []
for value in MyDict.values():
    List_of_names.append(value)

for x in List_of_names:
    if List_of_names.count(x) > 1:
        Bool = True
        break
    else:
        Bool = False
print(Bool)
