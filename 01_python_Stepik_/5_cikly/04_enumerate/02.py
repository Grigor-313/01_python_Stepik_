'''Вводится строка с номером телефона. Ожидается формат ввода:

+7(xxx)xxx-xx-xx

где x - это цифра. Размер введенных символов считается верным (то есть, не может быть,
чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо проверить, что введенная строка
соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.
+7(123)456-78-99
'''

number = input()

j = 0

for i, m in enumerate(number):
    if (number[0] == '+' and number[1] == '7' and number[2] == '(' and number[3:6].isdigit() and number[6] == ')'
            and number[7:10].isdigit() and number[10] == '-' and number[11:13].isdigit() and number[13] == '-'
            and number[14:-1].isdigit()):
        j += 1
if j == len(number):
    print('ДА')

else:
    print('НЕТ')

'''
num = '+7(xxx)xxx-xx-xx'
s = input()
if len(s) == len(num):
    for i,v in enumerate(s):
        if v == num[i]:
            continue
        elif v.isdigit() == True:
            num = num.replace('x', v, 1)
if num == s:
    print('ДА')
else:
    print('НЕТ')
'''
