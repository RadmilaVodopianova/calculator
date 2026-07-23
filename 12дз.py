# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних і непарних чисел.
# Результати вивести на екран.
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Парних чисел: {even}")
print(f"Непарних чисел: {odd}")
# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення у списку.
# Результати вивести на екран.
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
print(f"Максимальне число: {max(numbers)}")
print(f"Мінімальне число: {min(numbers)}")
# Рівень 2
# Завдання 3
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний,
# від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати
# кількість нулів. Результати вивести на екран.
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))
print(numbers)
positive_count = 0
negative_count = 0
zero_count = 0
positive_numbers = []
negative_numbers = []
for num in numbers:
    if num > 0:
        positive_count += 1
        positive_numbers.append(num)
    elif num < 0:
        negative_count += 1
        negative_numbers.append(num)
    else:
        zero_count += 1
if len(positive_numbers) > 0:
    print(f"Мінімальний додатний: {min(positive_numbers)}")
else:
    print("Додатних чисел немає")
if len(negative_numbers) > 0:
    print(f"Максимальний від'ємний: {max(negative_numbers)}")
else:
    print("Від'ємних чисел немає")
print(f"Кількість додатних: {positive_count}")
print(f"Кількість від'ємних: {negative_count}")
print(f"Кількість нулів: {zero_count}")
# Завдання 4
# Користувач із клавіатури вводить список цілих чисел і деяке число. Необхідно видалити зі списку всі елементи, які менші
# за задане число. Результат вивести на екран.
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
limit = int(input("Enter a number: "))
new_numbers = []
for num in numbers:
    if num >= limit:
        new_numbers.append(num)
print(new_numbers)
