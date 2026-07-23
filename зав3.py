# Користувач вводить число, що представляє оцінку за шкалою від 1 до 5. Програма
# повинна вивести текстову інтерпретацію оцінки:
# 1. Дуже погано.
# 2. Погано.
# 3. Задовільно.
# 4. Добре.
# 5. Відмінно.

grade=int(input("Enter your grade-"))
if grade ==1:
    print("Very bad!")
elif grade ==2:
    print("Bad!")
elif grade ==3:
    print("Satisfactory!")
elif grade ==4:
    print("Good!")
elif grade ==5:
    print("Very good!")
else:
    print("There is no rating!")