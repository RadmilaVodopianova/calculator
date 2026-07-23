# Завдання 1
# Написати програму, яка:
# 1. Запитує у користувача число.
# 2. Запитує степінь, у який потрібно піднести це число (від 0 до 7 включно).
# 3. Якщо користувач ввів правильний степінь — програма виводить результат.
# 4. Якщо степінь менший за 0 або більший за 7 — вивести повідомлення про помилку.

try:
    num=int(input("Enter a number: "))
    exponentiation= int(input("Enter a exponential number: "))
    if  0 <= exponentiation <= 7:
        print(f"Result: {num ** exponentiation}")
    else:
        print(f"Exponent must be between 0 and 7")
except ValueError:
    print("must be numbers")
except Exception as ex:
    print (ex)

# Завдання 2
# Написати програму підрахунку вартості розмови для різних мобільних операторів.
# Користувач вводить вартість розмови і вибирає з якого на який оператор він
# телефонує. Вивести вартість на екран.

try:
    minutes = float(input("Enter call duration in minutes: "))
    print("Choose your operator:")
    print("1 - Kyivstar")
    print("2 - Vodafone")
    print("3 - Lifecell")
    choice = int(input("Enter your choice: "))
    print("Choose call type:")
    print("1 - Inside your operator")
    print("2 - To another operator")
    call_choice = int(input("Enter your choice: "))
    if choice == 1:
        inside = 0
        outside = 3
    elif choice == 2:
        inside = 0.5
        outside = 2.5
    elif choice == 3:
        inside = 0.75
        outside = 2
    else:
        print("Wrong operator")
    if call_choice == 1:
        cost = minutes * inside
        print(f"Call cost: {cost} UAH")
    elif call_choice == 2:
        cost = minutes * outside
        print(f"Call cost: {cost} UAH")
    else:
        print("Wrong call type")
except ValueError:
    print("Enter numbers only")
except Exception as ex:
    print(ex)

# Завдання 3
# Користувач вводить із клавіатури число в діапазоні від 1 до 100. Якщо число
# кратне 3 (ділиться на 3 без залишку) потрібно вивести слово Fizz. Якщо число
# кратне 5 потрібно вивести слово Buzz. Якщо число кратне 3 і 5 потрібно
# вивести Fizz Buzz. Якщо число не кратне не 3 і 5 потрібно вивести саме число.
# Якщо користувач ввів значення не в діапазоні від 1 до 100 потрібно вивести
# повідомлення про помилку.

try:
    number = int(input("Enter a number (1-100): "))
    if number < 1 or number > 100:
        print("Error: number must be between 1 and 100")
    elif number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
except ValueError:
    print("Error: you must enter an integer")
except Exception as ex:
    print(ex)

# Завдання 4
# Зарплата менеджера становить 200$ + відсоток від продажів, продажі до 500$ – 3%,
# від 500 до 1000 – 5%, понад 1000 – 8%. Користувач вводить із клавіатури рівень
# продажів для трьох менеджерів. Визначити їхню зарплату, визначити найкращого
# менеджера, нарахувати йому премію 200$, вивести підсумки на екран.

try:
    base_salary = 200
    sales1 = float(input("Enter sales for Manager 1: "))
    sales2 = float(input("Enter sales for Manager 2: "))
    sales3 = float(input("Enter sales for Manager 3: "))
    if sales1 < 500:
        salary1 = base_salary + sales1 * 0.03
    elif sales1 <= 1000:
        salary1 = base_salary + sales1 * 0.05
    else:
        salary1 = base_salary + sales1 * 0.08
    if sales2 < 500:
        salary2 = base_salary + sales2 * 0.03
    elif sales2 <= 1000:
        salary2 = base_salary + sales2 * 0.05
    else:
        salary2 = base_salary + sales2 * 0.08
    if sales3 < 500:
        salary3 = base_salary + sales3 * 0.03
    elif sales3 <= 1000:
        salary3 = base_salary + sales3 * 0.05
    else:
        salary3 = base_salary + sales3 * 0.08
    if salary1 >= salary2 and salary1 >= salary3:
        best = "Manager 1"
        final_salary = salary1 + 200
    elif salary2 >= salary1 and salary2 >= salary3:
        best = "Manager 2"
        final_salary = salary2 + 200
    else:
        best = "Manager 3"
        final_salary = salary3 + 200
    print(f"Manager 1 salary: {salary1} $")
    print(f"Manager 2 salary: {salary2} $")
    print(f"Manager 3 salary: {salary3} $")
    print(f"Best manager: {best}, final salary with bonus = {final_salary} $")
except ValueError:
    print("Error: you must enter numbers only")
except Exception as ex:
    print(ex)

