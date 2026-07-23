numbers=[1,2,3,4,5]
for num in numbers:
    print(num)
for i in range(len(numbers)):
    print(numbers[i])
NUMBER_PI=3.14
print(NUMBER_PI)
NUMBER_PI="qwerty"

years=(2000,2005,1998,2001)
print(years)
print(type(years))

empty=()
print(type(empty))

nums=(1)
print(type(nums)) #<class 'int'>
nums=("1",)
print(type(nums)) #<class 'tuple'>

numbers=tuple(numbers)
print(type(numbers))

colors=('red','green','blue')
print(colors[1])
print(colors[2])
print(colors[:2])
print(colors[::-1])
print(colors.count('red'))
if 'green2' in colors:
    print(colors.index('green2'))

def showNums(*nums):
    print(nums)
showNums(1,2,3,4,5)

person=('Max',20)
name,age=person
print(name)
print(age)

# a,b,c=(1,2,3)
a=1
b=2
a,b=b,a
print(a,b)

students=(
    ('Ivan',23),
    ('Max',19),
    ('Oleg',21)
)
print(students[1][0])

# Завдання 1
# Користувач вводить з клавіатури назву фрукта.
# Виведіть на екран кількість фруктів, що містяться в
# кортежі як елемент.
# fruits=['apple','banana','orange']
# fruit=input('Enter a fruit:')
# print(fruits.count(fruit))
# Завдання 2
# Додайте до першого завдання підрахунок кількості, коли
# назва фрукта є частиною елемента. Наприклад, «banana,
# apple, bananamango, mango, strawberry-banana».
# У приведеному прикладі «banana» попадається три рази.
# fruits=("banana", "apple", "bananamango"," mango", "strawberry-banana")
# fruit=input("Enter a fruit:")
# count=0
# for i in fruits:
#     if fruit in i:
#         count+=1
# print(count)


emails=[
    'ivan@gmail.com',
    'max@gmail.com',
    'ivan@gmail.com',
    'bill@gmail.com',
    'kate@gmail.com'
]
unique=set(emails)
print(unique)
numbers={1,2,3,4,5}
nums=[2,2,4,4,5,8]
print(set(nums))

# s=set()
# print(type(s))  <class 'set'>

numbers.add(123)
print(numbers)

iphoneSet1={'Iphone11','Iphone12','Iphone13'}
IphoneSet2={'Iphone13','Iphone12','Iphone15','Iphone17'}
print(iphoneSet1.difference(IphoneSet2))
print(iphoneSet1-IphoneSet2)

print(iphoneSet1.intersection(IphoneSet2))

print(iphoneSet1.union(IphoneSet2))
print(iphoneSet1|IphoneSet2)

frozenA=frozenset(iphoneSet1)
print(frozenA)


# Завдання 1
# Маємо множину з назвами країн. Надайте користувачеві
# можливість:
# додавати країни;
# видаляти країни;
# пошуку країн за введеними символами;
# перевіряти, чи міститься країна в множині.

-


