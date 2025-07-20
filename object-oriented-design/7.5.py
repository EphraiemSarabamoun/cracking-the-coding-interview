class BookReader:
    def __init__(self):
        self.books = {}
        self.users = {}

    def handle_user_borrow_book(self,user):
        response = input("Which book would you like to borrow?"+ str(self.books.keys()) +"\n")
        if response in self.books and self.books[response].is_available:
            self.books[response].is_available = False
            user.borrowed_books[response] = self.books[response]
            print(response + " is borrowed")
            return
        else:
            print("Book not available")
            return
    def handle_user_return_book(self,user):
        response = input("Which book would you like to return?"+ str(user.borrowed_books.keys())+"\n")
        if response in user.borrowed_books and user.borrowed_books[response].is_available == False:
            user.borrowed_books.pop(response)
            self.books[response].is_available = True
            print(response + " is returned")
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
        self.borrowed_books = {}

if __name__ == "__main__":
    bookreader = BookReader()
    bookreader.books = {"book1": Book("book1"), "book2": Book("book2"), "book3": Book("book3")}
    bookreader.users = {"user1": Users("user1"), "user2": Users("user2"), "user3": Users("user3")}
    bookreader.handle_user_borrow_book(bookreader.users["user1"])
    bookreader.handle_user_return_book(bookreader.users["user1"])
