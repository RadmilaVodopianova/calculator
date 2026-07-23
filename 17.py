# def hello():
#     print("Hello")
# n=100
# a=hello
# a()
#
# def execute(func):
#     func()
# execute(hello)
#
# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper
#
# newHello=decorator(hello)
# newHello()
# @decorator
# def hello2():
#     print("hi")
# hello2()
#
# def decorator_v2(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         func(*args, **kwargs)
#         print("End")
#     return wrapper
# @decorator_v2
# def add(a,b):
#     print(a+b)
# add(2,4)
# @decorator_v2
# def add(a,b,c):
#     print(a+b+c)
# add(3,4,5)
# def decorator_v3(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result=func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper
# @decorator_v3
# def mul(a,b,c):
#     return a*b*c
# res=mul(1,2,c=3)
# print(res)


# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start=time.time()
#         result = func(*args, **kwargs)
#         end=time.time()
#         print(end-start)
#         return result
#     return wrapper
#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#        print(f"Calling {func.__name__}")
#        return func(*args, **kwargs)
#     return wrapper
# @timer
# @logger
# def sleep():
#     time.sleep(1)
# sleep()
#
#
# def counter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(count)
#         return func(*args, **kwargs)
#     return wrapper
# @counter
# def show():
#     print("test work")
# for i in range(5):
#     show()
#
# def repeat(func):
#     def decorator(func):
#     def wrapper(*args, **kwargs):
#         for i in range(times):
#             func(*args, **kwargs)
#         return wrapper
#     return
# @repeat(3)
# def hello3():
#     print("Hello world")
# hello3()


# Завдання 1. Створіть декоратор login_required.
# Якщо користувач не авторизований (logged=False),
# функція не повинна виконуватись.

# def login_required(func):
#
#     def wrapper(*args, **kwargs):
#         if logged:
#             return func(*args, **kwargs)
#         else:
#             print("Block")
#     return wrapper
#
# logged=False
# @login_required
# def show_marks():
#     print("1,2,3,4")
# show_marks()

# Завдання 2
# Створіть декоратор only_numbers.
# Він повинен дозволяти виконання функції лише тоді,
# коли всі аргументи є числами.

def only_numbers(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                print("Must be integer")
                return
        return func(*args)
    return wrapper
@only_numbers
def add(a,b):
    return a+b
add(5,6)
print(add("5",6))