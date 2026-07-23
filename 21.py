#
# opened = False
# try:
#     file = open("notes.txt","r")
#     opened = True
#     number=10/0
#     text = file.read()
#     print(text)
#     file.close()
#     print("closed")
# except Exception as ex:
#     print(ex)
# finally:
#     if opened:
#         print("File closed")
#         file.close()
#
# with open("notes.txt","r") as file:
#     text=file.read()
#     print(file.closed)
# print(text)
# print(file.closed)
#
# count=0
# with open('notes.txt','r') as file:
#     longest=''
#     for line in file:
#         count+=1
#         print(line.strip())
#         if len(word)>len(longest):
#             longest=line
# print(count)
# print(longest)
import keyword

# # Завдання 1
# # Напишіть програму, яка відкриває файл numbers.txt, читає числа
# # з нього та обчислює їхню суму, потім записує результат у sum.txt.
#
# with open('numbers.txt','r') as file:
#     numbers = list(map(int,file.readlines()))
#     print(sum(numbers))
# with open('sum.txt','w') as file:
#     file.write(str(sum(numbers)))
#     print(sum(numbers))
# # Завдання 2
# # Напишіть програму, яка запитує у користувача ім'я файлу і слово,
# # потім підраховує кількість входжень цього слова у файлі і виводить результат.
#
# filename=input('Enter file name: ')
# word=input('Enter word: ')
# file=open(filename,'r',encoding='utf-8')
# content=file.read()
# file.close()
# count=content.count(word)
# print(f"The word {word} appears {count} times")
#
# # авдання 3
# # Напишіть програму, яка об'єднує вміст кількох текстових файлів
# # (file1.txt, file2.txt, file3.txt) в один файл merged.txt, додаючи
# # перед вмістом кожного файлу його ім'я у вигляді заголовка.
#
# files=['files1.txt','files2.txt','files3.txt']
# with open('merged.txt','w',encoding='utf-8') as merged:
#     for file_name in files:
#         merged.write(f"======{file_name}======\n")
#         with open(file_name,'r') as file:
#             merged.write('\n\n'')


# # Завдання 4
# # Напишіть програму, яка об'єднує два файли (file1.txt і file2.txt)
# # порядково, чергуючи їхні рядки, і записує результат у merged_alternate.txt.
# with open('file1.txt','r',encoding='utf-8') as f1:
#     lines1 = f1.readlines()
# with open('file2.txt','r',encoding='utf-8') as f2:
#     lines2 = f2.readlines()
# max_length=max(len(lines1),len(lines2))
# with open('merged_alternate.txt','w',encoding='utf-8') as result:
#     for i in range(max_length):
#         if i < len(lines1):
#             result.write(lines1[i])
#         if i < len(lines2):
#             result.write(lines2[i])
# print("чергуючи їхні рядки, і записує результат")

# Завдання 5
# Напишіть програму, яка реалізує керування бібліотекою книжок за допомогою текстового файлу library.txt.
# Програма повинна надавати користувачеві меню з можливими діями:
# Додати нову книжку — користувач вводить назву книжки та автора, програма додає їх у файл.
# Переглянути всі книги — програма завантажує і відображає всі книги, збережені у файлі.
# Пошук книги за автором — користувач вводить ім'я автора, програма виводить усі книги цього автора.
# Видалити книгу — користувач вводить назву книги, і програма видаляє її з файлу, якщо вона існує.
# Вихід — завершує виконання програми.
file_name="library.txt"
def add_book():
    title=input("Enter name-")
    author=input("Enter author name-")

    with open(file_name,'a',encoding='utf-8') as file:
        file.write(f'{title}:{author}\n')

    print("Book added")
def show_books():
    try:
        with open(file_name,'r',encoding='utf-8') as file:
            books=file.readlines()
        if not books:
            print("Library is empty")
            return
        print("Books list:\n")
        # for book in books:
        #     print(book)
        for i,book in enumerate(books,start=1):
            title,author=book.strip().split(':')
            print(f'{i}. {title}:{author}')
    except FileNotFoundError:
        print("File not created")
def search_book():
    keyword=input("Enter name of the book or author")
    try:
        with open(file_name,'r',encoding='utf-8') as file:
            found=False
            for book in file:
                title,author=book.strip().split(':')
                if keyword in title.lower() or keyword in author.lower():
                    print(f' {title}:{author}')
                    found=True
            if not found:
                print("This book not found")
    except FileNotFoundError:
        print("File not created")
search_book()
def delete_book():
    title = input("Enter a book name: ").lower()
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            books = file.readlines()
        with open(file_name, "w", encoding="utf-8") as file:
            for book in books:
                if title not in book.lower():
                    file.write(book)
        print("Book deleted")
    except FileNotFoundError:
        print("File not created")

def main():
    while True:
        print('\nMenu')
        print('1. Add Book')
        print('2. Show Book')
        print('3. Search Book')
        print('4. Delete Book')
        print('5. Exit')
        choice=input('Enter your choice: ')
        match choice:
            case '1':
                add_book()
            case '2':
                show_books()
            case '3':
                search_book()
            case '4':
                delete_book()
            case '5':
                break
            case _:
                print("Invalid choice")
main()
