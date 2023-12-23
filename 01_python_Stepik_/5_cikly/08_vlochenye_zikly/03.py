'''
Используйте следующий список из строк:

t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
Необходимо преобразовать его в двумерный (вложенный) список lst, где каждая строка представляется списком
из слов (слова разделяются пробелом), но сохранять слова только длиной более трех символов. Решить данную
задачу с использованием list comprehension. Результат отобразить с помощью команды:

print(lst)

Sample Input:

Sample Output:

[['Скажи-ка,', 'дядя,', 'ведь', 'даром'], ['Python', 'выучил', 'каналом'], ['Балакирев', 'раздавал?'],
['Ведь', 'были', 'заданья', 'боевые,'], ['говорят,', 'какие!'], ['Недаром', 'помнит', 'Россия'],
['рубили', 'тогда!']]
'''

t = ["– Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с каналом",
     "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,",
     "Да, говорят, еще какие!",
     "Недаром помнит вся Россия",
     "Как мы рубили их тогда!"
     ]

lst = [[j for j in x if len(j) > 3] for x in [i.split() for i in t]]
print(lst)
