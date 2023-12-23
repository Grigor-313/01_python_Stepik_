'''PyDev console: starting.
Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
['Москва', 'Тверь', 'Вологда']
['Москва', 'Тверь', 'Вологда']
marks = [2, 3, 4 ,3, 5, 2]
marks[0]
2
marks[1]
3
(marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]) / 6
3.1666666666666665
marks[-1]
2
marks[0] = 3
(marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]) / 6
3.3333333333333335
marks[1] = 'удовлетворительно'
marks
[3, 'удовлетворительно', 4, 3, 5, 2]
lst = ['Москва', 1320, 5.8, True, 'Тверь', False]
lst
['Москва', 1320, 5.8, True, 'Тверь', False]
lst2 = [1, 2.5, [-1, -2, -3], 4]
lst2
[1, 2.5, [-1, -2, -3], 4]
a = []
a
[]
b = list()
b
[]
b = list([True, False])
b
[True, False]
list('python')
['p', 'y', 't', 'h', 'o', 'n']
t = [23.5, 25.6, 27.3, 26.0, 30.4, 29.5]
t
[23.5, 25.6, 27.3, 26.0, 30.4, 29.5]
min(t)
23.5
max(t)
30.4
sum(t)
162.3
sum(t) / len(t)
27.05
sorted(t)
[23.5, 25.6, 26.0, 27.3, 29.5, 30.4]
t_sort = sorted(t)
t_sort
[23.5, 25.6, 26.0, 27.3, 29.5, 30.4]
t_sort = sorted(t, reverse=True)
t_sort
[30.4, 29.5, 27.3, 26.0, 25.6, 23.5]
s = ('python')
s
'python'
s = list('python')
s
['p', 'y', 't', 'h', 'o', 'n']
max(s)
'y'
min(s)
'h'
sorted(s)
['h', 'n', 'o', 'p', 't', 'y']
[1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3] + [True]
[1, 2, 3, True]
['Я', 'люблю', 'Python']
['Я', 'люблю', 'Python']
['Я', 'люблю', 'Python'] * 3
['Я', 'люблю', 'Python', 'Я', 'люблю', 'Python', 'Я', 'люблю', 'Python']
['Я'] + ['люблю'] * 3 +['Python']
['Я', 'люблю', 'люблю', 'люблю', 'Python']
lst = ['Москва', 1320, 5.8, True, 'Тверь', False]
1230 in lst
False
1320 in lst
True
[1, 2]
[1, 2]
lst = ['Москва', 1320, 5.8, True, 'Тверь', [1, 2], False]
[1, 2] in lst
True
'Москва' in lst
True
del lst[2]
lst
'['Москва', 1320, True, 'Тверь', [1, 2], False]' '''
