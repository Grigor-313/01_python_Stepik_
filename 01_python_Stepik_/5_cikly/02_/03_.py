spisok = list(input().split())
dlina = len(spisok)
index = int(0)
kol_vo = 0

while True:
    if index < dlina:
        if len(spisok[index]) >= 5:
            kol_vo += 1
        index += 1

    else:
        break

if kol_vo == dlina:
    print("ДА")
else:
    print('НЕТ')
