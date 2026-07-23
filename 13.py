#
# numbers=[1,2,3,4,5]
# print(numbers)
# # генерація списків
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
#
# squares=[x**2 for x in range(1,11)]
# print(squares)
#
# list2=[i*3 for i in "abc"]
# print(list2)
#
# even_numbers=[x for x in range(20) if x % 2 == 0]
# print(even_numbers)
#
# prices=[100,200,300]
# new_prices=[price * 0.9 for price in prices]
# print(prices)
# print(new_prices)
#
# matrix=[[0 for j in range(3)]for i in range(3)]
# print(matrix)
#
# import random
# rand_nums=[random.randint(-100,100)for i in range(100)]
# print(rand_nums)
#
# user_str='2, 2 ,2'
# list_nums=[int(x) for x in user_str.split(',')]
# print(list_nums)
#
# list_nums.extend([1,2,3])
# print(list_nums)
#
# list_nums.copy()
# new_list=list_nums.copy()
# print(new_list)
# new_list[0] =-1
# print(list_nums)
#
# new_list.sort(reverse=True)
# print(new_list)
#
# words=['afgk','po','a']
# words.sort(key=len)
# print(words)
#
# del new_list[0]
# print(new_list)
# # матриця
# grades = [
#     [10,12,11],
#     [9,8,7],
#     [6,7,6]
# ]
# grades[1][0]=11
#
#
# for row in grades:
#
#     for col in row:
#         print(col, end=' ')
#     print()
# matrix=[[0 for j in range(4)] for i in range(4)]
# for row in matrix:
#     for col in row:
#         print(col, end=' ')
#     print()
#
#
# maximum = grades[0][0]
# for row in grades:
#     for elem in row:
#         if elem > maximum:
#             maximum = elem
# print(maximum)

# Завдання 1
# Створіть список квадратів чисел від 1 до 10
# за допомогою генератора списку.
squares=[x**2 for x in range(1,11)]
print(squares)
# Завдання 2
# Є список:
numbers = [3, 7, -2, 10, -5, 8]
# Створіть новий список, який містить тільки додатні
# числа
positives=[]
for x in numbers:
    if x > 0:
        positives.append(x)
print(positives)
# авдання 3
# Є список:
numbers = [1, 2, 3, 4, 5]
# Створіть новий список, у якому кожен
# елемент збільшений на 10.
new_numbers = []
for x in numbers:
    new_numbers.append(x+10)
print(new_numbers)
# Завдання 4
# Користувач вводить речення.
# Створіть список слів, довжина яких більша
# за 5 символів.
text=input("Enter text")
words = text.split()
result = []
for word in words:
    if len(word)>5:
        result.append(word)
print(result)

# Згенеруйте таблицю множення від 1 до 5 у
# вигляді вкладеного генератора списків.
numbers = [[a * b for b in range(1, 6)] for a in range(1, 6)]
print(numbers)
for row in numbers:
    for col in row:
        print(col, end=' ')
    print()