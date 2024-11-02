class Book:
    def __init__(self, pages, author, price):
        self.__pages = pages
        self.__author = author
        self.__price = price
        self.public_numeric_field = 0
        self.public_string_field = ""

    def get_pages(self):
        return self.__pages

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def get_numeric_field(self):
        return self.public_numeric_field
    
    def get_string_field(self):
        return self.public_string_field
    
    def set_pages(self, pages):
        self.__pages = pages

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def set_numeric_field(self, value):
        self.public_numeric_field = value

    def set_string_field(self, value):
        self.public_string_field = value

    def __str__(self):
        return (f"Book (Author: {self.get_author()}, Pages: {self.get_pages()}, "
                f"Price: {self.get_price()} UAH, "
                f"Numeric Field: {self.get_numeric_field()}, "
                f"String Field: '{self.get_string_field()}')")

    def __repr__(self):
        return (f"Book ('{self.get_author()}', {self.get_pages()}, "
                f"{self.get_price()}, {self.get_numeric_field()}, '{self.get_string_field()}')")

    def __del__(self):
        print(f"Book '{self.get_author()}' is being deleted.")

def main():
    book1 = Book(300, "Тарас Шевченко", 150.00)
    book1.set_numeric_field(1)
    book1.set_string_field("Класична література")
    
    book2 = Book(400, "Іван Франко", 180.00)
    book2.set_numeric_field(2)
    book2.set_string_field("Історична проза")
    
    book3 = Book(200, "Леся Українка", 120.00)
    book3.set_numeric_field(3)
    book3.set_string_field("Поезія")

    for book in (book1, book2, book3):
        print(book)

if __name__ == "__main__":
    main()
    
    