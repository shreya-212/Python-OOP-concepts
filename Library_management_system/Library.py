class Book:
    def __init__(self,title,author,isbn,available):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available

    def __str__(self):
        return f"Title:{self.title}| Author:{self.author}|Isbn:{self.isbn}|Available:{self.available}"
    
class Library:
    def __init__(self):
        self.books=[]

    def add_books(self,book):
        for b in self.books:
            if b.isbn==book.isbn:
                print("Book already exists in library")
                return
        self.books.append(book)
        print("Book added to the library")

    def display_books(self):
        if not self.books:
            print("No books in library")
        else:
            for b in self.books:
                print(b)
        

    def borrow_book(self,isbn):
        for b in self.books:
            if b.isbn==isbn:
                if b.available:
                    b.available=False
                    print("Book borrowed successfullly")
                    return
                else:
                    print("Book already borrowed")
                    return
        print("Book not found")
        
    
    def return_book(self,isbn):
        for b in self.books:
            if b.isbn==isbn:
                if b.available==False:
                    b.available=True
                    print("Book returned successfully")
                else:
                    print("The book was not borrowed")
                return
        print("No book found")

def main():
    lib=Library()
    
    while True:
        print("----Library Management System----")
        print("1.Add Book")
        print("2.View all books")
        print("3.Borrow book")
        print("4.Return book")
        print("5.Exit")

        try:
            choice=int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice")
            continue
        if choice==1:
            title=input("Enter title: ")
            author=input("Enter author: ")
            isbn=input("Enter isbn no: ")
            available=True
            book=Book(title,author,isbn,available)
            lib.add_books(book)

        elif choice==2:
            lib.display_books()

        elif choice==3:
            isbn=input("Enter isbn of book to be issued: ")
            lib.borrow_book(isbn)

        elif choice==4:
            isbn=input("Enter the isbn of book to be returned: ")
            lib.return_book(isbn)

        elif choice==5:
            print("Exiting")
            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()

            

    

       
        


    
        
        