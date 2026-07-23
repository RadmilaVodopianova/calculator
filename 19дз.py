# Завдання 1
# Є словник: capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}
# Виведи усі ключі (назви країн).
# Виведи усі значення (столиці).
# Додай до словника ще одну країну.
capitals = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Німеччина": "Берлін"
}
print("Країни:")
for country in capitals.keys():
    print(country)
print("Столиці:")
for capital in capitals.values():
    print(capital)
capitals["Франція"] = "Париж"
print(capitals)
# Завдання 2
# Створи словник prices, де зберігаються товари і їхня ціна:
# {"яблуко": 15, "банан": 20, "груша": 18}
# Попроси користувача ввести назву товару і виведи його ціну.
# Якщо товару немає — повідом: Такого товару немає в магазині.
prices = {
    "яблуко": 15,
    "банан": 20,
    "груша": 18
}
product = input("Введіть назву товару: ")
if product in prices:
    print("Ціна:", prices[product])
else:
    print("Такого товару немає в магазині.")
# Завдання 3
# Створіть програму «Фірма», яка зберігає інформацію про працівників: ПІБ, телефон, корпоративний email, назва посади,
# номер кабінету, Skype. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник
# для збереження інформації.
# Завдання 3
firm = {}
while True:
    print("\n1 - Додати працівника")
    print("2 - Видалити працівника")
    print("3 - Знайти працівника")
    print("4 - Змінити дані")
    print("5 - Показати всіх")
    print("0 - Вийти")
    choice = input("Ваш вибір: ")
    if choice == "1":
        pib = input("ПІБ: ")
        firm[pib] = {
            "phone": input("Телефон: "),
            "email": input("Корпоративний email: "),
            "position": input("Посада: "),
            "cabinet": input("Номер кабінету: "),
            "skype": input("Skype: ")
        }
        print("Працівника додано.")
    elif choice == "2":
        pib = input("Введіть ПІБ працівника: ")
        if pib in firm:
            del firm[pib]
            print("Працівника видалено.")
        else:
            print("Працівника не знайдено.")
    elif choice == "3":
        pib = input("Введіть ПІБ працівника: ")
        if pib in firm:
            for key, value in firm[pib].items():
                print(key, ":", value)
        else:
            print("Працівника не знайдено.")
    elif choice == "4":
        pib = input("Введіть ПІБ працівника: ")
        if pib in firm:
            field = input("Що змінити? phone/email/position/cabinet/skype: ")
            if field in firm[pib]:
                firm[pib][field] = input("Нове значення: ")
                print("Дані змінено.")
            else:
                print("Такого поля немає.")
        else:
            print("Працівника не знайдено.")
    elif choice == "5":
        for pib, info in firm.items():
            print("\nПрацівник:", pib)
            for key, value in info.items():
                print(key, ":", value)
    elif choice == "0":
        break
    else:
        print("Error")
# Завдання 4
# Напишіть функцію, яка об'єднує два словники. Якщо у них є спільні ключі, значення повинні складатися.
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
a = {"x": 10, "y": 20}
b = {"y": 5, "z": 30}
print(merge_dicts(a, b))
# Завдання 5: Підрахунок кількості слів у тексті
# Напишіть програму, яка підраховує кількість кожного слова у введеному тексті та зберігає цю інформацію в словнику.
# Завдання 5
text = input("Enter text: ")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)