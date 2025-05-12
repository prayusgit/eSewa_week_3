from abc import ABC, abstractmethod

# Abstract Iterator
class IteratorInterface(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

# Abstract collection
class Collection(ABC):
    @abstractmethod
    def __iter__(self):
        pass


# Concrete Iterator
class BookIterator(IteratorInterface):
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration


# Concrete Collection
class BookCollection(Collection):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)


# Client Code
book_collection = BookCollection()
book_collection.add_book("Harry Potter")
book_collection.add_book("Star Wars")
book_collection.add_book("Pirates of the Carrabian.")

for item in book_collection:
    print(item)
