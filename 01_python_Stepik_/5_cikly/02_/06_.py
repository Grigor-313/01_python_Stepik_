n = int(input())
i = 1

while n > 0:
    if i ** 2 > n:
        break

    i += 1
print(i)
