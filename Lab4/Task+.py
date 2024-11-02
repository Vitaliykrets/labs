class Book:
    def __init__(self, title, reading_hours):
        self.title = title
        self.__reading_hours = reading_hours

    def get_reading_hours(self):
        return self.__reading_hours

    def set_reading_hours(self, hours):
        if hours > 0:
            self.__reading_hours += hours
        else:
            print("The hours must be greater than zero")

    def __str__(self):
        return f"Book: {self.title}, Hours read: {self.__reading_hours}"

books = [Book("Book 1", 5), Book("Book 2", 3), Book("Book 3", 8)]

books[0].set_reading_hours(4)
books[1].set_reading_hours(3)
books[2].set_reading_hours(2)
min_hours_book = books[0]

for book in books:
    if book.get_reading_hours() < min_hours_book.get_reading_hours():
        min_hours_book = book

print(f"Book with the minimum number of hours read: {min_hours_book}")