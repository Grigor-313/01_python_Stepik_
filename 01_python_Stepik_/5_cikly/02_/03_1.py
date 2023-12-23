lst = input().split()

i = 0
ans = 'ДА'

while i < len(lst):
    if len(lst[i]) < 6:
        ans = 'НЕТ'
        break

    else:
        i += 1

print(ans)
