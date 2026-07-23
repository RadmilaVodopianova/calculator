# Завдання 1
# Користувач вводить із клавіатури два числа. Потрібно порахувати окремо суму парних, непарних і чисел, кратних 9 у
# вказаному діапазоні, а також середньоарифметичне кожної групи.
try:
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    sum_even = 0
    sum_odd = 0
    count_even = 0
    count_odd = 0
    sum9 = 0
    count9 = 0
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            sum_even += i
            count_even += 1
        else:
            sum_odd += i
            count_odd += 1
        if i % 9 == 0:
            sum9 += i
            count9 += 1
    if count_even > 0:
        print(f"Average of even numbers: {sum_even/count_even}")
    else:
        print("No even numbers in range")
    if count_odd > 0:
        print(f"Average of odd numbers:{sum_odd/count_odd}")
    else:
        print("No odd numbers in range")
    if count9 > 0:
        print(f"Average of numbers divisible by 9: {sum9/count9}")
    else:
        print("No numbers divisible by 9 in range")
    print("Sum of even numbers:", sum_even)
    print("Sum of odd numbers:", sum_odd)
    print("Sum of numbers divisible by 9:", sum9)
except ValueError:
    print("Error")
# Завдання 2
# Користувач вводить з клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані
# вертикальну лінію із введеного символу, зазначеної довжини.
try:
    length = int(input("Enter line length: "))
    symbol = input("Enter symbol: ")
    for i in range(length):
        print(symbol)
except ValueError:
    print("Error")
# Завдання 3
# Користувач вводить із клавіатури числа. Якщо число більше нуля потрібно вивести напис "Number is positive", якщо менше
# нуля "Number is negative", якщо дорівнює нулю "Number is equal to zero". Коли користувач вводить число 7 програма
# припиняє свою роботу і виводить на екран напис "Good bye!".
while True:
    try:
        num = int(input("Enter a number: "))
        if num > 0:
            print("Number is positive")
        elif num < 0:
            print("Number is negative")
        else:
            print("Number is equal to zero")
        if num == 7:
            print("Good bye!")
            break
    except ValueError:
        print("Error")
# Завдання 4
# Користувач вводить із клавіатури числа. Програма повинна підраховувати суму, максимум і мінімум, введених чисел.
# Коли користувач вводить число 7 програма припиняє свою роботу і виводить на екран напис "Good bye!".

try:
    num = int(input("Enter a number: "))
    sum = 0
    max = num
    min = num
    while True:
        if num == 7:
            print("Good bye!")
            break
        sum = sum + num
        if num > max:
            max = num
        if num < min:
            min = num
        num = int(input("Enter a number: "))
    print("Sum total", sum)
    print("Maximum", max)
    print("Minimum", min)
except ValueError:
    print("Error")
# Завдання 5
# Напишіть програму, яка перевіряє, чи є введене користувачем число простим.
#
# Принцип роботи програми:
#
# Програма повинна запитувати в користувача ціле число N.
# Якщо число N просте, програма виводить повідомлення: "Число N є простим".
# Якщо число N не є простим, програма виводить повідомлення: "Число N не є простим".
# Якщо користувач вводить число, що менше або дорівнює 1, програма виводить повідомлення: ("Число має бути більшим за "
#                                                                                          1") і завершує виконання.
# Що таке просте число:
# Просте число — це число більше за 1, яке ділиться тільки на 1 і на саме себе. Наприклад, 2, 3, 5, 7, 11 тощо.
try:
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Число має бути більшим за 1")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"Число {n} не є простим")
                break
        else:
            print(f"Число {n} є простим")
except ValueError:
    print("Error")
# Завдання 6
# Напишіть програму, яка перевіряє, чи є введене користувачем число членом послідовності Фібоначчі.
#
# Принцип роботи програми:
#
# Програма повинна запитувати у користувача ціле число N .
# Якщо число N належить послідовності Фібоначчі, програма виводить повідомлення: ("Число N належить послідовності
#  Фібоначчі").Якщо число N не належить послідовності Фібоначчі, програма виводить повідомлення: "Число N не належить
# послідовності Фібоначчі".
# Що таке число Фібоначчі:
# Числа Фібоначчі — це числа, що утворюють послідовність, у якій кожне наступне число є сумою двох попередніх.
#  Початкові значення: 0,1,1,2,3,5,8,13, і так далі.
try:
    print(" Початкові значення: 0,1,1,2,3,5,8,13")
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    while a < n:
        a, b = b, a + b
    if a == n:
        print(f"Число {n} належить послідовності Фібоначчі")
    else:
        print(f"Число {n} не належить послідовності Фібоначчі")
except ValueError:
    print("Error")



