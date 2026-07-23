

#
# number=int(input("enter the number"))
# count=0
# for i in range(1,number+1):
#     if number%i==0:
#         print(i)
#         count+=1
# print(f"Count {count}")
#
#
# number=int(input("enter the number"))
# sum_divisors=0
# for i in range(1,number+1):
#     if number%i==0:
#         sum_divisors==number:
#         print("Doskonale")
#     else:
#         print("Not Doskonale")
#
# a=number//100
# b=number%10
# c=number%100
# print(f"a {a} b {b} c {c}")

# Користувач вводить з клавіатури ширину та висоту прямокутника. Потрібно відобразити на екран
# заповнений прямокутник із зазначеними висотою та шириною. Наприклад, якщо користувач ввів висоту
# 3, а ширину 5 на екрані буде виведено:

# height=int(input("enter the height"))
# width=int(input("enter the width"))
#
# for i in range(height):
#     print("*"*width)

# Завдання 2
# Необхідно написати програму, яка малює заповнену фігуру – квадрат або прямокутник
# – залежно від вибору користувача. Програма повинна виконувати такі кроки:
# Запросити в користувача тип фігури (квадрат або прямокутник).
# Запросити розміри фігури:
# Якщо обрано квадрат, запитати довжину сторони;
# Якщо обрано прямокутник, запитати ширину і висоту.
# Запросити символ, яким буде заповнена фігура.
# Вивести заповнену фігуру на екран.

# fig=input("Choose figures: 1 квадрат 2 прямокутник")
# symbol=input("Choose a symbol")
# if fig =="1":
#     height = int(input("enter the height"))
#     for i in range(height):
#         print(symbol*height)
# elif fig =="2":
#     height=int(input("enter the height"))
#     width=int(input("enter the width"))
#     for i in range(height):
#         print(symbol*width)
# else:
#     print("Wrong choice")


# Користувач вводить з клавіатури розмір сторони квадрата. Потрібно
# відобразити на екран незаповнений квадрат (відображаються тільки межі квадрата).
# Розмір сторони дорівнює введеному розміру.
# lenght=int(input("enter the length of the number"))
# for i in range(lenght):
#     for j in range(lenght):
#         if i==0 or i==lenght-1 or j==0 or j==lenght-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# Користувач вводить з клавіатури довжину і ширину
# прямокутника. Потрібно відобразити на екран незаповнений
# прямокутник (відображаються тільки межі прямокутника).
# Розмір довжини та ширини дорівнює введеним даним.
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# for i in range(width):
#     for j in range(length):
#         if i == 0 or i == width - 1 or j == 0 or j == length - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Гра камінь/ножиці/папір


# import random
#
# while True:
#
#     player_score = 0
#     computer_score = 0
#     rounds = 0
#
#     while True:
#         print()
#         print("--- GAME Rock, Scissors, Paper ---")
#         print("r - Rock\ns - Scissors\np - Paper\ne - exit")
#         print()
#         user = input("Enter your choice - ")
#         if user == 'e':
#             print("Game over")
#             break
#         if user not in 'rpse':
#             print("Error input, try again!")
#             continue
#
#         comp = random.choice('rps')
#         rounds += 1
#         print(f"Computer choice - {comp}")
#
#         if comp == user:
#             print("Tie!")
#         elif user == 'r' and comp == 's' or user == 's' and comp == 'p' or user == 'p' and comp == 'r':
#             print("User win !")
#             player_score += 1
#         else:
#             print("Comp win!")
#             computer_score += 1
#
#         print(f"Your score: {player_score}")
#         print(f"Comp score {computer_score}")
#         print(f"Round number {rounds}")
#
#         if player_score == 3:
#             print("User win the game !")
#             break
#         elif computer_score == 3:
#             print("Comp win the game !")
#             break
#
#     choice = input("Do you want to start new game ? (y/n)")
#     if choice == 'y':
#         continue
#     else:
#         break

# Втеча з підземелля"
# Гравець рухається кімнатами.
# У кожній кімнаті потрібно обрати дію:
# 1 - Йти вперед
# 2 - Відкрити скриню
# 3 - Вийти з гри
# Події визначаються випадково:
# знайдено золото;
# знайдено зілля;
# зустріли монстра.
# Якщо здоров'я стало 0 — програш.
# Якщо пройшли 10 кімнат — перемога.

import random
while True:
    health = 100
    gold = 0
    rooms = 0
    while True:
        print("1 - Йти вперед")
        print("2 - Відкрити скриню")
        print("3 - Вийти з гри")
        choice = input("Choose action: ")
        if choice == "1":
            rooms += 1
            comp = random.randint(1, 3)
            if comp == 1:
                gold += 10
                print("Знайдено золото!")
            elif comp == 2:
                health += 20
                print("Знайдено зілля!")
            else:
                health -= 30
                print("Ви зустріли монстра!")
        elif choice == "2":
            comp = random.randint(1, 3)
            if comp == 1:
                gold += 20
                print("У скрині було золото!")
            elif comp == 2:
                health += 10
                print("У скрині було зілля!")
            else:
                health -= 20
                print("У скрині був монстр!")
        elif choice == "3":
            print("Game over")
            break
        else:
        if health <= 0:
            print("здоров'я стало 0 — програш")
            break
        if rooms >= 10:
            print("пройшли 10 кімнат — перемога")
            break

