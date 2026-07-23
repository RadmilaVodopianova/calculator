# students=['Anna','Bill','Max']
# print(students)
#
# # # name=input("Enter your name: ")
# # students.append(name)
# # print(students)
#
# file_name='students.txt'
# file=open(file_name,'w',encoding='utf-8')
# for st in students:
#     file.write(st+'\n')
# file.close()
#
# student={
#     'name':'Max',
#     'age':15,
#     'grade':11
# }
# file=open(file_name,'w',encoding='utf-8')
# for key,value in student.items():
#     file.write(f"{key}: {value}\n")
# file.close()
#
# products = [
#     {
#         "name": "Ноутбук",
#         "price": 35000
#     },
#     {
#         "name": "Миша",
#         "price": 800
#     },
#     {
#         "name": "Клавіатура",
#         "price": 1500
#     }
# ]
# file=open("products.txt", "w", encoding="utf-8")
# for product in products:
#     file.write(f"Назва: {product['name']}, Ціна: {product['price']}\n")
# file.close()
#
# file=open('students.txt','r',encoding='utf-8')
# data=file.read(5)
# data2=file.read(10)
# print(data)
# print(data2)
# file.close()
#
# file=open('students.txt','r',encoding='utf-8')
# data=file.readline()
# alllines=file.readlines()
# print(data)
# print(alllines)
# file.close()
#
# file =open(file_name,'a',encoding='utf-8')
# file.seek(0,0)
# print(file.tell())
# file.write('Ben\n')
# file.close()

# Завдання 1
# Напишіть програму, яка створює текстовий файл
# output.txt і записує в нього рядок "Hello, world!".
def create_file(name_file,text):
    file=open('output.txt','w',encoding='utf-8')
    file.write(text)
    file.close()
create_file('output.txt','Hello World')
# Завдання 2
# Напишіть програму, яка відкриває файл output.txt,
# читає його вміст і виводить у консоль.
file = open('output.txt','r',encoding='utf-8')
text = file.read()
print(text)
file.close()


# Завдання 3
# Напишіть програму, яка копіює вміст файлу data.txt
# у новий файл backup.txt.
data_file=open('data.txt','r',encoding='utf-8')
data_file.write("LOL")
file.close()
source_file=open('data.txt','r',encoding='utf-8')
content=source_file.read()
source_file.close()
backup_file=open('backup.txt','w',encoding='utf-8')
backup_file.write(content)
backup_file.close()


# Завдання 4
# Напишіть програму, яка підраховує кількість рядків у
# файлі data.txt і виводить результат
data_file=open('data.txt','r',encoding='utf-8')
lines=data_file.readlines()
print("К-ть рядків:",len(lines))
file.close()

# Завдання 5
# Напишіть програму, яка відкриває файл data.txt,
# аналізує його вміст і створює звіт summary.txt, у
# якому вказується кількість рядків, слів і символів у
# файлі.
data_file=open('data.txt','r',encoding='utf-8')