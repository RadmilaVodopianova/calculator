# 1.Використовуючи функцію map, перетворіть список рядків на список їх довжин. Вихідний список:
# ["apple", "banana", "cherry"].
words = ["apple", "banana", "cherry"]
result = list(map(len, words))
print(result)
# 2.Використовуючи функцію filter, відфільтруйте список рядків, залишивши лише рядки, що
# починаються з літери "a". Вихідний список: ["apple", "banana", "cherry"].
words = ["apple", "banana", "cherry"]
result = list(filter(lambda word: word.startswith("a"), words))
print(result)
# 3.Використовуючи функції map і filter, створіть новий список, у якому залишаться лише числа, що
# поділяються на 3. Вихідний список: [1, 2, 3, 4, 5].
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x, filter(lambda x: x % 3 == 0, numbers)))
print(result)
# 4.Використовуючи функцію zip, об'єднайте два списки чисел до списку пар чисел. Вихідні списки:
# [1, 2, 3] та [4, 5, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(zip(list1, list2))
print(result)
# 5.Використовуючи функцію map, перетворіть два списки чисел на список їх творів. Вихідні списки:
# [1, 2, 3] та [4, 5, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x * y, list1, list2))
print(result)
# 6.Використовуючи функцію filter, відфільтруйте список пар чисел, залишивши лише пари, в яких
# перше число більше за друге.
# Вихідний список: [(1,2), (3, 1), (4, 4), (5, 3)].
numbers = [(1, 2), (3, 1), (4, 4), (5, 3)]
result = list(filter(lambda pair: pair[0] > pair[1], numbers))
print(result)
# 7.Даний список чисел, відфільтрувати тільки позитивні
numbers = [-5, -3, -1, 0, 1, 3, 5]
result = list(filter(lambda x: x > 0, numbers))
print(result)
# 8.Даний список чисел, відфільтрувати числа в діапазоні вказаним користувачем
numbers = [1, 2, 8, 3, 12, 4, 16]
start = int(input("Start: "))
end = int(input("End: "))
result = list(filter(lambda x: start <= x <= end, numbers))
print(result)
# 9.Даний список чисел, відфільтрувати всі цілі значення
numbers = [1, 1.2, 2, 2.2, 3, "lol", True]
result = list(filter(lambda x: type(x) == int, numbers))
print(result)
# 10.Даний список логінів користувачів, додайте кожному логіну приставку "$"
logins = ["Bob", "Bill", "Bib"]
result = list(map(lambda login: "$" + login, logins))
print(result)
# 11.На основі трьох списків різних значень, сформувати список, елемент якого містить набір із
# елементів інших списків.
names = ["Bob", "Bill", "Bib"]
ages = [12, 9, 11]
groups = ["A", "B", "C"]
result = list(zip(names, ages, groups))
print(result)