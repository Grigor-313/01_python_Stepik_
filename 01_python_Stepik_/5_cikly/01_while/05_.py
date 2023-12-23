n = int(input())
x = 1
n = n // 3
z = [1]
while len(z) <= n:
    z.append(z[-1] * 2)

print(z[-1])
