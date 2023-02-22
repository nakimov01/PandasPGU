import random

print('A1 ', "______________________________________________________________________________", '\n')
List = [round(random.uniform(-99.999, 100), 2) for x in range(10)]  # Создание списка из 10 элементов случайными числами
Avg__Val = round(sum(List) / 10, 2)  # Среднее значение списка из 10 элементов
print("Список:", List, '\n', "Среднее значение списка: ", Avg__Val)
List.insert(0, Avg__Val)  # Добавление среднего значения в начало списка
print("Добавление среднего значения в начало списка: ", List, "\n")

print('A2 ', '______________________________________________________________________________', '\n', 'Матрица 5х5')

N, M = 5, 5
Matr = [[round(random.uniform(-100, 100), 2) for i in range(N)] for j in range(M)]  # Создание матрицы 5x5
avg_res = 0
res_sum = 0
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end=' ')
    print()
print('_____________________________________________________________________________', '\n')
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        res_sum += Matr[i][j]
print("Сумма элементов матрицы: ", round(res_sum, 2), "\n")
print('______________________________________________________________________________', '\n')
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if i == j:
            avg_res += Matr[i][j]
            print(Matr[i][j])

print('\n', "Среднее значение элементов на главной диагонали: ", round((avg_res / 5), 2), "\n")
print('______________________________________________________________________________', '\n')
print('Элеметы побочной диагонали: ')
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        if j == (len(Matr[i]) - i - 1):
            print(Matr[i][j])
            if Matr[i][j] < 0:
                Matr[i][j] = 0
print()
print("Замена нулями всех отрицательных элементов на побочной диагонали: ")
for i in range(len(Matr)):
    for j in range(len(Matr[i])):
        print(Matr[i][j], end=' ')
    print()
print('\n', "A3 ", '______________________________________________________________________________', '\n')
MyDict = {'5702-323241': 'Портнов И.П.', '5702-434451': 'Светлов К.И.', '5702-432441': 'Акимов Н.М.',
          '5702-430141': 'Акимов Н.М.', '5702-439901': 'Медведев Д.С.',
          input("Введите паспорт: \n"): input("Введите фамилию с инициалами: \n")}
print(MyDict, '\n')
print('______________________________________________________________________________')
passport = str(input("Введите паспорт который хотите изменить: \n"))
if passport in MyDict:
    MyDict[passport] = input("Изменить ФИО на: \n")
else:
    print('Паспорт не найден')
print(MyDict)

print('______________________________________________________________________________')
print('Есть ли полные совпадения ФИО в списке всех владельцев паспортов: ', '\n')

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
