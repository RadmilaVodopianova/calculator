# Користувач вводить з клавіатури три числа. Залежно від вибору користувача
# програма виводить на екран максимум із трьох, мінімум із трьох або
# середньоарифметичне трьох чисел.

num1 = int(input("Enter first number -"))
num2 = int(input("Enter second number -"))
num3 = int(input("Enter third number -"))
choice=int(input("Enter your choice 1 - max, 2 - min, 3 - arithmetic "))
if choice == 1:
    if num1>num2 and num1>num3:
        print(f"Maximum {num1}")
    elif num2>num1 and num2>num3:
        print(f"Maximum {num2}")
    else:
        print(f"Maximum {num3}")
if choice == 2:
    if num1<num2 and num1<num3:
        print(f"Minimum {num1}")
    elif num2<num1 and num2<num3:
        print(f"Minimum {num2}")
    else:
        print(f"Minimum {num3}")
if choice == 3:
    print(f"Arithmetic {( num1 + num2 + num3) / 3}")
