x = list(map(int, input().split()))
s = 0
for i in x:
    if i % 2 != 0:
        s += i
print(s)
# 8 11 -2 4 0 13 19 12 7
