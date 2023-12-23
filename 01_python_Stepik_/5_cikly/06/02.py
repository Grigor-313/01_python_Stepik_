'''
 Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ
 дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования
 вывести на экран в виде строк из URL-адресов.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya

'''

lst_in = ['django chto  eto takoe    poryadok ustanovki',
          'model mtv   marshrutizaciya funkcii  predstavleniya',
          'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']

for i, line in enumerate(lst_in):
    while line.count('  '):
        line = line.replace('  ', ' ')
    lst_in[i] = line
    while line.count(' '):
        line = line.replace(' ', '-')

    lst_in[i] = line

print(*lst_in, sep='\n')
