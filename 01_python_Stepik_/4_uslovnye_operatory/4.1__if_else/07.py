a, b, c, d = map(int, input().split())
if (a - 2) >= c and (b - 2) >= d:
    print('ДА')
else:
    if (a - 2) >= d and (b - 2) >= c:
        print('ДА')
    else:
        print('НЕТ')
# a, b, c, d = list(map(int, input().split()))
# print("ДА") if a-2 >= c and b-2 >= d or a-2 >= d and b-2 >= c else print("НЕТ")
