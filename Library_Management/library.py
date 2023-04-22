from book import Book

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]

    def search_book(self, title):
        if title in self.books:
            return self.books[title]
        else:
            return None
        
    def get_books(self):
        return self.books

