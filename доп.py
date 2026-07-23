# Користувач вводить два числа і вибирає операцію (додавання, віднімання,
# множення, ділення, знаходження залишку, піднесення до степеня). Програма
# повинна виконати вибрану операцію і вивести результат.

num1 = int(input("Enter first number -"))
num2 = int(input("Enter second number -"))
choice=int(input("Enter your choice: 1 - summ , 2- subtraction , 3- multiplication , 4- division , 5- remainder ,6 -exponentiation" ))
if choice == 1:
    print(f"Summ = {num1+num2}")
elif choice == 2:
    print(f"Subtraction = {num1-num2}")
elif choice == 3:
    print(f"Multiplication = {num1*num2}")
elif choice == 4:
    print(f"Division = {num1/num2}")
elif choice == 5:
    print(f"Remainder = {num1%num2}")
elif choice == 6:
    print(f"Exponentiation = {num1**num2}")

# Користувач вводить тризначне число.Програма повинна визначити, чи всі цифри
# числа однакові.Якщо всі цифри однакові, вивести «Всі цифри однакові», інакше —  «Цифри різні».

num=int(input("Enter number - "))
num1 = num//100
num2 = (num//10) % 10
num3 = num%10
if num1 == num2 == num3:
    print("All numbers are the same")
else:
    print("The numbers are different")

# Користувач вводить суму покупки і свій вік. Програма обчислює знижку:
# Якщо вік менше 18, знижка 10%.
#  Від 18 до 60 років — знижка 5%.
#  Якщо вік більше 60 років — знижка 15%.
# Програма виводить підсумкову суму з урахуванням знижки.

age=int(input("Enter your age - "))
total_amount=float(input("Enter total amount - "))
if age<18:
    print(f"Discounted total {total_amount*0.9}")
elif 18 <= age <= 60:
    print(f"Discounted total {total_amount*0.95}")
elif  age> 60:
    print(f"Discounted total {total_amount*0.85}")



