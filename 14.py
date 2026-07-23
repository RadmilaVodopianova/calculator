# print("Hello!")
# print("Hello!")
# print("Hello!")
# print("Hello!")
# print("Hello!")
#
# def welcome():
#     print("Hello from func!")
# welcome()
# welcome()
# print(abs(-20))
# print(round(5.30504))
# print(sum([1,2,3,]))
# print(pow(2,3))
# print(divmod(10,2))
# hours,minutes=divmod(130,60)
# print(f'Hours:{hours} Minutes:{minutes} ')
#
# import random
# print(random.chice([1,2,3]))
# numbers = [1,2,3,4,5,6]
# random.shuffle(numbers)
# print(numbers)
# def hello():
#     print("Hello from func!")
# hello()
# def print_line():
#     print("-"*50)
# print_line()

# def morning():
#     print("Drink some coffee")
# morning()
#
# def quote():
#     print('''"Don't let the noise of others' opinions
#     drown out your own inner voice."
# Steve Jobs''')
# quote()
#
# def greet(name):
#     print("Hello,", name)
# greet("Bob")
# greet("Max")
#
# def show_user_info(name,age):
#     print(name)
#     print(age*7)
# age = 12
# show_user_info("Bill",age)
# def add(num1,num2):
#     return num1+num2
#
# result=add(1,2)*2
# print(result)
#
# def get_info():
#     return 'max',20,"123654"
# result=add(1,2)*2
# print(result)
# result=get_info()
# print(result)
#
# def menu(choose):
#     if choose == 1:
#         return "Your choice 1"
#     elif choose == 2:
#         return "Your choice 2"
# print(menu(2))

# Завдання2
# Напишіть функцію, яка приймає два числа як параметр
# і відображає всі непарні числа між ними.
# start=int(input("Enter Starting Number: "))
# end=int(input("Enter Ending Number: "))
# def count(start,end):
#    for i in range(start,end+1):
#        if i%2:
#            print(i)
# count(start,end)
# Завдання 3
# Напишіть функцію, яка відображає горизонтальну або
# вертикальну лінію з деякого символу. Функція приймає
# як параметр: довжину лінії, напрямок, символ.
# line=int(input("Enter length of line: "))
#
# def show_line(height,symbol,nap):
#     if nap=="x":
#         print(height*symbol)
#     elif nap=="y":
#         for i in range(height):
#             print(symbol)
#     else:
#         print("Invalid input")
# nap=input("x - horizontal\ny - vertical ")
# symbol=input("Enter symbol: ")
# show_line(line,symbol,nap)
# Завдання 4
# Напишіть функцію, яка повертає максимальне з чотирьох
# чисел. Числа передаються як параметри.

def max_num(n1,n2,n3,n4):
    maximum=n1
    if n2>maximum:
        maximum=n2
    if n3>maximum:
        maximum=n3
    if n4>maximum:
        maximum=n4
    return maximum
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))
n4=int(input("Enter a number: "))
print(max_num(n1,n2,n3,n4))