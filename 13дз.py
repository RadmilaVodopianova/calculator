# Рівень 1
# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно визначити кількість елементів у списку, які більші за
# попередній елемент. Результат вивести на екран.
# Приклад:
# Вхідні дані:
# Список чисел: 1, 3, 2, 4, 5.
# Очікуваний результат:
# Кількість елементів: 3.
# (Пояснення: 3 > 1, 4 > 2, 5 > 4).
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1
print(f"Кількість елементів: {count}")
# Завдання 2
# Користувач вводить список цілих чисел. Необхідно вивести тільки ті елементи, які зустрічаються у списку рівно один раз,
# зберігаючи порядок їхньої появи.
# Приклад:
# Вхідні дані: 1, 2, 2, 3, 4, 4, 5.
# Очікуваний результат: [1, 3, 5].
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
result = []
for num in numbers:
    if numbers.count(num) == 1:
        result.append(num)
print(result)
# Рівень 2
# Завдання 3
# Користувач з клавіатури вводить список чисел. Необхідно знайти у списку найдовшу послідовність елементів, що зростають,
# і вивести її довжину та самі елементи.
# Приклад:
# Вхідні дані:
# Список чисел: 1, 2, 1, 2, 3, 4, 1.
# Очікуваний результат:
# Довжина послідовності: 4.
# Послідовність: [1, 2, 3, 4].
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
current = [numbers[0]]
longest = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current.append(numbers[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [numbers[i]]
if len(current) > len(longest):
    longest = current
print(f"Довжина послідовності: {len(longest)}")
print(f"Послідовність: {longest}")
# Завдання 4
# Користувач із клавіатури вводить список цілих чисел. Необхідно реалізувати циклічний зсув списку вправо на N позицій.
# Результат вивести на екран.
# Приклад:
# Вхідні дані:
# Список чисел: 1, 2, 3, 4, 5.
# Число позицій N: 2.
# Очікуваний результат:
# Зсунутий список: [4, 5, 1, 2, 3].
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    numbers.append(num)
n = int(input("Enter N: "))
n = n % len(numbers)
numbers = numbers[-n:] + numbers[:-n]
print(numbers)

