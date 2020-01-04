class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class EBook(Book):
    def __init__(self, title, author, file):
        super().__init__(title,author)
        self.file = file

class TextBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title,author)
        self.pages = pages 

e_obj_1 = EBook("XYZ", "John Doe", "dir1")
print(f"{e_obj_1.title} {e_obj_1.author} {e_obj_1.file}")
tb1 = TextBook("ABC", "Jane Doe", 600)
print(f"{tb1.title} {tb1.author} {tb1.pages}")
