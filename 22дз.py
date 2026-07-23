# Завдання 1. Робота з JSON
# Створіть словник з інформацією про себе:
# student = {
#  "name": "Іван",
#  "age": 20,
#  "city": "Київ",
#  "group": "ПЗ-23"
# }
# Необхідно:
# Записати словник у файл student.json.
# Зчитати дані з файлу.
# Вивести інформацію у форматі:
# Ім'я: Іван
# Вік: 20
# Місто: Київ
# Група: ПЗ-23
import json
student = {
    "name": "Radmila",
    "age": 22,
    "city": "Odesa",
    "group": "PythonAI62"
}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)
with open("student.json", "r", encoding="utf-8") as file:
    student_data = json.load(file)
print(f"Ім'я: {student_data['name']}")
print(f"Вік: {student_data['age']}")
print(f"Місто: {student_data['city']}")
print(f"Група: {student_data['group']}")
# Завдання 2. Робота з CSV
# Створіть файл products.csv.
# Користувач вводить інформацію про 5 товарів:
# назва;
# ціна;
# кількість.
# Після введення всі дані потрібно записати у CSV-файл.
# Після цього:
# прочитати файл;
# вивести всі товари у вигляді таблиці.
import csv
products = []
for i in range(5):
    print(f"\nProduct №{i + 1}")
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))
    products.append([name, price, quantity])
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Name", "Price", "Quantity"])
    writer.writerows(products)
with open("products.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    print("\nProduct table:")
    print("-" * 45)
    print(f"{'Name':<20}{'Price':<12}{'Quantity':<10}")
    print("-" * 45)
    next(reader)
    for row in reader:
        print(f"{row[0]:<20}{row[1]:<12}{row[2]:<10}")
    print("-" * 45)
# Завдання 3 *. Каталог фільмів (JSON)
# Створіть програму «Каталог фільмів».
# Для збереження інформації використовуйте файл movies.json.
# Для кожного фільму зберігайте:
# назву;
# жанр;
# рік;
# рейтинг.
# Реалізуйте меню:
# 1. Додати фільм
# 2. Показати всі фільми
# 3. Знайти фільми за жанром
# 4. Видалити фільм
# 5. Вихід
# Усі зміни повинні автоматично зберігатися у JSON-файл.
import json
file_name = "movies.json"
def load_movies():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def save_movies(movies):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)
def add_movie(movies):
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    try:
        year = int(input("Enter release year: "))
        rating = float(input("Enter movie rating: "))
    except ValueError:
        print("Year and rating must be numbers.")
        return
    movie = {
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating
    }
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully.")
def show_movies(movies):
    if not movies:
        print("Movie catalog is empty.")
        return
    print("\nMovie catalog:")
    for number, movie in enumerate(movies, start=1):
        print(f"\nMovie #{number}")
        print(f"Title: {movie['title']}")
        print(f"Genre: {movie['genre']}")
        print(f"Year: {movie['year']}")
        print(f"Rating: {movie['rating']}")
def search_by_genre(movies):
    genre = input("Enter genre to search: ").lower()
    found_movies = []
    for movie in movies:
        if movie["genre"].lower() == genre:
            found_movies.append(movie)
    if not found_movies:
        print("No movies found in this genre.")
        return
    print("\nFound movies:")
    for movie in found_movies:
        print(
            f"{movie['title']} | "
            f"{movie['genre']} | "
            f"{movie['year']} | "
            f"Rating: {movie['rating']}"
        )
def delete_movie(movies):
    title = input("Enter movie title to delete: ").lower()
    for movie in movies:
        if movie["title"].lower() == title:
            movies.remove(movie)
            save_movies(movies)

            print("Movie deleted successfully.")
            return
    print("Movie not found.")
def main():
    movies = load_movies()
    while True:
        print("\nMenu")
        print("1. Add movie")
        print("2. Show all movies")
        print("3. Search movies by genre")
        print("4. Delete movie")
        print("5. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                add_movie(movies)
            case "2":
                show_movies(movies)
            case "3":
                search_by_genre(movies)
            case "4":
                delete_movie(movies)
            case "5":
                print("Program finished.")
                break
            case _:
                print("Invalid menu option.")
main()
# авдання 4**. Електронний журнал (CSV)
# Створіть програму «Журнал оцінок».
# Інформацію зберігайте у файлі grades.csv
# Для кожного студента потрібно записувати:
# ПІБ;
# групу;
# оцінку.
# Реалізуйте меню:
# 1. Додати студента
# 2. Показати всіх студентів
# 3. Знайти студента
# 4. Обчислити середній бал групи
# 5. Показати студентів із балом більше 90
# 6. Вихід
# Додатково (за бажанням)
# Під час виведення інформації відсортувати студентів за оцінкою (від більшої до меншої)
import csv
import os
file_name = "grades.csv"
field_names = ["full_name", "group", "grade"]
def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
def load_students():
    students = []
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["grade"] = float(row["grade"])
            students.append(row)
    return students
def add_student():
    full_name = input("Enter student's full name: ").strip()
    group = input("Enter student's group: ").strip()
    try:
        grade = float(input("Enter student's grade: "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return
    except ValueError:
        print("Grade must be a number.")
        return
    student = {
        "full_name": full_name,
        "group": group,
        "grade": grade
    }
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow(student)
    print("Student added successfully.")
def display_students(students):
    if not students:
        print("No students found.")
        return
    students.sort(key=lambda student: student["grade"], reverse=True)
    print("\n" + "-" * 65)
    print(f"{'Full name':<30}{'Group':<15}{'Grade':<10}")
    print("-" * 65)
    for student in students:
        print(
            f"{student['full_name']:<30}"
            f"{student['group']:<15}"
            f"{student['grade']:<10.1f}"
        )

    print("-" * 65)
def show_all_students():
    students = load_students()
    display_students(students)
def find_student():
    search_name = input("Enter student's name: ").strip().lower()
    students = load_students()
    found_students = []
    for student in students:
        if search_name in student["full_name"].lower():
            found_students.append(student)
    if not found_students:
        print("Student not found.")
        return
    print("\nFound students:")
    display_students(found_students)
def calculate_group_average():
    group = input("Enter group name: ").strip().lower()
    students = load_students()
    group_grades = []
    for student in students:
        if student["group"].lower() == group:
            group_grades.append(student["grade"])
    if not group_grades:
        print("No students found in this group.")
        return
    average_grade = sum(group_grades) / len(group_grades)
    print(f"Average grade of the group: {average_grade:.2f}")
def show_students_above_90():
    students = load_students()
    high_grade_students = []
    for student in students:
        if student["grade"] > 90:
            high_grade_students.append(student)
    if not high_grade_students:
        print("No students with a grade above 90.")
        return
    print("\nStudents with grades above 90:")
    display_students(high_grade_students)
def main():
    create_file()
    while True:
        print("\nGrade Journal")
        print("1. Add student")
        print("2. Show all students")
        print("3. Find student")
        print("4. Calculate group average")
        print("5. Show students with grades above 90")
        print("6. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                add_student()
            case "2":
                show_all_students()
            case "3":
                find_student()
            case "4":
                calculate_group_average()
            case "5":
                show_students_above_90()
            case "6":
                print("Program finished.")
                break
            case _:
                print("Invalid option. Please choose from 1 to 6.")
main()