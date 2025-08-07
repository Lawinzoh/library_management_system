from exceptions.custom_exceptions import BookNotAvaialableError, BookNotFoundError
from models.library import Library
from models.users import User


class LibraryService:
    def __init__(self, library: Library) -> None:
        self.library = library
    
    def checkout_book(self, user: User, title: str):
        book = self.library.find_book(title)
        
        if book is None:
            """Raise a book not found exception."""
            raise BookNotFoundError(title)
            
        if not book.is_avaiable:
            """Raise a book not available exception."""
            raise BookNotAvaialableError(title)
            

        book.is_avaiable = False
        user.borrow_book(book)
        print(f"{user.name} has checked out '{book.title}'.")

    def return_book(self, user: User, title: str):
        book = se;f.library,find_book(title)

        if book is None:
            """Raise a book not found exception."""
            raise BookNotFoundError(title)
        
        if book in user.borrowed_books:
            user.return_book(book)
            book.is_avaiable = True
            print(f"{user.name} has returned '{book.title}'.")