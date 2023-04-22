class Book:
    def __init__(self, title, author, pages, publisher, isbn, description, genre, num_copies, ):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher
        self.isbn = isbn
        self.description = description
        self.genre = genre
        self.num_copies = num_copies

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_pages(self):
        return self.pages
    
    def get_publisher(self):
        return self.publisher
    
    def get_isbn(self):
        return self.isbn
    
    def set_publisher(self, publisher):
        self.publisher = publisher 

    def set_title(self, title):
        self.title = title
    
    def set_author(self, author):
        self.author = author
    
    def set_pages(self, pages):
        self.pages = pages
    
    def set_isbn(self, isbn):
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, published by {self.publisher} (ISBN: {self.isbn})"
    
    def get_description(self):
        return self.description
    
    def get_genre(self):
        return self.genre
    
    def get_num_copies(self):
        return self.num_copies
    
    def borrow_book(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            return True
        else: 
            return False
        
    def return_book(self):
        self.num_copies += 1

    

