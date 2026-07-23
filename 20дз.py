# Рівень 1
# Завдання 1
# Напишіть програму, яка запитує в користувача три рядки і записує їх у файл data.txt, кожен рядок має бути записаний на новому рядку.
line1 = input("Enter first row: ")
line2 = input("Enter second row: ")
line3 = input("Enter third row: ")
data_txt= open("data.txt", "w", encoding="utf-8")
data_txt.write(line1 + "\n")
data_txt.write(line2 + "\n")
data_txt.write(line3 + "\n")
print("The rows were successfully recorded in the file data.txt")
data_txt.close()
# Завдання 2
# Напишіть програму, яка перевіряє, чи існує файл data.txt, і виводить відповідне повідомлення. Якщо файл існує, відкрийте його і виведіть кожен другий рядок у консоль.
try:
    data_txt = open("data.txt", "r", encoding="utf-8")
    print("File data.txt ")
    lines = data_txt.readlines()
    for i in range(1, len(lines), 2):
        print(lines[i], end="")
    data_txt.close()
except FileNotFoundError:
    print("File data.txt do not exist")
# Рівень 2
# Завдання 3
# Напишіть програму, яка читає файл data.txt, фільтрує рядки, що містять слово "Python", і записує їх у новий файл filtered.txt.
data_txt = open("data.txt", "r", encoding="utf-8")
filtered_txt = open("filtered.txt", "w", encoding="utf-8")
for line in data_txt:
    if "Python" in line:
        filtered_txt.write(line)
data_txt.close()
filtered_txt.close()
print("Rows with the word Python written in file  filtered.txt")
# Завдання 4
# Напишіть програму, яка запитує в користувача ім'я файлу, відкриває його, видаляє всі цифри з вмісту і зберігає результат у новому файлі cleaned.txt.
file_name = input("Enter file name: ")
try:
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    file.close()
    cleaned_text = ""
    for symbol in text:
        if not symbol.isdigit():
            cleaned_text += symbol
    cleaned_file = open("cleaned.txt", "w", encoding="utf-8")
    cleaned_file.write(cleaned_text)
    cleaned_file.close()
    print("Result saved in cleaned.txt")
except FileNotFoundError:
    print("File does not exist")
# Рівень 3
# Завдання 5
# Напишіть програму, яка аналізує файл log.txt, визначає 10 найпоширеніших слів, що зустрічаються найчастіше, і записує їх разом з їхньою частотою в word_stats.txt.
log_file = open("log.txt", "r", encoding="utf-8")
text = log_file.read()
log_file.close()
text = text.lower()
symbols = ".,!?;:()[]{}\"'"
for symbol in symbols:
    text = text.replace(symbol, " ")
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_words = sorted(
    word_counts.items(),
    key=lambda item: item[1],
    reverse=True
)
stats_file = open("word_stats.txt", "w", encoding="utf-8")
for word, count in sorted_words[:10]:
    stats_file.write(word + " — " + str(count) + "\n")
stats_file.close()
print("Statistics recorded in file word_stats.txt")
