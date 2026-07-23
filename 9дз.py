# Рівень 1
# Завдання 1
# Напишіть програму, яка запитує два цілих числа x і y, після чого обчислює і виводить значення x у степені y.
try:
    x = int(input("Enter number x: "))
    y = int(input("Enter power y: "))
    result = 1
    for i in range(y):
        result = result * x
    print(f"{x} ^ {y} = {result}")
except ValueError:
    print("Error!")


# Завдання 2
# Користувач вводить ціле додатне число. Програма повинна знайти і вивести всі його дільники, а також їхню кількість.
# Приклад введення:
# Введіть число: 28.
# Приклад виведення:
# Дільники числа 28: 1, 2, 4, 7, 14, 28.
# Кількість дільників: 6.
try:
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Error: you must enter a positive number!")
    else:
        count = 0
        print(f"Дільники числа {num}:", end=" ")
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
                if i < num:
                    print(i, end=", ")
                else:
                    print(i, end=".\n")
        print("Кількість дільників:", count)
except ValueError:
    print("Error!")


# Рівень 2
# Завдання 3
# Підрахувати кількість цілих чисел у діапазоні від 100 до 999 у яких є дві однакові цифри.
count = 0
for n in range(100, 1000):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a == b or a == c or b == c:
        count += 1
print(count)

# Завдання 4
# Підрахувати кількість цілих чисел у діапазоні від 100 до 9999 у яких усі цифри різні.
count = 0
for n in range(100, 10000):
    if n <= 999:
        a = n // 100
        b = (n // 10) % 10
        c = n % 10
        if a != b and a != c and b != c:
            count += 1
    else:
        a = n // 1000
        b = (n // 100) % 10
        c = (n // 10) % 10
        d = n % 10
        if a != b and a != c and a != d and b != c and b != d and c != d:
            count += 1
print(count)



# Завдання 6
# Користувач вводить будь-яке ціле число. Необхідно з цього цілого числа видалити всі цифри 3 і 6 і вивести назад на екран.

number = input("Enter number: ")
result = ""
for i in number:
    if i != "3" and i != "6":
        result += i
print(result)




import random

while True:

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print()
        print("--- GAME Rock, Scissors, Paper ---")
        print("r - Rock\ns - Scissors\np - Paper\ne - exit")
        print()
        user = input("Enter your choice - ")
        if user == 'e':
            print("Game over")
            break
        if user not in 'rpse':
            print("Error input, try again!")
            continue

        comp = random.choice('rps')
        rounds += 1
        print(f"Computer choice - {comp}")

        if comp == user:
            print("Tie!")
        elif user == 'r' and comp == 's' or user == 's' and comp == 'p' or user == 'p' and comp == 'r':
            print("User win !")
            player_score += 1
        else:
            print("Comp win!")
            computer_score += 1

        print(f"Your score: {player_score}")
        print(f"Comp score {computer_score}")
        print(f"Round number {rounds}")

        if player_score == 3:
            print("User win the game !")
            break
        elif computer_score == 3:
            print("Comp win the game !")
            break

    choice = input("Do you want to start new game ? (y/n)")
    if choice == 'y':
        continue
    else:
        break