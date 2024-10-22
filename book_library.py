'''
Design and implement a simple Library Management System . The system should support the following operations:
Add a New Book:
     Input details: Name, Author, Genre,
     The system should assign a unique ID to each new book automatically.
Display Book Details:
     Display the details of all the books in the library.
Search for a Book by Name:
     Input the name of the book.
     Display the details of all books that match the search criteria.

'''

class Book():
    def __init__(self):
        self.books_store = []
    
    def addBook(self, name, author, genre):
        self.books_store.append({
            'name': name,
            'author': author,
            'genre': genre
        })
        
        self.books_index_name = {
            '[name of book]': len(self.books_store) - 1
        }
        
        print(f'Added book: {name}')
        return True
    
    def getAllBooks(self):
        print(f'Total books: {len(self.books_store)}')
        return self.books_store

    def getBookByName(self, book_name):
        for book in self.books_store:
            if book['name'] == book_name:
                return book
        
        raise Exception(f'Book with name: {book_name} is not found in book store')

book = Book()
book.addBook('a journey', 'sourabh', 'fiction')
print(book.getAllBooks())
print(book.getBookByName('a journey'))
print(book.getBookByName('a journ'))
