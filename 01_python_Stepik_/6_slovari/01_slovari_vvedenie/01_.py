'''
Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа
 (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой:

print(*sorted(d.items()))

Sample Input:
one=1 two=2 three=3

Sample Output:
('one', 1) ('three', 3) ('two', 2)
'''

c = input().replace('=', ' ').split(' ')
d = dict([[c[i], int(c[i + 1])] for i in range(0, len(c), 2)])
print(*sorted(d.items()))
print(d)
