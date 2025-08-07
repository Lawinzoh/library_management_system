class BookNotAvaialableError(Exception):
    """Exception raised when a book is not available in the library."""
    def __init__(self, book_title: str) -> None:
        super().__init__(f"The book '{book_title}' is not available in the library.")

class BookNotFoundError(Exception):
    """Exception raised when a book is not found in the library."""
    def __init__(self, book_title: str) -> None:
        super().__init__(f"The book '{book_title}' was not found in the library.")
