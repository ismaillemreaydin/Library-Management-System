class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("Kütüphane boş.")
        else:
            print("*** Kitaplar ***")
            for book in books:
                print(book.strip())

    def add_book(self):
        title = input("Kitap Başlığı: ")
        author = input("Yazar: ")
        publication_year = input("Yayın Tarihi: ")
        page_count = input("Sayfa Sayısı: ")
        book_info = f"{title},{author},{publication_year},{page_count}\n"
        self.file.write(book_info)
        self.file.write("\n")  # Yeni satır ekle
        print("Kitap başarıyla eklendi.")

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        removed = False
        for book in books:
            if title not in book:
                self.file.write(book)
            else:
                removed = True
        if removed:
            print(f"{title} başlıklı kitap kaldırıldı.")
        else:
            print(f"{title} başlıklı kitap bulunamadı.")

    def get_book_list(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        return books

# Library sınıfı ile bir nesne oluşturun
lib = Library()

# Kullanıcı girişi ile etkileşim kurmak için bir menü oluşturun
while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listeleyin")
    print("2) Kitap Ekle")
    print("3) Kitabı Kaldır")
    print("q) Çıkış")
    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        title = input("Kaldırılacak Kitap Başlığı: ")
        lib.remove_book(title)
    elif choice == 'q':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")