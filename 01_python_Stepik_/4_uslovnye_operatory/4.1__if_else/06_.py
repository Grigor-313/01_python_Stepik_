a = input().split()
print(a)
if 'Москва' in a:
    a.remove('Москва')
print(*a)
