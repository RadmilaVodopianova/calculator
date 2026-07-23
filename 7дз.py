# Завдання 1
# Користувач вводить із клавіатури два числа (початок і кінець діапазону).
# Потрібно проаналізувати всі числа в цьому діапазоні за таким правилом:
# якщо число кратне 7, його треба виводити на екран.
try:
    start=int(input("Enter a first number: "))
    end=int(input("Enter a second number: "))
    while start <= end:
        if start % 7 == 0:
            print(start)
        start += 1
except ValueError:
    print("Error")
# Завдання 2
# Користувач вводить із клавіатури два числа (початок і кінець діапазону).
# Потрібно проаналізувати всі числа в цьому діапазоні. Потрібно вивести на екран:
# Усі числа діапазону.
# Усі числа діапазону в спадному порядку.
# Усі числа, кратні 7.
# Кількість чисел, кратних 5.
try:
    start=int(input("Enter a first number: "))
    end=int(input("Enter a second number: "))
    print("------------All numbers in the range---------------")
    num=start
    while num<=end:
        print(num,end = " ")
        num+=1
    print("\n")
    print("---All numbers in the range in descending order----")
    num=end
    while num>=start:
        print(num,end = " ")
        num-=1
    print("\n")
    print("---------All numbers that are multiples of 7-------")
    num = start
    while num <= end:
        if num % 7 == 0:
            print(num,end = " ")
        num += 1
    print("\n")
    print("---------Count of numbers that are multiples of 5-------")
    num = start
    count = 0
    while num <= end:
        if num % 5 == 0:
            count += 1
        num+=1
    print(f"{count}")
except ValueError:
    print("Error")
# Завдання 3
# Користувач вводить із клавіатури два числа (початок і кінець діапазону).
# Потрібно проаналізувати всі числа в цьому діапазоні. Виведення на екран має відбуватися
# за правилами, зазначеними нижче.
# Якщо число кратне 3 (ділиться на 3 без залишку) потрібно вивести слово "Fizz".
# Якщо число кратне 5 потрібно вивести слово "Buzz". Якщо число кратне 3 і 5 потрібно вивести "Fizz Buzz".
# Якщо число не кратне не 3 і 5 потрібно вивести саме число.

try:
    start=int(input("Enter a first number: "))
    end=int(input("Enter a second number: "))
    num = start
    while num <= end:
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1
except ValueError:
    print("Error")
# Завдання 4
# Користувач вводить два числа і крок (інтервал), з яким потрібно проходити по діапазону.
# Програма має показати числа від початку діапазону до кінця, збільшуючи кожне число на вказаний крок.
# Також програма повинна надавати вибір порядку виведення: у прямому або зворотному порядку.
try:
    start=int(input("Enter a first number: "))
    end=int(input("Enter a second number: "))
    interval=int(input("Enter a interval: "))
    if interval <= 0:
        print("Interval must be greater than 0")
    else:
        choice = int(input("Enter a choice: 1 forward , 2 reverse input order "))
        if choice==1:
            print("Numbers in forward order:")
            num = start
            while num <= end:
                print(num, end=" ")
                num += interval
        elif choice==2:
            print("Numbers in reverse order:")
            num = end
            while num >= start:
                print(num, end=" ")
                num -= interval
        else:
            print("Error")
except ValueError:
    print("Error")
# Завдання 6
# Користувач вводить два числа: число A і ступінь N, у який потрібно піднести число.
# Програма повинна обчислити A у степені N за допомогою циклу (без використання вбудованих функцій піднесення до степеня).
try:
    a=int(input("Enter number A: "))
    n=int(input("Enter power N: "))
    if n < 0:
        print("Power must be non-negative")
    else:
        result = 1
        count = 0
        while count < n:
            result = result * a
            count = count + 1
        print(f"{a} ^ {n} = {result}")
except ValueError:
    print("Error")