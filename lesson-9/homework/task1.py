class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self,id,title,author,is_borrowed=False):
        self.id=id
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def __str__(self):
        return f"{self.id}, {self.title}, {self.author}, {'borrowed' if self.is_borrowed else 'not borrowed'}"

class Member:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.borrowed_books=[]
    def borrow(self,book):
        if len(self.borrowed_books)<3:
            self.borrowed_books.append(book)
        else:
            try:
                raise MemberLimitExceededException("You cannot borrow more than 3 books")
            except MemberLimitExceededException as e:
                print(f"Caught an error: {e}")
    def __str__(self):
        return f"{self.id}, {self.name}, {self.borrowed_books}"
class Library:
    def __init__(self):
        self.books={}
        self.members={}
    
    def borrow(self,id,book_id):
        if book_id not in list(self.books.keys()):
            try:
                raise BookNotFoundException("This book is not found")
            except BookNotFoundException as e:
                print(f"Caught an error: {e}")
        elif self.books[book_id].is_borrowed:
            try:
                raise BookAlreadyBorrowedException("This book is already borrowed")
            except BookAlreadyBorrowedException as e:
                print(f"Caught an error: {e}")
        else:
            if id in list(self.members.keys()):
                self.members[id].borrow(self.books[book_id])
                self.books[book_id].is_borrowed=True
    def return_book(self,id,book_id):
        if book_id not in list(self.books.keys()):
            try:
                raise BookNotFoundException("This book is not found")
            except BookNotFoundException as e:
                print(f"Caught an error: {e}")
        else:
            if id in list(self.members.keys()):
                self.members[id].borrowed_books.remove(self.books[book_id])
                self.books[book_id].is_borrowed=False
    def __str__(self):
        msg=""
        for member in list(self.members.values()):
            msg=msg+str(member)+"\n"
        for book in list(self.books.values()):
            msg=msg+str(book)+"\n"
        return msg

my_library=Library()
my_library.books={
    1: Book(1, "To Kill a Mockingbird", "Harper Lee"),
    2: Book(2, "1984", "George Orwell"),
    3: Book(3, "The Great Gatsby", "F. Scott Fitzgerald"),
    4: Book(4, "Moby-Dick", "Herman Melville"),
    5: Book(5, "Pride and Prejudice", "Jane Austen"),
    6: Book(6, "War and Peace", "Leo Tolstoy"),
    7: Book(7, "The Catcher in the Rye", "J.D. Salinger"),
    8: Book(8, "The Hobbit", "J.R.R. Tolkien"),
    9: Book(9, "Fahrenheit 451", "Ray Bradbury"),
    10: Book(10, "Crime and Punishment", "Fyodor Dostoevsky")
}
my_library.members={
    101: Member(101, "Alice Johnson"),
    102: Member(102, "Bob Smith"),
    103: Member(103, "Charlie Brown"),
    104: Member(104, "David Wilson"),
    105: Member(105, "Emma Davis"),
    106: Member(106, "Frank Miller"),
    107: Member(107, "Grace Lee"),
    108: Member(108, "Hannah Martin"),
    109: Member(109, "Ian Thompson"),
    110: Member(110, "Jack White")
}
print(my_library.books[2].is_borrowed)
my_library.borrow(101,60) #intentional error


my_library.borrow(101,2)
print(my_library.books[2].is_borrowed)
my_library.borrow(101,2) #intentional error

print(my_library)

my_library.return_book(101,2)
print(my_library)

