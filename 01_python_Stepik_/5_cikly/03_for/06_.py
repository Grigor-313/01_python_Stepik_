cities = list(input().replace('ъ', '').replace('ы', '').replace('ь', '').lower().split())

for i in range(len(cities)):

    if cities[i][-1] != cities[i + 1][0]:
        print('НЕТ')
        break
    i += 1
    if i + 1 == len(cities):
        print('ДА')
        break

# i = a[0]
# print(range(len(cities)))
# print(len(cities))

# Москва Астрахань Новгородъ Димитровграды Душанбе

# Вологда Архангельск Курск Москва
