'''
Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых
позициях, единиц (см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по
 горизонтали, вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит
 вывести ДА, иначе - НЕТ.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0

Sample Output:
ДА'''
b = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

fl = 1
for i in range(len(b) - 1):
    for j in range(len(b) - 1):
        sum_1 = b[i][j] + b[i][j + 1] + b[i + 1][j] + b[i + 1][j + 1]
        if sum_1 > 1:
            fl = 0
            break
        else:
            sum_1 = 0

print("ДА" if fl == 1 else "НЕТ")
