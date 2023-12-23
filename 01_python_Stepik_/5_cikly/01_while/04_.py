n = int(input())
x = [1, 1]

while len(x) < n:
    x.append(x[-2] + x[-1])

print(*x)
