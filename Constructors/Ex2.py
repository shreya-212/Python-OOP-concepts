class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

b1=Book("Programming","ABC",200)
b1.book_info()