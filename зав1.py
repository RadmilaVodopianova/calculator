# Користувач вводить з клавіатури три числа. Залежно від вибору користувача
# програма виводить на екран суму трьох чисел або добуток трьох чисел.


num1 = int(input("Enter first number -"))
num2 = int(input("Enter second number -"))
num3 = int(input("Enter third number -"))
choice=int(input("Enter your choice: 1 - summ , 2- multiplication" ))
if choice == 1:
    summ=num1+num2+num3
    print(f"Summ = {summ}")
if choice == 2:
    multiplication=num1*num2*num3
    print(f"Multiplication = {multiplication}")
