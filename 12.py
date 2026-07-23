# num1=10
# num2=11
# num3=10
# marks = [10,9,11,12,6]
# print(marks)
# names =["Ilon","Bill","Bob","Jonh"]
# print(names)
# data=[12,0.5,"text",True,12,12]
# print(data)
# list()
# nums=list((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
# print(nums)
# print(names[-1])
# print(names[0:2])
# print(names[2:])
# print(names[4:0:-1])
# print(len(names))
# names[0]='Kate'
# print(names)
# for s in 'python':
#     print(s)
# for elem in marks:
#     print(elem, end=' | ')
# print()
# print(marks)
# sum_marks=0
# for mark in marks:
#     sum_marks+=mark
# print(f"avg marks: {sum_marks/len(marks)}")
# min_marks=marks[0]
# for mark in marks[1:]:
#     if mark<min_marks:
#         min_marks=mark
# print(f"min marks: {min_marks}")
#
# print(sum(marks))
# print(min(marks))
# print(max(marks))
#
# product_list=["banana","apple"]
# print(product_list)
# product_list.append("orange")
# print(f"After add: {product_list}")
# product_list.insert(-1,"bread")
# print(f"After insert: {product_list}")
# product_list.pop()
# print(f"After pop: {product_list}")
# if "apple" in product_list:
#     product_list.remove("apple")
# print(f"After remove: {product_list}")
# print(product_list.count('bread'))
from enum import unique

# Завдання 1
# Користувач з клавіатури вводить елементи списку цілих.
# Необхідно порахувати суму всіх елементів та їхнє
# середньоарифметичне. Результати вивести на екран.
# numbers=[]
# while True:
#     num=int(input("enter a number: "))
#     if num == 0:
#         break
#     numbers.append(num)
# print(sum(numbers))
# print(sum(numbers)/len(numbers))


# Завдання 2
# Користувач з клавіатури вводить елементи списку цілих
# і деяке число. Необхідно порахувати скільки разів дане
# число присутнє у списку. Результат вивести на екран.
# numbers=[]
# while True:
#     num=int(input("enter a number: "))
#     if num == 0:
#         break
#     numbers.append(num)
# find_num=int(input("enter a number to find: "))
# print(numbers.count(find_num))

# Завдання 3
# Користувач з клавіатури вводить список чисел.
# Необхідно знайти суму всіх додатних чисел у списку.
# Результат вивести на екран.
# numbers=[]
# while True:
#     num=int(input("enter a number: "))
#     if num == 0:
#          break
# total=0
# for num in numbers:
#     if num>0:
#         total+=num
# print(total)

# Завдання 4
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно видалити зі списку всі елементи, що
# повторюються, залишивши тільки унікальні. Результат
# вивести на екран.
numbers=[]
while True:
    num=int(input("Enter a number: "))
    if num==0:
        break
    numbers.append(num)
unique=[]
for num in numbers:
    if numbers.count(num)==
print(unique)