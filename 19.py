dict1 = {
    'mom': '3802342343',
    'qwerty': '12312312'
}

student={'name':'Max',
         'age':21,
         'city':'Dnipro'}

print(f"Student name: {student['name']}")
if age in student:
    student['age']=21
print(f"Student age: {student['age']}")
student['phone']='12312312'
print(f"Student phone: {student['phone']}")

dict(zip([1, 2, 3], [11, 22, 33]))
print(dict(**student))
print(len(student))

for key, value in dictionary.items():
    print(f"{key}: {value}")

print(student['name'])
print(student.get('name2'))

users = [
    {'name': 'Bill', 'age': 30, 'login': 'qwer'},
    {'name': 'Mark', 'age': 28, 'login': '123asd'},
    {'name': 'Den', 'age': 39, 'login': 'fsdfd'},
    {'name': 'Ilon', 'age': 45, 'login': '1111'}
]

keyName = input("Input info type - ")
keyValue = input("Input info value - ")

isElementFound = False

for user in users:
    if user.get(keyName) == keyValue:
        print("Element is found!")

        for key, val in user.items():
            print(f"{key}: {val}")

        isElementFound = True
        break

if isElementFound:
    print("Element is not  found!")



filmDict = {
    'originalTitle': 'Python',
    'creator': 'Gvido',
    'rate': 9,
    'description': 'Film about python',
    'year': [1991, 1992]
}

for key, value in filmDict.items():
    print(f"{key} {value}")

sortedFilm = sorted(filmDict.items(), key=lambda x: x[0])

print(sortedFilm)
for element in sortedFilm:
    print(elem)


keyList = list(filmDict.keys())

sortedKeys = sorted(keyList)

for key in sortedKeys:
    print(key, filmDict[key])


users = [
    {'name': 'Bill', 'age': 30, 'login': 'qwer'},
    {'name': 'Mark', 'age': 28, 'login': '123asd'},
    {'name': 'Den', 'age': 39, 'login': 'fsdfd'},
    {'name': 'Ilon', 'age': 45, 'login': '1111'}
]
SortedUsersByName = sorted(users, key=lambda x: x['name'])
print(SortedUsersByName)


users30 = list(filter(lambda user: user['age'] > 30, users))