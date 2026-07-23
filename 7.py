#
# print("-----------------2------------------")
# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1
# print("-----------------3------------------")
# n1 = 10
# while n1 >=1 :
#     print(n1)
#     n1 -= 1
# print("-----------------4------------------")
# n1=1
# while n1 < 11:
#     if not n1%2:
#         print(n1)
#     n1 += 1
# # Користувач вводить із клавіатури два числа.
# # Потрібно показати всі числа в зазначеному діапазоні.
# print("-----------------5------------------")
# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))
# while num1 < num2:
#     print(num1)
#     num1+=1
# # Користувач вводить з клавіатури два числа.
# # Потрібно показати всі непарні числа в зазначеному
# # діапазоні.
# print("-----------------6-------------------")
# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))
# while num1 <= num2:
#     if num1 % 2 == 0:
#         print(num1)
#     num1+=1
#
# while True:
#     word = input("Enter a word: ")
#     if word == "stop":
#         break
#     print(f"Your word {word}")
from turtledemo.forest import start

# print("-----------------7-------------------")
# while True:
#     password=input("Enter a password: ")
#     if password == "admin":
#         break
#     print("Error password")
# print("Password is ok")

# num = 1
# sum = 0
# while num != 0:
#     try:
#         num = int(input("Enter a num: "))
#         print(num)
#         sum += num
#     except ValueError:
#         print("error value")
# print(f"Result is {sum}")

# while True:
#     print("________Menu__________")
#     print("1 Balance")
#     print("2 Exit")
#     try:
#         choice = int(input("Press btn: "))
#         if choice == 1:
#             print("Balance 1000")
#         elif choice == 2:
#             print("End work")
#             break
#     except ValueError:
#         print("Error")


# Користувач вводить з клавіатури два числа.
# Потрібно показати всі парні числа в зазначеному
# діапазоні в спадному порядку.
# try:
#     num1=int(input("Enter a first number: "))
#     num2=int(input("Enter a second number: "))
#     while num2>=num1:
#         if num2%2==0:
#             print(num2)
#             num2-=1
# except ValueError:
#     print("error")

# Користувач вводить з клавіатури два числа.
# Потрібно показати всі числа в зазначеному діапазоні.
# Порядок визначається користувачем:
# 1 — відображаємо у зростаючому порядку,
# 2 — відображаємо у спадному порядку.
# try:
#     start=int(input("Enter a number: "))
#     end=int(input("Enter another number: "))
#     choice=int(input("Enter a choice:1 for cycle getting upwards,2 getting downwards "))
#     if start > end:
#         start,end=end,start
#         print("start")
#     if choice==1:
#         while start<= end:
#             if num1% 2 ==0:
#                 print(start)
#             start+=1
#     elif choice==2:
#         while end > start:
#             if end%2 ==0:
#                 print(end)
#             end -=1
# except ValueError:
#     print("Enter a number")

# Користувач вводить із клавіатури два числа.
# Потрібно показати всі непарні числа в зазначеному
# діапазоні. Якщо межі діапазону вказані неправильно,
# потрібно провести нормалізацію меж. Наприклад,
# користувач ввів 33 і 13, потрібна нормалізація,
# після якої початок діапазону дорівнюватиме 13, а
# кінець 33.
# try:
#     start=int(input("Enter the starting number: "))
#     end=int(input("Enter the ending number: "))
#     if start > end:
#         start,end=end,start
#     while start<= end:
#         if start%2!=0:
#             print(start)
#             start+=1
# except ValueError:
#     print("Error")

# Користувач вводить два числа. Програма повинна показати
# спочатку всі парні числа в діапазоні в зростаючому порядку,
# потім всі непарні числа в спадному порядку. Якщо діапазон
# введено некоректно (переплутані верхня і нижня межі), нормалізувати його.
try:
    start=int(input("Enter the starting number: "))
    end=int(input("Enter the ending number: "))
    if start > end:
        start,end=end,start
    print("Even")
    while start<= end:
        if start %2!=0:
            print(start)
        start+=1
    print("Odd")
    while end>= start:
        if end %2!=0:
            print(end)
         end-=1
except ValueError:
     print("Error")