from book import Book  
from library import Library  

library = Library()

while True:
    print("Kutuphane Otomasyonu\n")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara")
    print("4. Tum Kitaplari Listele")
    print("5. Cikis")

    choice = input("Seciminiz: ")

    if choice == "1":
        title = input("Kitap Basligi: ")
        author = input("Yazar: ")
        pages = input("Sayfa Sayisi: ")
        publisher = input("Yayinevi: ")
        isbn = input("ISBN: ")
        description = input("Aciklama: ")
        genre = input("Tur: ")
        num_copies = int(input("Kopya Sayisi: "))

        book = Book(title, author, pages, publisher, isbn, description, genre, num_copies)
        library.add_book(book)
        print("Kitap basariyla eklendi.\n")

    elif choice == "2":
        title = input("Silmek istediginiz kitabin adini girin: ")
        library.remove_book(title)
        print("Kitap basariyla silindi.\n")

    elif choice == "3":
        title = input("Aramak istediginiz kitabin adini girin: ")
        book = library.search_book(title)

        if book:
            print("Kitap bulundu:")
            print(book)
        else:
            print("Kitap bulunamadi.\n")

    elif choice == "4":
        books = library.get_books()

        if books:
            print("Mevcut kitaplar:")
            for book in books.values():
                print(book)
        else:
            print("Kütüphanede hic kitap yok.\n")

    elif choice == "5":
        print("Programdan cikiliyor...")
        break

    else:
        print("Lutfen gecerli bir secim yapin.\n")
