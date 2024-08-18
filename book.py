
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self): 
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    

