# try:
#     amount = int(input("Enter amount - "))
#     items_type = input("Enter item type - ")
#
#     parts_number = int(input("Enter parts number - "))
#     parts_amount = amount / parts_number
#     print(f"We got {amount}{items_type}")
#     print(f"Parts amount of product {parts_amount}")
# except ValueError:
#     print("Amount should be an integer")
# except ZeroDivisionError:
#     print("Number parts can't be zero")
# except Exception as ex:
#     print(f"We have erorr - ", ex )
# finally:
#     print(" The program has finished")


# try:
#     age = int(input("Enter age - "))
#     if age < 0:
#         raise ValueError
#
# except Exception:
#     print("Age must be > 0 !")
# else:
#     print("Your age is ok")



# Створіть програму для розрахунку фінальної ціни товару.
# Запитайте в користувача введення вихідної ціни та відсотка знижки.
# Оберніть перетворення введених даних і обчислення підсумкової ціни в
# блок try.Якщо відбувається помилка перетворення (наприклад, ValueError),
# перехопіть її в блоці except і виведіть повідомлення про помилку.
# У блоці finally (за необхідності) виведіть повідомлення про завершення
# обчислень

# try:
#     price = float(input("Enter price: "))
#     discount = float(input("Enter discount: "))
#
#     print(f"{price - (price/100*discount)}")
# except ValueError:
#     print("We have error")
# else:
#     print("We don't have error")
# finally:
#     print(" we finished")

# Розробіть додаток, який запитує суму в доларах і курс обміну на євро,
# потім обчислює суму в євро.Помістіть перетворення вхідних даних і обчислення
# результату в блок try.Перехопіть ValueError для некоректного введення.
# Якщо курс обміну дорівнює нулю, до обчислень перевірте цю умову або згенеруйте
# виняток (наприклад, raise Exception("Курс обміну не може дорівнювати нулю")).
# У блоці finally виведіть повідомлення про завершення операції

# try:
#     dollar = float(input("Enter summ in dollars: - "))
#     rate = float(input("Enter currency rate in euro- "))
#     if rate ==0:
#         raise Exception ("Currency rate cannot be 0")
#     print(f" Your summ in euro is {dollar}*{rate} = {dollar * rate} EUR")
# except ValueError:
#     print(" Summ and currency must be numeric value")
# except Exception as ex:
#     print(ex)
# finally:
#     print("finish")

# Симулюйте роботу банкомату, де у користувача запитується сума для зняття.
# У блоці try отримайте суму, перетворіть її на число і перевірте, що сума кратна 10 і не перевищує заданий баланс (наприклад, 1000).
# Перехопіть ValueError, якщо введення некоректне.
# Якщо сума не відповідає вимогам, за допомогою raise згенеруйте виняток (наприклад, raise Exception("Некоректна сума для зняття")) і перехопіть його в блоці except.
# У блоці finally виведіть повідомлення про завершення транзакції


balance = 1000
try:
    amount = int(input( "Enter amount"))
    if amount % 10 !=0 or amount > balance:
        raise Exception("Invalid amount")
    balance-=amount
    print(" Money withdrawn:", amount)
    print("Remain:", balance)
except ValueError:
    print("Invalid amount")
except Exception as ex:
    print(ex)
except Exception as ex:
    print(ex)



