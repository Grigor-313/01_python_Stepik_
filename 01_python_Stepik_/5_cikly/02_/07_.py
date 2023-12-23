x = int(input())
d = 10
i = 1

while x > 0:
    if d < x:
        d = d + d * 0.1
        i += 1

    else:
        break
print(i)
