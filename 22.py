import json
# import pickle
# from dataclasses import field
#
# student={
#     "name": "Max",
#     "age": 23,
#     "grades":[10,11,10]
# }
# with open("student.pickle", "wb") as file:
#     pickle.dump(student, file)
#
# with open("student.pickle", "rb") as file:
#     student = pickle.load(file)
# print(student)
#
# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)
#
# with open("student.json", "w") as file:
#     st=json.load(student, indent=4))
# print(st)

    # Завдання
    # 1
    # Користувач заповнює з клавіатури список цілих.Стисніть отримані дані
    # та збе­ре­жіть їх у файл.Після цього
    # завантажте
    # дані
    # з
    # файлу
    # в
    # новий
    # список.
# import pickle
# list_numbers = list(map(int, input("Введіть список цілих: ").split()))
# with open("list_numbers.pkl", "wb") as file:
#     pickle.dump(list_numbers, file)
# print("Список успішно записаний.")

# import csv
# with open("student.csv", "w",newline="",encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age', 'Phone'])
#     writer.writerow(['Max','34','5645645245'])
#     writer.writerow(['Ban', '14', '56456455445'])
#
# with open("student.csv",encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# with open("student.csv") as file:
#     reader = csv.DictReader(file)
#     for st in reader:
#         print(st)
#
# with open('employee.csv','w',newline='') as file:
#       field_names = ['Name', 'Salary']
#       writer = csv.DictWriter(file, fieldnames=field_names)
#       writer.writeheader()
#       writer.writerow({'Name': 'Max', 'Salary': 1000})

# Прочитати файл.
# Вивести всіх працівників.
# Порахувати кількість працівників.
# Знайти найбільшу зарплату.
# Знайти найменшу зарплату.
# Обчислити середню зарплату.
# Вивести всіх працівників відділу IT.
# Додати нового працівника.
# Зберегти файл.
import csv
count=0
with open('employee.csv',encoding='utf-8',newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        count+=1
print(count)
employees = []
with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Salary"] = int(row["Salary"])
        employees.append(row)
max_salary = max(employee["Salary"] for employee in employees)
print(f"Maximum salary: {max_salary}")
min_salary = min(employee["Salary"] for employee in employees)
print(f"Minimum salary: {min_salary}")
average_salary = sum(employee["Salary"] for employee in employees) / len(employees)
print(f"Average salary: {average_salary}")
