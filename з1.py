# Користувач вводить з клавіатури три цифри. Створіть число, яке містить ці
# цифри. Наприклад, якщо з клавіатури введено 1, 5, 7, ви маєте сформувати
# число 157.

num1 = int(input("Enter first number -"))
num2 = int(input("Enter second number -"))
num3 = int(input("Enter third number -"))
print(f"{(num1*100)+(num2*10)+(num3)}")