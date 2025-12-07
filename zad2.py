class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka: {self.city}, {self.street}, {self.zip_code}, "
            f"Godziny otwarcia: {self.open_hours}, Tel. kontakt. {self.phone}"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, zatrudniony: {self.hire_date}, "
            f"urodzony: {self.birth_date}, zamieszkały: {self.city}, "
            f"{self.street}, {self.zip_code}, nr tel: {self.phone}"
        )


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages,):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f" - Książka napisana przez: {self.author_name} "
            f"{self.author_surname}, wydana: {self.publication_date}, "
            f"ilość stron: {self.number_of_pages}, {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n ".join(str(book) for book in self.books)
        return (
            f"Zamówienie (dnia: {self.order_date})\n"
            f"Pracownik: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Książka:\n {books_str}"
        )


class Student:
    def __init__(self, album_number, first_name, last_name, city, street, zip_code):
        self.album_number = album_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return (
            f"Student: {self.album_number} {self.first_name} {self.last_name}, "
            f"Adres {self.city} {self.street}, {self.zip_code}"
        )


library1 = Library("Warszawa", "Kwiatowa 5", "00-123", "8-18", "500-111-222")
library2 = Library("Kraków", "Rynek 10", "30-001", "9-17", "500-222-333")

book1 = Book(library1, "1999", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2005", "Henryk", "Sienkiewicz", 450)
book3 = Book(library2, "2010", "Olga", "Tokarczuk", 380)
book4 = Book(library2, "1980", "Stanisław", "Lem", 500)
book5 = Book(library1, "2020", "Andrzej", "Sapkowski", 600)

emp1 = Employee("Jan", "Kowalski", "2020-01-10", "1985-05-03", "Warszawa", "Kwiatowa 5", "00-123", "500-111-222")
emp2 = Employee("Anna", "Nowak", "2019-07-20", "1990-02-14", "Kraków", "Rynek 10", "30-001", "500-333-444")
emp3 = Employee("Piotr", "Zieliński", "2021-11-05", "1988-10-30", "Warszawa", "Leśna 12", "00-140", "500-555-666")

stud1 = Student("145168", "Michał", "Lewandowski", "Warszawa", "Polna 3", "00-200")
stud2 = Student("142797", "Natalia", "Kaczmarek", "Kraków", "Grodzka 7", "30-002")
stud3 = Student("165893", "Ola", "Wiśniewska", "Gdańsk", "Długa 1", "80-100")

order1 = Order(emp1, stud1, [book1, book3, book5], "2025-01-10")
order2 = Order(emp2, stud2, [book2, book4], "2025-01-11")

print(order1)
print(order2)
