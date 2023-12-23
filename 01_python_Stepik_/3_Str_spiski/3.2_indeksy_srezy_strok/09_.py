a, b = input().split()
c = a[:len(b)]
print(c)
print(b[1::2] == c[::2])
