# while True:
#     psswd=input("Enter a password: ")
#     if password=="":
#         print("Can't be empty")
#     if password =="admin":
#         print("OK")
#         break
#     print("Error password")


# Користувач вводить із клавіатури два числа.
# Потрібно порахувати суму чисел у вказаному діапазоні,
# а також середньоарифметичне.
# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))
# summ = 0
# avg = 0
# count=0
# while num1<=num2:
#     summ+=num1
#     print(f"{summ}")
#     count+=1
#     num1+=1
# print(f"Result:{summ}")
# avg = summ/count
# print(f"Average is: {avg}")
# Завдання 2
# Користувач вводить із клавіатури число.
# Потрібно порахувати факторіал числа.
# Наприклад, якщо введено 3, факторіал числа 1*2*3 = 6.
# Формула для розрахунку факторіалу:
# n! = 1*2*3...*n, де n — число для розрахунку
# факторіалу.
# num=int(input("Enter a number: "))
# factorial=1
# try:
#     i = 1
#     while i<=num:
#         factorial*=i
#     i+=1
#     print(factorial)
# except Exception as e:
#     print(e)

# for i  in 1,2,3,4,5:
#     print(i)
#
# for num in range(20):
#     if num%2:
#         continue
#     print(num,end=" ")
#     if  num==10:
#         break
# print()
#
# for s in "python":
#     print(s)

# таблиця множення
# num=2
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# Користувач вводить із клавіатури довжину лінії. Потрібно
# відобразити на екрані горизонтальну лінію з *, вказаної довжини.
# Наприклад, якщо було введено 7, тоді виведення на екран буде таким:

# num=int(input("Enter a number to get a line "))
# for i in range(num):
#     print("*",end="")
# Користувач вводить з клавіатури довжину лінії та
# символ для заповнення лінії. Потрібно відобразити на екрані
# горизонтальну лінію із введеного символу, зазначеної довжини.
# Наприклад, якщо було введено 5 і &, тоді виведення на екран буде таким:
# num=int(input("Enter a number: "))
# symb=input("Enter a symbol: ")
# for i in range (num):
#     print(symb,end=" ")
# Користувач вводить число.
# За допомогою циклу for порахувати кількість цифр.
# num=input("Enter a number: ")
# count=0
# for i in num:
#     count+=1
# print(count)
# # Користувач вводить число N.
# Порахувати:
# суму парних;
# суму непарних чисел від 1 до N.
# num=int(input("Enter a number: "))
# even=0
# odd=0
# for i in range(1,num+1):
#     print(i)
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"The sum of the even numbers is {even}")
# print(f"The sum of the odd numbers is {odd}")

# Користувач вводить висоту.
# Для 5:
# *
# **
# ***
# ****
# *****
# hght=int(input("Enter a height: "))
# for i in range(1,hght+1):
#     print("*" * i )

# Користувач вводить слово.
# Вивести його у зворотному порядку через for.
# word=input("Enter a word: ")
# reverse=""
# for letter in word:
#     reverse=letter+reverse
# print("Reversed word-",reverse)

# Створіть програму, яка відображає меню з опціями для вибору:
# 1 — знайти мінімум двох чисел, 2 — знайти максимум двох чисел,
# 3 — вихід. Програма має запитувати в користувача номер опції і,
# якщо вибрано пункт 1 або 2, запитувати введення двох чисел, після
# чого знаходити і виводити або мінімум (якщо вибрано 1), або максимум
# (якщо вибрано 2) із введених чисел. При введенні пункту 3 програма
# завершує роботу, виводячи повідомлення про вихід. Якщо введено
# некоректну опцію, програма має повідомити про помилку і знову показати
# меню. Програма має працювати в циклі, повторюючи виведення меню і
# виконання дій доти, доки не буде обрано вихід.
try:
 while True:
        print("1 — знайти мінімум двох чисел, 2 — знайти максимум двох чисел, 3 — вихід")
        choice=input("Enter your choice: ")
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        if choice==1:
            if num1<num2:
                print(num1)
            else:
                print(num2)
        elif choice==2:
            if num1 < num2:
                print(num2)
            else:
                print(num1)
        elif choice==3:
            print("Program is ending")
        continue
except ValueError:
    print("Please enter a number")
