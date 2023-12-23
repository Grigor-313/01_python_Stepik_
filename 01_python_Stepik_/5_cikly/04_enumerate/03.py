'''
В виде строки записано арифметическое выражение, например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть разным.

Необходимо выполнить вычисление и результат отобразить на экране. Полагается, что в качестве арифметических
операций здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные
числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

10+25 - 12
'''

y = input()
y = y.replace('+', ' + ')
y = y.replace('-', ' - ')
x = list(y.split())
s = int(x[0])

print(x)
for i, m in enumerate(x):
    if m == '-':
        s -= int(x[i + 1])
    elif m == '+':
        s += int(x[i + 1])

print(s)