'''На вход программы поступают данные в виде набора строк в формате:

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в
словарь d (без использования функции dict()) и вывести его на экран командой:

print(*sorted(d.items()))

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
5=отлично
4=хорошо
3=удовлетворительно

Sample Output:
(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
'''

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
lst_in = [x.replace('=', ' ') for x in lst_in]
for i in range(len(lst_in)):
    d[int(lst_in[i][0])] = lst_in[i][2:]

print(*sorted(d.items()))