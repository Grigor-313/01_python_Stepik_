book = [input(), input(), int(input()), float(input())]
book[1] = 'Пушкин'
del book[2]
book[2] = book[2] * 2
print(book)
