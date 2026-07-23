# Завдання 1. Вартість покупки
# Створіть функцію:
# calculate_price(price, quantity=1)
# Функція повинна повертати загальну вартість товару.
def calculate_price(price, quantity=1):
    return price * quantity
print(calculate_price(50))
print(calculate_price(50, 2))
# Завдання 2. Інформація про студента
# Створіть функцію:
# show_student(name, age, group="Не вказана")
# Виведіть інформацію про студента.
# Викличте функцію як зі звичайними, так і з іменованими аргументами.
def show_student(name, age, group="Не вказана"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Group: {group}")
show_student("Rada", 22,62)
show_student(name="Rada", age=22, group=62)
# Завдання 3. Середнє арифметичне
# Створіть функцію:
# average(*args)
# Функція повинна знаходити середнє арифметичне всіх переданих чисел.
def average(*args):
    return sum(args) / len(args)
print(average(1, 2, 6))
print(average(1, 15, 20, 23))
# Завдання 4. Пошук мінімального числа
# Створіть функцію:
# find_min(*args)
# Знайдіть найменше число без використання min().
def find_min(*args):
    minimum = args[0]
    for num in args:
        if num < minimum:
            minimum = num
    return minimum
print(find_min(5, 2, 1, 1, 9))
print(find_min(10, 9, 8))
 # Завдання 6.
 # Рекурсивна сума цифр числа
 # Створіть рекурсивну функцію:
 # sum_digits(n)
 # яка знаходить суму цифр числа.
 # Приклад:
 # Введіть число: 583
 # 16
 # Тому що:
 # 5 + 8 + 3 = 1
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
number = int(input("Введіть число: "))
print(sum_digits(abs(number)))