s = 1
while True:
    a = int(input())
    if a > 0:
        s = s * a
    elif a < 0:
        continue
    else:
        break
print(s)
