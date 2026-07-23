# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:
# "Don't compare yourself with anyone in this world…
#     if you do so, you are insulting yourself."
#         Bill Gates
def show_quote():
    print('"Don\'t compare yourself with anyone in this world…')
    print('    if you do so, you are insulting yourself."')
    print('        Bill Gates')
show_quote()
# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.
def show_even_numbers(start, end):
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
show_even_numbers(10, 1)
# Рівень 2
# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.
def draw_square(size, symbol, mode):
    for i in range(size):
        if mode == "filled":
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + " " * (size - 2) + symbol)
draw_square(5, "*", "filled")
draw_square(5, "*", "empty")
# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри
def minimum_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)
result = minimum_of_five(8, 3, 15, 2, 10)
print("Мінімальне число:", result)
# Рівень 2
# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.
def draw_square(size, symbol, filled):
    for i in range(size):
        if filled == 1:
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + " " * (size - 2) + symbol)
draw_square(5, "*", 1)  
print()
draw_square(5, "*", 0)
# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри
def min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)
print(min_of_five(8, 3, 15, 2, 10))