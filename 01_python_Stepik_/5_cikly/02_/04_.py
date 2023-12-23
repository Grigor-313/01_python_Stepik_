names = input().lower().split()
i = 0
while i < len(names):
    if names[i][0] == names[i][-1]:
        print('ДА')
        break
    i += 1
else:
    print("НЕТ")

# Петр Анна Иван Сергей Михаил Федор
