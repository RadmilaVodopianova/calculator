# for i in range(1,11):
#     print(i)
#
# while True:
#     command = input("Enter exit: ")
#     if command == "exit":
#         break
#
# while True:
#     print("--------Converter usd--------")
#     print("1- usd to uah")
#     print("2- euro to uah")
#     choice=input("Enter number: ")
#     if choice == "1":
#         money = float(input("Enter usd: "))
#         result = money * 44
#         print(f"Result {result} uah")
#     elif choice == "2":
#         money = float(input("Enter euro: "))
#         result = money * 52
#         print(f"Result {result} euro")
#     elif choice == "0":
#         break
#     else:
#         print("Invalid input")
#
#
# max_number=0
# while True:
#     number=int(input("Enter a number: "))
#     if number==0:
#         break
#     if number > max_number:
#         max_number=number
#         print("Update max number",max_number)
# print("Max number",max_number)


# Показати таблицю множення для числа, введеного
# користувачем. Наприклад, якщо користувач вводить число
# 7, потрібно показати:


# zadanie1

# number = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{i} x {number} = {i*number}")

# zadanie2
# Користувач вводить із клавіатури дві межі діапазону і
# число. Якщо число не потрапляє в діапазон, програма
# просить користувача повторно ввести число, і так доти,
# доки він не введе число правильно. Програма відображає
# всі числа діапазону, виділяючи число знаками оклику.

# start = int(input("Enter a starting number: "))
# end = int(input("Enter a ending number: "))
# while True:
#     number=int(input("Enter a number: "))
#     if start<=number<=end:
#         break
# for i in range(start,end+1):
#     if i==number:
#          print(f"!{i}!", end=" ")
#     else:
#         print(i,end=" ")

# for i in range(3):
#     print("Hello")
#
# for row in range(3):
#     for col in range(3):
#         print("*",end="  ")
#     print()
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="  ")
#     print()
#
# height=0
# for row in range(height):
#     for space in range(height-row-1):
#         print("*",end="  ")
#     for star in range(2*row+1):
#         print("*",end="  ")
#     print()

# gra vgadai chuslo
import random
random_number=random.randint(1,10)
print(random_number)
tries=0
while True:
    try:
        user_number=int(input("Enter a number 1-10: "))

        if user_number==0:
            print("Game Over")
            break
        while user_number <1 or user_number >10:
            user_number=int(input("Enter a number 1-10: "))

        tries+=1
        if tries==5:
            print("You lose!")
            print(f"The number was {random_number}")
            print("Game Over")
            break
        if user_number==random_number:
            print("You win!")
            print(f"Count {tries} tries left")
            again = input("Do you want to play again? (yes/no): ")
            if again == "no":
                break
            else:
                random_number = random.randint(1, 10)
                print(random_number)
                tries = 0
                continue
        elif user_number < random_number:
            print("Try bigger!")
        else:
            print("Try lower!")

    except ValueError:
        print("Error")



