# Завдання 1:
# Створи декоратор @debug_info, який перед виконанням функції виводить "Start function",
# а після — "End function".
def debug_info(func):
    def wrapper():
        print("Start function")
        func()
        print("End function")
    return wrapper
@debug_info
def hello():
    print("Hello, World!")
hello()
# Завдання 2:
# Створи декоратор @check_login, який не дозволяє виконати функцію, якщо user_logged_in = False.
# user_logged_in = False
# @check_login
# def show_profile():
#  print("Welcome to your profile!")
user_logged_in = False
def check_login(func):
    def wrapper():
        if user_logged_in:
            func()
        else:
            print("Access denied!")
    return wrapper
@check_login
def show_profile():
    print("Welcome to your profile!")
show_profile()
# Завдання 3:
# Напиши декоратор @upper_text, який робить результат функції великими літерами.
def upper_text(func):
    def wrapper():
        return func().upper()
    return wrapper
@upper_text
def greeting():
    return "Hello, world!"
print(greeting())
# Завдання 4:
# Створи декоратор @repeat_three_times, який запускає функцію тричі.
def repeat_three_times(func):
    def wrapper():
        for i in range(3):
            func()
    return wrapper
@repeat_three_times
def say_hello():
    print("Hello!")
say_hello()
# Завдання 5. Приховування персональних даних
# Умова
# Створіть декоратор hide_personal_data.
# Після виконання функції потрібно приховати особисті дані у рядку.
# Приклад 1
# Функція повертає телефон
# @hide_personal_data
# def phone():
#  return "+380991234567"
# Результат
# +38099****567
# Приклад 2
# Функція повертає email
# @hide_personal_data
# def email():
#  return "student@gmail.com"
# Результат
# stu*****@gmail.com
def hide_personal_data(func):
    def wrapper():
        data = func()
        if "@" in data:
            name, domain = data.split("@")
            return name[:3] + "*****@" + domain
        else:
            return data[:6] + "****" + data[-3:]
    return wrapper
@hide_personal_data
def phone():
    return "+380991234567"
@hide_personal_data
def email():
    return "student@gmail.com"
print(phone())
print(email())