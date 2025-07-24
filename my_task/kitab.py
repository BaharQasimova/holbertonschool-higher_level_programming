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
        
    def main():
       library = Library("Ağıllı Kitabxana")
    
    while True:
        print("\nAğıllı Kitabxanaya xoş gelmisiz.")
        print("1. Kitab elave et.")
        print("2. Kitabları goster.")
        print("3. Kitab kiraye gotur.")
        print("4. Kitabı qaytar.")
        print("5. Çıxış")
        
        choice = input("Seçiminizi daxil edin (1-5): ")
        
        if choice == '1':
            title = input("Kitabın adını daxil edin: ")
            author = input("Kitabın muellifini daxil edin: ")
            library.add_book(title, author)
        
        elif choice == '2':
            library.display_books()
        
        elif choice == '3':
            title = input("Kiraye goturmek istediyiniz kitabın adını yazın: ")
            library.borrow_book(title)
        
        elif choice == '4':
            title = input("Qaytarmaq istediyiniz kitabın adını yazın: ")
            library.return_book(title)
        
        elif choice == '5':
            print("Sag olun, goruserik!")
            break
        
        else:
            print("Yanlış seçim. Zehmet olmasa 1-den 5-e qeder reqem daxil edin.")

if __name__ == "__main__":
    main()
