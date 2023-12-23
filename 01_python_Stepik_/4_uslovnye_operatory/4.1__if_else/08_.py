c = list(map(int, input()))
if sum(c[:3]) == sum(c[3:]):
    print('ДА')
else:
    print('НЕТ')

# print("ДА") if sum(c[:2]) == sum(c[:-3]) else print("НЕТ")
