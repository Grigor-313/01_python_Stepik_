p = [0] * 10
i = 0

while p.count(1) < 5:
    i = int(input('Введите число: '))
    if p[i] != 1:
        p[i] = 1
    i += 1
    continue

print(*p)
