n, m = map(int, input().split())
x = n + 1

while x < m and x % 2 != 0:
    print(x, end=' ')
    x += 2
