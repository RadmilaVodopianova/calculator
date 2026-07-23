# Завдання 4
# На картці є 5000 грн.
# Користувач вводить суму зняття.
# Програма повинна:
#  порахувати залишок після зняття;
#  якщо грошей недостатньо → "Недостатньо коштів";
#  якщо введено текст → "Потрібно вводити тільки число";
#  якщо сума ≤ 0 → "Неправильна сума".

money = 5000
try:
    withdrawal = float(input("Enter your withdrawal amount: "))
    if withdrawal > money:
        print("Недостатньо коштів")
    elif  withdrawal <= 0:
        print("Неправильна сума")
    else:
        print(f"Remaining balance is {money - withdrawal}")
except ValueError:
    print("Потрібно вводити тільки число")







