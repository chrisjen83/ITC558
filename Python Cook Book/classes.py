# Question 1

# class Book:
#     def __init__(self, title, author, page_number):
#         self.title = title
#         self.author = author
#         self.page_number = page_number
#
#     def length_of_book(self):
#         pass
#
#     def __str__(self):
#         title_formatter = ('Book Title: ' + self.title + '\n'
#                            'Author: ' + self.author + '\n'
#                            'Page Numbers: ' + self.page_number)
#
#         return title_formatter

# Question 2

class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    # Mutators
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    # Accessors
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def __str__(self):
        return f'Book Title: {self.__title}\nAuthor: {self.__author}\nPublisher: {self.__publisher}'

python_book = Book('Python for beginners', 'John Smith', 'Pub House')

python_book.set_title('New title')
print(python_book)
