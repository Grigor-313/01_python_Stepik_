'''
Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n,
 то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.

Sample Input:
11
Sample Output:
2 3 5 7
'''

n = int(input())
s = list(range(2, n))
for i in s:
    for j, m in enumerate(s):
        if i == m:
            continue
        if m % i == 0:
            s.pop(j)
print(*s)
