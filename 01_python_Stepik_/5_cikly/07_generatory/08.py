'''Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
С помощью list comprehension сформировать третий список, состоящий из суммы соответствующих
пар чисел введенных списков. Результат вывести на экран в одну строку через пробел.

Sample Input:
1 2 3 4 5
6 7 8 9 10

Sample Output:
7 9 11 13 15
'''

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
n = len(a)
lst = [c.append(a[i] + b[i]) for i in range(n)]
print(*c)
