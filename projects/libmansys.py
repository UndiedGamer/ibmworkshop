class Library:
    def __init__(self, name, books, members):
        self.name = name
        self.books = books
        self.members = members

    def take_book(self, book, member):
        got_member = self.members.get(member)
        got_book = self.books.get(book)
        if not got_member or not got_book:
            print("Member or book not found")
        else:
            self.members.update({member: {"books": got_member.get('books')+1, "book_taken": got_member.get('book_taken')+[book]}})
    
    def return_book(self, book, member):
        got_member = self.members.get(member)
        got_book = self.books.get(book)
        if not got_member or not got_book:
            print("Member or book not found")
        else:
            got_member.get('book_taken').remove(book)
            self.members.update({member: {"books": got_member.get('books')-1, "book_taken": got_member.get('book_taken')}})
    
lamrin = Library(name="lamrin", books=
                {
                    "English Comm Skills": {
                        "author": "Krishna",
                        "price": 500,
                        "count": 5,
                        "pages": 220,
                    },
                    "AIML": {
                        "author": "Raesh",
                        "price": 2000,
                        "count": 10,
                        "pages": 1200,
                    },
                    "DSA": {"author": "ramesh", "price": 800, "count": 20, "pages": 50},
                }
            , members=
                {
                    "H": {"books": 0, "book_taken": []},
                    "Car": {"books": 0, "book_taken": []},
                }
            )

lamrin.take_book("DSA", "H")
lamrin.take_book("AIML", "Car")
lamrin.take_book("AIML", "H")

print(lamrin.members)
lamrin.return_book("DSA", "H")
print(lamrin.members)