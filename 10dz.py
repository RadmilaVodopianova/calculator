# Завдання 1
# Користувач вводить висоту трикутника і символ для заповнення. Програма повинна
# вивести трикутник, вирівняний по правому краю.
# Приклад введення:
#  Введіть висоту: 4.
#  Введіть символ: $.

height = int(input("Enter a height: "))
symbol = input("Enter a symbol: ")
if height <= 0:
    print("Height must be greater than 0")
else:
    for i in range(1, height + 1):
        print(" " * (height - i) + symbol * i)

# Завдання 2
# Користувач вводить розміри дошки (ширину і висоту) і два символи для клітинок.
# Програма повинна відобразити шахову дошку, використовуючи ці символи.

width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
symbol1 = input("Enter a symbol: ")
symbol2 = input("Enter a second symbol: ")
if height <= 0 or width <= 0:
    print("Height and width must be greater than 0")
else:
    for i in range(height):
        for j in range(width):
            if (i + j) % 2 == 0:
                print(symbol1, end=" ")
            else:
                print(symbol2, end=" ")
        print()

# Завдання 3
# Програма випадковим чином загадує чотиризначне число без цифр, що
# повторюються. Користувач повинен спробувати вгадати це число, вводячи свої
# варіанти. Після кожного введення програма повідомляє:
#  Кількість цифр, які стоять на своїх місцях (бики).
#  Кількість цифр, які є в числі, але стоять не на своїх місцях (корови).

import random
while True:
    random_number = random.randint(1000, 9999)
    r1 = random_number // 1000
    r2 = random_number // 100 % 10
    r3 = random_number // 10 % 10
    r4 = random_number % 10
    if len({r1, r2, r3, r4}) == 4:
        break
attempts = 0
while True:
    user_number = int(input("Enter your number: "))
    if user_number == 0:
        print("GAME OVER. Computer number was:", random_number)
        break
    if user_number < 1000 or user_number > 9999:
        print("Must be 4 numbers!")
        continue
    attempts += 1
    u1 = user_number // 1000
    u2 = user_number // 100 % 10
    u3 = user_number // 10 % 10
    u4 = user_number % 10
    bull = 0
    cow = 0
    if u1 == r1:
        bull += 1
    elif u1 in (r2, r3, r4):
        cow += 1
    if u2 == r2:
        bull += 1
    elif u2 in (r1, r3, r4):
        cow += 1
    if u3 == r3:
        bull += 1
    elif u3 in (r1, r2, r4):
        cow += 1
    if u4 == r4:
        bull += 1
    elif u4 in (r1, r2, r3):
        cow += 1
    print("Bulls:", bull, "Cows:", cow)
    if bull == 4:
        print("U WIN! U GUESSED THE NUMBER", random_number, "BY", attempts, "ATTEMPTS")
        break
# Завдання 4
# Напишіть консольну гру “Битва з босом”.
# Програма повинна:
# 1. Створити здоров’я гравця — 100.
# 2. Створити здоров’я боса — 150.
# 3. Запустити цикл гри.
# 4. Кожен раунд показувати HP гравця і HP боса.
# 5. Давати гравцю вибір дії:
# o 1 — атакувати;
# o 2 — лікуватися;
# o 3 — втекти.
# 6. Якщо гравець атакує — бос втрачає випадкову кількість HP від 10 до 30.
# 7. Якщо гравець лікується — гравець відновлює випадкову кількість HP від 10 до 25.
# 8. Якщо гравець тікає — гра завершується.
# 9. Після дії гравця бос атакує і завдає випадкову шкоду від 5 до 20.
# 10. Якщо HP боса стало 0 або менше — гравець переміг.
# 11. Якщо HP гравця стало 0 або менше — гравець програв.

import random
try:
    player_hp = 100
    boss_hp = 150
    print("-----------Battle with Boss -----------------")
    while True:
        print("\nPlayer HP:", player_hp)
        print("Boss HP:", boss_hp)
        print("1 - Attack")
        print("2 - Heal")
        print("3 - Run")
        choice = input("Your choice: ")
        if choice == "1":
            damage = random.randint(10, 30)
            boss_hp -= damage
            print("You hit boss for", damage, "damage!")
        elif choice == "2":
            heal = random.randint(10, 25)
            player_hp += heal
            print("You heal yourself for", heal, "HP!")
        elif choice == "3":
            print("You run away. Game Over.")
            break
        else:
            print("Wrong choice!")
            continue
        if boss_hp <= 0:
            print("Boss is defeated! You win!")
            break
        boss_damage = random.randint(5, 20)
        player_hp -= boss_damage
        print("Boss hits you for", boss_damage, "damage!")
        if player_hp <= 0:
            print("Your HP is 0. You lose!")
            break
except ValueError:
    print("Error: wrong input!")



