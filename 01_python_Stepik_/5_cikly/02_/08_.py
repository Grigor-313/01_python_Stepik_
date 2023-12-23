lst_in = ['Мастер Маргарита', 'Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок',
          'Муму']
m = len(lst_in)
i = -1

while True:
    if m + 1 != abs(i):
        if ' ' in lst_in[i]:
            lst_in.pop(i)
            m = len(lst_in)
        else:
            i += -1
    else:
        break
print(*lst_in)
