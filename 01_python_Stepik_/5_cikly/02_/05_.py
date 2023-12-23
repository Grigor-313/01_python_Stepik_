n = int(input())
i = 1
m = []
while i <= n:
    if n < 100:
        if i % 3 == 0 and i % 5 == 0:
            m.append(i)
        i += 1
    else:
        print('слишком большое значение n')
        break
print(*m)
