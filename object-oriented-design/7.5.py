class BookReader:
    def __init__(self):
        self.books = {}
        self.users = []
    def handle_user_borrow_book(self,user):
        response = input("Which book would you like to borrow?"+ ", ".join(book.title for book in self.books if book.is_available) +"\n")
        if response in self.books.keys():
            book = self.books[response]
            user.borrowed_books.append(book)
            print(book.title + "is borrowed")
            book.is_available = False
            return
        else:
            print("Book not available")
            return
    def handle_user_return_book(self,user):
        response = input("Which book would you like to return?"+ [book.title for book in user.borrowed_books] +"\n")
        if response in user.borrowed_books:
            book = user.borrowed_books[response]
            user.borrowed_books.remove(book)
            book.is_available = True
            print(book.title + "is returned")
        else:
            print("Book not borrowed")
        return



class Book:
    def __init__(self,title):
        self.title = title
        self.is_available = True

class Users:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []

if __name__ == "__main__":
    bookreader = BookReader()
    bookreader.books = [Book("book1"), Book("book2"), Book("book3")]
    bookreader.users = [Users("user1"), Users("user2"), Users("user3")]
    bookreader.handle_user_borrow_book(bookreader.users[0])
    bookreader.handle_user_return_book(bookreader.users[0])
