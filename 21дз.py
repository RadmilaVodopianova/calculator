# Рівень 1
# Завдання 1
# Напишіть програму, яка відкриває файл data.txt і замінює в ньому всі входження слова "Python" на "Java", потім зберігає зміни в тому самому файлі.
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()
    text = text.replace("Python", "Java")
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print('Word "Python" replaced by  "Java".')
except FileNotFoundError:
    print("File data.txt not created.")
# Завдання 2
# Напишіть програму, яка відкриває файл data.txt, підраховує кількість символів у кожному рядку і записує результати в новий файл char_count.txt у форматі "Рядок X: Y символів".
try:
    with open("data.txt", "r", encoding="utf-8") as data_file:
        lines = data_file.readlines()
    with open("char_count.txt", "w", encoding="utf-8") as result_file:
        for number, line in enumerate(lines, start=1):
            line = line.rstrip("\n")
            character_count = len(line)
            result_file.write(f"Row  {number}: {character_count} symbols\n")
    print("Result in file  char_count.txt.")
except FileNotFoundError:
    print("File  data.txt not created.")
# Рівень 2
# Завдання 3
# Напишіть програму, яка порівнює два файли (old_version.txt і new_version.txt) і створює файл differences.txt, у якому вказуються рядки, присутні в одному файлі, але відсутні в іншому.
try:
    with open("old_version.txt", "r", encoding="utf-8") as old_file:
        old_lines = old_file.readlines()
    with open("new_version.txt", "r", encoding="utf-8") as new_file:
        new_lines = new_file.readlines()
    old_lines = [line.rstrip("\n") for line in old_lines]
    new_lines = [line.rstrip("\n") for line in new_lines]
    only_in_old = []
    for line in old_lines:
        if line not in new_lines:
            only_in_old.append(line)
    only_in_new = []
    for line in new_lines:
        if line not in old_lines:
            only_in_new.append(line)
    with open("differences.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Rows in  old_version.txt:\n")
        if only_in_old:
            for line in only_in_old:
                result_file.write(line + "\n")
        else:
            result_file.write("Row not found\n")
        result_file.write("\nRows in  new_version.txt:\n")
        if only_in_new:
            for line in only_in_new:
                result_file.write(line + "\n")
        else:
            result_file.write("Таких рядків немає.\n")

    print("Differences differences.txt.")
except FileNotFoundError:
    print("File not found.")
# Завдання 4
# Напишіть програму, яка зчитує два файли (source.txt і words.txt), замінює всі слова зі words.txt у source.txt на *** і зберігає результат у censored.txt.
try:
    with open("source.txt", "r", encoding="utf-8") as source_file:
        text = source_file.read()
    with open("words.txt", "r", encoding="utf-8") as words_file:
        words = words_file.readlines()
    for word in words:
        word = word.strip()
        if word:
            text = text.replace(word, "***")
    with open("censored.txt", "w", encoding="utf-8") as result_file:
        result_file.write(text)
    print("Result in  censored.txt.")
except FileNotFoundError:
    print("File source.txt or  words.txt not found")
# Рівень 3
# Завдання 5
# Напишіть програму, яка реалізує керування замовленнями інтернет-магазину за допомогою текстового файлу orders.txt. Програма повинна надавати користувачеві меню з можливими діями:
# Додати нове замовлення – користувач вводить номер замовлення, назву товару, кількість і ціну, після чого дані додаються у файл.
# Переглянути всі замовлення – програма завантажує і відображає всі замовлення, збережені у файлі.
# Пошук замовлення за номером – користувач вводить номер замовлення, програма виводить інформацію про нього.
# Оновити замовлення – користувач вводить номер замовлення, програма дає змогу оновити кількість і ціну товару.
# Видалити замовлення – користувач вводить номер замовлення, і програма видаляє його з файлу, якщо він існує.
# Вихід – завершує виконання програми.
# Рівень 3
# Завдання 5
# Керування замовленнями інтернет-магазину
file_name = "orders.txt"
def add_order():
    order_number = input("Enter order number: ")
    product = input("Enter product name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        if quantity <= 0 or price < 0:
            print("Quantity must be greater than 0 and price cannot be negative.")
            return
    except ValueError:
        print("Quantity must be a whole number and price must be a number.")
        return
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            orders = file.readlines()
        for order in orders:
            data = order.strip().split("|")
            if data[0] == order_number:
                print("An order with this number already exists.")
                return
    except FileNotFoundError:
        pass
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{order_number}|{product}|{quantity}|{price}\n")
    print("Order successfully added.")
def show_orders():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            orders = file.readlines()
        if not orders:
            print("The order list is empty.")
            return
        print("\nOrder list:")
        for order in orders:
            data = order.strip().split("|")
            print("-------------------------")
            print(f"Order number: {data[0]}")
            print(f"Product: {data[1]}")
            print(f"Quantity: {data[2]}")
            print(f"Price: {data[3]}")
    except FileNotFoundError:
        print("File orders.txt not found.")
def search_order():
    order_number = input("Enter order number: ")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            orders = file.readlines()
        for order in orders:
            data = order.strip().split("|")
            if data[0] == order_number:
                print("\nOrder found:")
                print(f"Order number: {data[0]}")
                print(f"Product: {data[1]}")
                print(f"Quantity: {data[2]}")
                print(f"Price: {data[3]}")
                return
        print("Order with this number was not found.")
    except FileNotFoundError:
        print("File orders.txt not found.")
def update_order():
    order_number = input("Enter order number to update: ")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            orders = file.readlines()
    except FileNotFoundError:
        print("File orders.txt not found.")
        return
    updated_orders = []
    order_found = False
    for order in orders:
        data = order.strip().split("|")
        if data[0] == order_number:
            print(f"Product: {data[1]}")
            try:
                new_quantity = int(input("Enter new quantity: "))
                new_price = float(input("Enter new price: "))
                if new_quantity <= 0 or new_price < 0:
                    print("Quantity must be greater than 0 and price cannot be negative.")
                    return
            except ValueError:
                print("Incorrect data entered.")
                return
            data[2] = str(new_quantity)
            data[3] = str(new_price)
            order_found = True
        updated_orders.append("|".join(data) + "\n")
    if order_found:
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(updated_orders)
        print("Order successfully updated.")
    else:
        print("Order with this number was not found.")
def delete_order():
    order_number = input("Enter order number to delete: ")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            orders = file.readlines()
    except FileNotFoundError:
        print("File orders.txt not found.")
        return
    remaining_orders = []
    order_found = False
    for order in orders:
        data = order.strip().split("|")
        if data[0] == order_number:
            order_found = True
        else:
            remaining_orders.append(order)
    if order_found:
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(remaining_orders)
        print("Order successfully deleted.")
    else:
        print("Order with this number was not found.")
def main():
    while True:
        print("\nMenu")
        print("1. Add new order")
        print("2. Show all orders")
        print("3. Search order")
        print("4. Update order")
        print("5. Delete order")
        print("6. Exit")
        choice = input("Choose an action: ")
        match choice:
            case "1":
                add_order()
            case "2":
                show_orders()
            case "3":
                search_order()
            case "4":
                update_order()
            case "5":
                delete_order()
            case "6":
                print("Program finished.")
                break
            case _:
                print("Invalid choice.")
main()