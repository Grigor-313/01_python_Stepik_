a = input()
a = list(a)
n = len(a)
i = 1
sum = 1
while i <= n:
    d = int(a[i - 1])
    sum *= d
    i += 1
print(sum)
