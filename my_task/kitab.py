class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def __str__(self):
        status = "Kitabxanada var." if not self.is_borrowed else "Kiraye goturulub."
        return f" '{self.title}' - {self.author} ({status})"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f" '{title}' adli kitab kitabxanaya elave edildi.")
        
    def display_books(self):
        if not self.books:
            print("Kitabxanada hele kitab yoxdur.")
            return
        print(f"\n{self.name} kitabxanadaki kitablar:")
        for book in self.books:
            print(book)
            
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f" '{book.title}' kitabi kiraye goturuldu.")
                    return
                else:
                    print(f"Teessuf, '{book.title}' kitabi artiq kiraye goturulub.")
                    return
        print(f" '{title}' kitabi kitabxanada tapilmadi.")
        
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f" '{book.title}' kitabini qaytardiginiz ucun cox sagolun.")
                    return
                else:
                    print(f" '{book.title}' kitabi kiraye verilmeyib.")
                    return
        print(f" '{title}' kitab kitabxanada tapilmadi.")