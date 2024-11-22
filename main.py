class Book():
    def __init__(self, title: str, author: str, price: float, quantity: int) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage: int):
        self.price = self.price * (1 - discount_percentage)

    def sell(self, amount: int):
        if self.quantity - amount >= 0:
            self.quantity -= amount
        else:
            print('There are no enough books to take!')

    def __str__(self) -> str:
        return f'Title: {self.title}, author: {self.author}, price: ${self.price}, quantity: {self.quantity}'


class BookStore():
    def __init__(self, books: list[Book]):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def search(self, search_query: str) -> list[str]:
        return list(
            map(
                lambda book: str(book),
                list(
                    filter(lambda book: (search_query.lower() in book.title.lower()), self.books)
                ))
        )

    def calculate_total_value(self):
        return sum(book.price * book.quantity for book in self.books)


book1 = Book('title', 'author', 1.22, 3)
book2 = Book('title2', 'author', 4.5, 2)

book_store = BookStore([book1, book2])

print(book_store.search('titl'))

print(book_store.calculate_total_value())