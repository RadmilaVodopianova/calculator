# def square(x):
#     return x * x
# result = square(2)
# print(result)
#
# numbers = [1,2,3,4,5,6,7,8,9]
# result = []
# for n in numbers:
#     result.append(n * n**2)
# print(result)
# result=list(map(lambda x: x**2, numbers))
# print(result)
#
# def greet(name):
#     return f"Hello {name}"
# print(greet("Rada"))
# message_func=greet
# print(message_func("lol"))
#
# def apply_operetion(a,b,operetion):
#     return operetion(a,b)
#
# def add(x,y):
#     return x+y
#
# def multiply(x,y):
#     return x+y
#
# print(apply_operetion(2,2,multiply))
# print(apply_operetion(6,10,add))
#
# def nameUpper(name):
#     return 'user'+name.upper()
# def nameLower(name):
#     return 'user'+ name.lower()
# def makeLog(userName,maker):
#     return maker(userName)
# print(f"New login:{makeLog('max',nameLower)}")
# print(f"New login:{makeLog('max',nameUpper)}")
#
# square=lambda x: x ** 2
# print(square(3))
#
# add=lambda a,b: a+b
# print(add(3,4))
#
# is_even=lambda x: x%2==0
# print(is_even(22))
#
# maximum=lambda a,b: a if a>b else b
# print(maximum(3,4))
#
# studens=[['Bob',70],['Jane',60],['Nick',88]]
# print(studens)
# sortedSts=sorted(studens,key=lambda x:x[0])
# print(sortedSts)
#
# studBirthYear=[2000,1997,2003,1996]
# studYears=[]
# for year in studBirthYear:
#     studYears.append(2026-year)
# print(studYears)
#
# studAges=list(map(lambda year:2026-year,studBirthYear))
# print(studAges)
#
# userLogs=['Admin','STUDENT','GHbh','User']
# print(userLogs)
#
# userLogsLower=list(map(str.lower,userLogs))
# print(userLogsLower)
#
# myValues=['2','4.6','7.9']
# myNumbers=list(map(float,myValues))
# print(myNumbers)
#
# def modifyPizzaType(pizzaType):
#     return pizzaType+" Pizza"
#
# pizzaTypes=['Meat','4Cheese','Margarita']
# print(pizzaTypes)
#
# pizzaNames=list(map(modifyPizzaType,pizzaTypes))
# print(pizzaNames)
#
# prices=[100,8,6,4,120,230]
# expensive=list(filter(lambda x: x>=100,prices))
# print(expensive)
#
# def checkLog(user):
#     if user.lower().find('user')!=-1:
#         return True
#     else:
#         return False
#
# userLogs=['Admin','STUDENT','GHbh','User']
# userPass=['111','32125','254555']
# for log,passw in zip(userLogs,userPass):
#     print(f"login:{log} pass:{passw}")
# print(list(zip(userLogs,userPass)))

# Використовуючи
# функцію
# filter, відфільтруйте
# список
# чисел, залишивши
# лише
# парні
# числа.Вихідний
# список: [1, 2, 3, 4, 5].

numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Є список чисел. Отримати список їх квадратів.
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Напишіть програму, яка приймає список цілих чисел і
# повертає список рядків, які представляють ці числа.

numbers = [1,2,3,4,5]
strings = list(map(str, numbers))
print(strings)

# Є два списки:
# students = ["Анна", "Олег", "Марія", "Іван"]
# scores = [95, 67, 88, 73]
# Потрібно:
# об’єднати списки в пари (ім’я, бал);
# залишити тільки тих студентів, у кого бал 80 або більше;
# вивести результат.
students = ["Анна", "Олег", "Марія", "Іван"]
scores = [95, 67, 88, 73]
pairs=list(zip(students, scores))
result=list(filter(lambda student: scores >=80, pairs))
print(result)