n = int(input())
x = 1000
y = 1

while y <= n:
    x += x * 0.05
    y += 1

print(round(x, 2))
