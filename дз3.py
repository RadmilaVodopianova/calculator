# Завдання 3
# Калькулятор
# Користувач вводить:
#  перше число;
#  друге число;
#  дію (+, -, *, /).
# Програма повинна:
#  виконати обчислення;
#  якщо введено текст замість числа → повідомлення про помилку;
#  якщо операція неправильна → "Невідома операція";
#  якщо ділення на 0 → "На нуль ділити не можна".

try:
    num1 = float(input("Enter first number - "))
    num2 = float(input("Enter second number - "))
    choice = input("Enter your choice:+, -, *, / : :")
    if choice == "+":
        print(f"Summ  {num1} + {num2}  = {num1+num2}")
    elif choice == "-":
        print(f"Subtraction {num1} - {num2} = {num1-num2}")
    elif choice == "*":
        print(f"Multiplication {num1} * {num2} = {num1*num2}")
    elif choice == "/":
         print(f"Division {num1} / {num2} = {num1/num2}")
    else:
        print("Невідома операція")
except ZeroDivisionError:
    print("На нуль ділити не можна")
except ValueError:
    print("Error")


