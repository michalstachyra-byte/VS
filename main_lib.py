from library_sys.library import Library
from library_sys.book import Book
from library_sys.employee import Employee
from library_sys.student import Student
from library_sys.order import Order


library1 = Library("Warsaw", "Kwiatowa 5", "00-123", "8-18", "500-111-222")
library2 = Library("Cracow", "Rynek 10", "30-001", "9-17", "500-222-333")

book1 = Book(library1, "1999", "Adam", "Mickiewicz", 300)
book2 = Book(library1, "2005", "Henryk", "Sienkiewicz", 450)
book3 = Book(library2, "2010", "Olga", "Tokarczuk", 380)
book4 = Book(library2, "1980", "Stanislaw", "Lem", 500)
book5 = Book(library1, "2020", "Andrzej", "Sapkowski", 600)

emp1 = Employee("Jan", "Kowalski", "2020-01-10", "1985-05-03", "Warsaw", "Kwiatowa 5", "00-123", "500-111-222")
emp2 = Employee("Anna", "Nowak", "2019-07-20", "1990-02-14", "Cracow", "Rynek 10", "30-001", "500-333-444")

stud1 = Student("145168", "Michal", "Lewandowski", "Warsaw", "Polna 3", "00-200")
stud2 = Student("142797", "Natalia", "Kaczmarek", "Cracow", "Grodzka 7", "30-002")

order1 = Order(emp1, stud1, [book1, book3, book5], "2025-01-10")
order2 = Order(emp2, stud2, [book2, book4], "2025-01-11")

print(order1)
print(order2)
