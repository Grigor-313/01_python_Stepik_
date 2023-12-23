y = 100
x = []
while y <= 999:
    if y % 47 == 43 and y % 3 == 0:
        x.append(y)
    y += 1
print(*x)
