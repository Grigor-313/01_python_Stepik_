a = list(input().split(' '))
b = list(a.pop(0))
c = list(a.pop(0))
print(*a, (b.pop(0) + '.' + c.pop(0) + '.'))
