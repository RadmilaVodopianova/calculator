# Завдання 1
class Book:
    def __init__(self, title, author, pages, current_page=1):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
    def show_info(self):
        print("Назва:", self.title)
        print("Автор:", self.author)
        print("Кількість сторінок:", self.pages)
        print("Поточна сторінка:", self.current_page)
    def read_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
        else:
            print("Це остання сторінка")
    def read_pages(self, count):
        if self.current_page + count <= self.pages:
            self.current_page += count
        else:
            self.current_page = self.pages
    def restart(self):
        self.current_page = 1
    def progress(self):
        percent = self.current_page / self.pages * 100
        print("Прочитано:", round(percent, 2), "%")
book1 = Book("Воно", "Стівен Кінг", 1138)
book2 = Book("Сяйво", "Стівен Кінг", 447)
book1.show_info()
book1.read_page()
print(book1.current_page)
book1.read_pages(100)
print(book1.current_page)
book1.progress()
book1.restart()
print(book1.current_page)
print()
book2.show_info()
book2.read_pages(500)
print(book2.current_page)
book2.progress()

# Завдання 2
class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code
    def show_info(self):
        print("Назва міста:", self.name)
        print("Регіон:", self.region)
        print("Країна:", self.country)
        print("Кількість жителів:", self.population)
        print("Поштовий індекс:", self.postal_code)
        print("Телефонний код:", self.phone_code)
    def set_name(self, new_name):
        self.name = new_name
    def set_population(self, new_population):
        self.population = new_population
    def set_postal_code(self, new_postal_code):
        self.postal_code = new_postal_code
    def set_phone_code(self, new_phone_code):
        self.phone_code = new_phone_code
city1 = City(
    "Одеса",
    "Одеська область",
    "Україна",
    1010000,
    "65000",
    "+380 48"
)
city2 = City(
    "Львів",
    "Львівська область",
    "Україна",
    720000,
    "79000",
    "+380 32"
)
city1.show_info()
print()
city2.show_info()
print()
city1.set_population(1020000)
print(city1.population)
city2.set_postal_code("79008")
print(city2.postal_code)

# Завдання 3
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities
    def show_info(self):
        print("Назва країни:", self.name)
        print("Континент:", self.continent)
        print("Кількість жителів:", self.population)
        print("Телефонний код:", self.phone_code)
        print("Столиця:", self.capital)
        print("Міста:", self.cities)
    def set_population(self, new_population):
        self.population = new_population
    def set_capital(self, new_capital):
        self.capital = new_capital
    def add_city(self, new_city):
        self.cities.append(new_city)
    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
        else:
            print("Такого міста немає")
country1 = Country(
    "Україна",
    "Європа",
    37000000,
    "+380",
    "Київ",
    ["Київ", "Одеса", "Львів", "Харків"]
)
country1.show_info()
print()
country1.add_city("Дніпро")
print(country1.cities)
country1.remove_city("Харків")
print(country1.cities)
country1.set_population(36000000)
print(country1.population)
