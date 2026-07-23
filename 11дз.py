# Завдання 1
# Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат.
text = "Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат."
count = text.count(".") + text.count("!") + text.count("?")
print(count)

# Завдання 2
# Користувач вводить з клавіатури рядок. Перевірте чи є введений рядок паліндромом. Паліндром — слово або текст, що
# читається однаково зліва направо і справа наліво. Наприклад:
# Кок;
# Козак з казок;
# Радар;
# А мене нема.

text = input("Enter your text: ")
text = text.lower().replace(" ", "")
if text == text[::-1]:
    print("Паліндром")
else:
    print("Не паліндром")
# Завдання 3
# Користувач вводить з клавіатури деякий текст. У програмі визначено набір зарезервованих слів. Необхідно знайти в
# тексті всі зарезервовані слова і змінити їхній регістр на верхній. Вивести на екран змінений текст.

text = input("Enter your text: ")
text = text.replace("if", "if".upper())
text = text.replace("else", "else".upper())
text = text.replace("for", "for".upper())
text = text.replace("while", "while".upper())
print(text)


# Завдання 4
# Користувач вводить рядок і два символи. Видаліть із рядка всі символи між першим входженням першого символу і
# першим входженням другого символу, включаючи самі символи. Виведіть результат.
text = input("Enter your text: ")
symbol1 = input("Enter first symbol: ")
symbol2 = input("Enter second symbol: ")
start = text.find(symbol1)
end = text.find(symbol2)
if start == -1 or end == -1 or start > end:
    print("Symbol not found")
else:
    result = text[:start] + text[end + 1:]
    print(result)
# Завдання 5
# Користувач вводить текст і набір символів. Видаліть з тексту всі слова, що містять хоча б один з цих символів, і
# виведіть результат.
text = input("Enter text: ")
symbols = input("Enter symbols: ")
word = ""
result = ""
for letter in text + " ":
    if letter != " ":
        word += letter
    else:
        delete_word = False
        for s in symbols:
            if s in word:
                delete_word = True
        if delete_word == False:
            result += word + " "
        word = ""
print(result)

# Завдання 6
# Створіть програму, яка із введеного тексту створює "зворотний текст" (перевертає текст на рівні слів, а не символів).
# Наприклад, "я люблю Python" перетворюється на "Python люблю я".
text = input("Enter text: ")
word = ""
result = ""
for letter in text + " ":
    if letter != " ":
        word += letter
    else:
        result = word + " " + result
        word = ""
print(result)

