# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # was not checked out

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
