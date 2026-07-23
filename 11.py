# "python"
# 'a'
# text="""some text"""
# print(type(text))
# print(text)
# print(id(text))
# text="python"
# print(id(text))
#
# print(text[0])
# print(text[1])
# print(text[-1])
# print(len(text))
#
# str1="hello"
# str2="world"
# print(str1+str2)
# print(str1*3)
#
# str3=str1+str2
# print(str3[0:5])
# print(str3[5:])
# print(str3[:len(str3)//2])
# Користувач вводить рядок. Виведіть його у зворотному
# порядку, використовуючи зріз.
# text=input("Enter a text: ")
# print(text[::-1])
# Завдання 2. Перші та останні символи
# Користувач вводить рядок. Виведіть:
# перший символ;
# останній символ;
# перші три символи;
# останні три символи.
# text=input("Enter a text: ")
# print(text[0])
# print(text[-1])
# print(text[:3])
# print(text[-3:])
# Завдання 3. Парні та непарні символи
# Користувач вводить рядок.
# Виведіть:
# усі символи з парними індексами;
# усі символи з непарними індексами.
# text=input("Enter a text: ")
# print(text[::2])
# print(text[1::2])


# new_str="PYthon"
# print(new_str.lower())
# print(new_str.upper())
# print(new_str.capitalize())
# print(new_str.title())
# print(new_str.swapcase())
# print(new_str)
#
# print(new_str.count("n"))
# print(new_str.find("n"))
# print(new_str.find("n",3,10))
# print(new_str.rfind("n"))
# print(new_str.startswith("n"))
# print(new_str.endswith("n"))
#
# num="123"
# print(num.isdigit())
# print(num.isalnum())
# print(num.isnumeric())
# print(num.strip())
# Користувач вводить з клавіатури рядок.
# Порахуйте кількість букв, цифр у рядку. Виведіть обидві
# кількості на екран.

# letters=0
# digits=0
# word=input("Enter a word")
# for letter in word:
#     if letter.isalpha():
#         letters += 1
#     elif letter.isdigit():
#         digits += 1
# print(f"Letters: {letters}, Digits: {digits}")

# Користувач вводить з клавіатури рядок і символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається шуканий
# символ. Отримане число виведіть на екран.

# text=input("Enter text")
# symbol=input("Enter symbol")
# count=text.count(symbol)
# print(f"Count: {count}")




# Завдання 3
# Користувач вводить з клавіатури рядок.
# Зробіть поворот рядків і отриманий результат виведіть на
# екран. Не використовуйте зрізи (slicing) для розв('язання '
#                                                   'задачі.)
# text=input("enter text")
# result=""
# for letter in text:
#     result=letter+result
# print(result)
# Завдання 4
# Користувач вводить з клавіатури рядок і слово для пошуку
# . Порахуйте скільки разів у рядку зустрічається шукане
# слово. Отримане число виведіть на екран.
# text=input("enter text")
# word=input("enter word")
# print(text.count(word))

# Завдання 5
# Користувач вводить з клавіатури рядок, слово для пошуку,
# слово для заміни. Зробіть у рядку заміну одного слова на
# інше. Отриманий рядок відобразіть на екрані.
# text=input("enter text")
# word1=input("enter word to find")
# word2=input("enter word to replace")
# result=text.replace(word1,word2)
# print(result)

# Завдання 6
# Користувач вводить із клавіатури рядок. Знайдіть
# найдовше слово в рядку і виведіть його на екран.
# Якщо таких слів декілька, виведіть перше з них.


# Завдання 7. Перевірка надійності пароля
# Користувач вводить пароль.
# Програма повинна перевірити:
# довжина не менше 8 символів
#  є хоча б одна велика літера
#  є хоча б одна маленька літера
#  є хоча б одна цифра
#  є хоча б один спеціальний символ (! @ # $ % & *)
password = input("Enter your password: ")
upper=0
lower=0
digit=0
special=0
for symbol in password:
    if symbol.isupper():
        upper += 1
    elif symbol.islower():
        lower += 1
    elif symbol.isdigit():
        digit += 1
    elif symbol in "! @ # $ % & *":
        special += 1
if len(password) >=8 and upper and lower and digit and special:
    print("Yes, password is valid")
else:
    print("No, password is invalid")
