# Є секретний код. Користувач вводить код.
# Якщо код правильний — сейф відкрито.
# Якщо ні — помилка.
# Якщо ввели текст — обробити виняток.
from itertools import product

# secret_code = "1111"
# try:
#     user_code = int(input("Enter code: "))
#     if user_code == secret_code:
#         print("Open")
#     else:
#         print("Wrong code")
# except ValueError:
#     print("Error code must be integer")
# except Exception as ex:
#     print(ex)






# Ціна квитка — 150 грн.
# Користувач вводить вік і кількість квитків.
# до 12 років — знижка 50%;
# від 60 років — знижка 30%;
# інші — без знижки.

# try:
#     price = 150
#     age=int(input("Enter your age: "))
#     quantity = int(input("How many people are you in  "))
#     if age<=0 or quantity<=0:
#         print("Age and quantity must be more than 0")
#     else:
#         total_price = price * quantity
#         if age <=12:
#             total_price = total_price-total_price*0.5
#             print(f"Price ticket {total_price}")
#         elif age>=60:
#             total_price = total_price - total_price * 0.3
#             print(f"Price ticket {total_price}")
#         else:
#             print(f"Price ticket {total_price}")
# except ValueError:
#     print("Please enter a number")
# except Exception as ex:
#     print(ex)


# Є секретне число. Користувач вводить число.
# Програма підказує: більше, менше або перемога.

# try:
#     secret=9
#     number=int(input("Enter your number: "))
#     if number < secret:
#         print("More than your number")
#     elif number > secret:
#         print("Less than your number")
#     else:
#         print("Win")
# except ValueError:
#     print("Please enter a number")
# except Exception as ex:
#     print(ex)

# Користувач вводить суму в гривнях.
# Програма переводить її в долари.
# try:
#     uan=int(input("Enter your summ in uan: "))
#     dollars=uan/44
#     print(f"Dollars is {dollars:.2f}")
#     if uan<=0:
#         print("Please enter a positive number")
# except ValueError:
#     print("Please enter a number")
# except Exception as ex:
#     print(ex)




# Є правильний логін і пароль.
# Користувач вводить свої дані.
# try:
#     login = "lol"
#     password = "1234"
#     user_login = input("Enter your login : ")
#     user_password = input("Enter your password: ")
#     if login == user_login and password == user_password:
#         print("Successful")
#     else:
#         print("Wrong login or password")
# except Exception as ex:
#     print(ex)


# print("---------------- Menu ---------------------")
# print("1)Молоко - 50 грн")
# print("2)Хліб - 30 грн")
# print("3)Сік - 70 грн")
# try:
#     choice = int(input("Оберіть товар - "))
#     quantity = int(input("Введіть кількість - "))
#     if quantity <= 0 or choice <= 0:
#         raise Exception("Quantity and choice must be > 0")
#     else:
#         if choice == 1:
#             product = "Молоко"
#             price = 50
#         elif choice == 2:
#             product = "Хліб"
#             price = 30
#         elif choice == 3:
#             product = "Сік"
#             price = 70
#         else:
#             product = ""
#             price = 0
#             print("Такого товару немає!")
#         if price > 0:
#             total = price * quantity
#             if total >= 300:
#                 total = total * 0.9
#                 print("Знижка 10%!")
#                 money = int(input("Введіть суму оплати - "))
#                 if money >= total:
#                     change = money - total
#                     print(f"Product {product}")
#                     print(f"До сплати {total}")
#                     print(f"Решта {change}")
#                 else:
#                     print("Недостатньо коштів !")
# except ValueError:
#     print("Enter a number !")
# except Exception as ex:
#     print(ex)


print("---------------- Menu ---------------------")
print("1) Appetizer - 290 uan")
print("2) Soup - 350 uan")
print("3) Main - 550 uan")

try:
    choice = int(input("Choose a dish: "))
    quantity = int(input("Enter quantity: "))

    if quantity <= 0 or choice <= 0:
        raise Exception("Quantity and choice must be > 0")

    if choice == 1:
        product = "Appetizer"
        price = 290
    elif choice == 2:
        product = "Soup"
        price = 350
    elif choice == 3:
        product = "Main"
        price = 550
    else:
        raise Exception("No choice")

    total = price * quantity

    if total > 1000:
        total = total * 0.9
        print("Discount 10%")

    money = int(input("Enter your money: "))

    if money >= total:
        change = money - total
        print(f"Product: {product}")
        print(f"For pay: {total}")
        print(f"Rest: {change}")
    else:
        print("Not enough money")

except ValueError:
    print("Enter a number!")
except Exception as ex:
    print(ex)

# логін;
# пароль;
# вік.
# логін не має бути порожнім;
# пароль мінімум 4 символи;
# вік має бути більше 0;
# якщо вік менше 13 — реєстрація заборонена.


login = input("Enter login: ")
password = input("Enter password: ")

try:
    age = int(input("Enter age: "))

    if login == "":
        print("Login cannot be empty")

    elif len(password) >= 4:

        if age <= 0:
            print("Age must be more than 0")

        elif age < 13:
            print("Registration is forbidden")

        else:
            print("Registration successful")

    else:
        print("Password must be at least 4 characters")

except ValueError:
    print("Age must be a number")