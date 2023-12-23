m, n = map(int, input().split())
c = m % n
if c == 0:
    print(m // n)
else:
    print(f'{m} на {n} нацело не делится')