# Завдання 5
# Користувач вводить суму кредиту і термін (у роках). Програма визначає процентну
# ставку і розраховує загальну суму до виплати:
#  Для кредиту до 10 000$ на строк до 3 років – ставка 8%.
#  Для кредиту до 10 000$ на строк понад 3 роки – ставка 10%.
#  Для кредиту від 10 001$ до 50 000$ на строк до 3 років – ставка 12%.
#  Для кредиту від 10 001$ до 50 000$ на строк понад 3 роки – ставка 15%.
#  Для кредиту понад 50 000$ на будь-який термін – ставка 20%.
# Програма виводить підсумкову суму до виплати і щомісячний платіж.

try:
    credit = float(input("Enter loan amount ($): "))
    years = int(input("Enter loan term (years): "))
    if credit <= 10000 and years <= 3:
        rate = 0.08
    elif credit <= 10000 and years > 3:
        rate = 0.10
    elif 10001 <= credit <= 50000 and years <= 3:
        rate = 0.12
    elif 10001 <= credit <= 50000 and years > 3:
        rate = 0.15
    else:
        rate = 0.20
    total = credit + credit * rate * years
    monthly = total / (years * 12)
    print(f"Loan amount: {credit} $")
    print(f"Term: {years} years")
    print(f"Interest rate: {rate*100}%")
    print(f"Total amount to pay: {total} $")
    print(f"Monthly payment: {monthly} $")
except ValueError:
    print("Error: enter numbers only")
except Exception as ex:
    print(ex)

# Завдання 6
# Ви розробляєте програму для розрахунку вартості комплексного обіду в ресторані.
# Меню складається з трьох категорій: закуска, основна страва і десерт. Залежно від
# вибору клієнта і його статусу програма повинна розрахувати підсумкову вартість з
# урахуванням можливих знижок і спеціальних пропозицій.
# 1. Меню комплексного обіду.
#  Закуски:
# o Салат – 5$,
# o Суп – 7$.
#  Основні страви:
# o Курка – 10$,
# o Риба – 12$.
#  Десерти:
# o Морозиво – 3$,
# o Фрукти – 4$.
# Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт), надається
# знижка 10% на все замовлення.
#  Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
#  Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з іншими
# знижками.
# 3. Спеціальні пропозиції.
#  Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
#  Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається безкоштовний
# напій (наприклад, "Чай").
# 4. Підсумкова вартість.
#  Програма повинна коректно застосувати всі знижки та спеціальні пропозиції, а потім
# розрахувати підсумкову вартість замовлення.

try:
    print("------------ Appetizers ------------")
    print("1 - Salad - 5$")
    print("2 - Soup - 7$")
    appetizer = int(input("Choose appetizer: "))
    print("------------ Main dishes ------------")
    print("1 - Chicken - 10$")
    print("2 - Fish - 12$")
    main = int(input("Choose main dish: "))
    print("------------ Desserts ------------")
    print("1 - Ice cream - 3$")
    print("2 - Fruits - 4$")
    dessert = int(input("Choose dessert: "))
    regular = int(input("Regular customer? 1-Yes 2-No: "))
    total = 0
    if appetizer == 1:
        appetizer_name = "Salad"
        total = total + 5
    elif appetizer == 2:
        appetizer_name = "Soup"
        total = total + 7
    else:
        raise Exception("Wrong appetizer choice")
    if main == 1:
        main_name = "Chicken"
        total = total + 10
    elif main == 2:
        main_name = "Fish"
        total = total + 12
    else:
        raise Exception("Wrong main dish choice")
    if dessert == 1:
        dessert_name = "Ice cream"
        dessert_price = 3
    elif dessert == 2:
        dessert_name = "Fruits"
        dessert_price = 4
    else:
        raise Exception("Wrong dessert choice")
    if appetizer_name == "Soup" and main_name == "Fish":
        dessert_price = dessert_price - 2
        print("Special offer: 2$ discount on dessert")
    total = total + dessert_price
    discount = 0
    if total > 20:
        discount = discount + 15
    else:
        discount = discount + 10
    if regular == 1:
        discount = discount + 5
    elif regular == 2:
        discount = discount + 0
    else:
        raise Exception("Wrong customer choice")
    if main_name == "Chicken" and dessert_name == "Ice cream":
        print("Special offer: free Cola")
    final_total = total - total * discount / 100
    print("------------ Result ------------")
    print(f"Appetizer: {appetizer_name}")
    print(f"Main dish: {main_name}")
    print(f"Dessert: {dessert_name}")
    print(f"Total before discount: {total} $")
    print(f"Discount: {discount}%")
    print(f"Final total: {final_total} $")
except ValueError:
    print("Enter numbers only")
except Exception as ex:
    print(ex)