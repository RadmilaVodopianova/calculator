# Завдання 2
# Користувач вводить 3 оцінки.
# Програма повинна:
#  порахувати середній бал;
#  якщо введено текст → "Оцінка має бути числом";
#  якщо оцінка не від 1 до 12 → "Неправильна оцінка".

try:
    mark1 = float(input("Enter mark 1 - "))
    mark2 = float(input("Enter mark 2 - "))
    mark3 = float(input("Enter mark 3 - "))
    if mark1 < 1 or mark1 > 12:
        print("Неправильна оцінка")
    elif mark2 < 1 or mark2 > 12:
        print("Неправильна оцінка")
    elif mark3 < 1 or mark3 > 12:
        print("Неправильна оцінка")
    else:
        print(f"GPA is {(mark1 + mark2 + mark3) / 3}")
except ValueError:
    print("Оцінка має бути числом")





