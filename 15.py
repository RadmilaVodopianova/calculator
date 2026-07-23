# def add(a, b):
#     return a + b
# res=add(2,3)
# print(res)
#
# def greet(name='guest'):
#     print(f"Hello, { name}")
# greet("Max")
#
# def power(number,degree=2):
#     return number ** degree
# print(power(2))
# print(power(2,3))
#
# print(power(3,4))
# print(power(number=3,degree=4))
#
# def total(*args)
#     print(args)
#     return sum(args)
# total(1,2,3)
# nums=[1,2,3]
# print(total(*nums))

# Напишіть функцію, яка повертає добуток чисел у
# вказаному діапазоні. Межі діапазону передаються як
# параметри. Якщо межі діапазону переплутані (наприклад,
# 5 — верхня межа, 25 — нижня межа), їх потрібно
# поміняти місцями.

# def multiple_nums(start, end):
#     result = 1
#     if start>=end:
#         start,end = end,start
#     for i in range(start, end):
#         result *= i
#     return result
# print(multiple_nums(15, 10))

# Напишіть функцію для знаходження максимуму в списку
# цілих. Список передається як параметр.

# def max_nums(*numbers):
#     return max(numbers)
# nums = [1, 2, 3]
# print(max_nums(*nums))
# Завдання 3
# Напишіть функцію, що обчислює суму елементів списку
# цілих. Список передається як параметр.

# def sum_numbers(numbers):
#     return sum(numbers)
# nums = [1, 2, 3]
# print(sum_numbers(nums))

# global namespace
# global_num=100
# def add(a, b):
#     return a + b
#
#
# res = add(2, 3)
# print(res)
#
#
# def greet(name='guest'):
#     print(f"Hello {name}")
#
#
# greet("Max")
#
#
# def power(number, degree=2):
#     return number ** degree
#
#
# print(power(2))
# print(power(2, 3))
#
# print(power(degree=4,
#             number=3
#             ))
#
#
# def total(*args):
#     print(args)
#     return sum(args)
#
#
# total(1, 2, 3)
# print(total(1, 2))
#
# nums = [1, 2, 3]
#
# print(total(*nums))
# namespace global
# global_num = 100
# from random import randint
import random

#
# def choice():
#     pass
#
#
# def test():
#     # namespace local
#     global global_num
#     x = 10
#     print(x)
#     global_num = 500
#     print(f"glob num: {global_num}")
#
#
# # print(x)
# test()
# gx = 2
# print(gx)
# print(f"glob num: {global_num}")
#
#
# def outer():
#     value = 0
#
#     def inner():
#         nonlocal value
#         print("Inner func working")
#         value = 1
#         print(value)
#
#     inner()
#     print(value)
#
#
# outer()
#
#
# def countDown(n):
#     if n == 0:
#         return
#     print(n)
#     countDown(n - 1)
#
#
# countDown(5)
#
#
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)  # 5 * 4 * 3 * 2 * 1
#
#
# print(factorial(5))

# Завдання 4. Сума чисел від 1 до N
# Створіть рекурсивну функцію для обчислення:
# 1 + 2 + 3 + ... + N
def sum_num(n):
    if n==1:
        return 1
    return n+sum_num(n-1)
print(sum_num(5))
# Напишіть рекурсивну функцію:
# power(a, b)
# яка підносить число a до степеня b.
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,10))