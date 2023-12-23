'''Вводятся названия городов в строку через пробел. Необходимо сформировать список с
помощью list comprehension, содержащий названия длиной более пяти символов.
Результат вывести в строчку через пробел.

Sample Input:
Казань Уфа Москва Челябинск Омск Тур Самара

Sample Output:
Казань Москва Челябинск Самара '''

# cities = list(input().split())
print(*[city for city in list(input().split()) if len(city) > 5])

# cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
# a = [city for city in cities if len(city) < 7]
# print(a)
