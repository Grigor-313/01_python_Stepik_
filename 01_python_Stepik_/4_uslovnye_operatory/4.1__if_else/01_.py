a = input().lower()
b = list(a)
print(b)
if b == b[::-1]:
    print("Да")
else:
    print('Нет')
