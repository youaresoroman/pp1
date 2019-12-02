class ebook():
    def __init__(self, tytul, autor, stron, nr_strony):
        self.opened = False
        self.tytul = tytul
        self.autor = autor
        self.stron = stron
        self.nr_strony = nr_strony
        
    def open(self):
        self.opened = True
        
    def close(self):
        self.opened = False
        
    def summary(self):
        print(f"This book have {self.stron} pages")
    
    def read(self, pages):
        if self.opened:
            self.nr_strony += pages
        else:
            print(f'This book is closed')
    
    def status(self):
        if self.opened:
            #print(f'This book is opened')
            print(f'Autor                : {self.autor}')
            print(f'Tytuł                : {self.tytul}')
            print(f'Liczba stron         : {self.stron}')
            print(f'Numer bieżącej strony: {self.nr_strony}')
        else:
            print(f'This book is closed')

book = ebook("1984","George Orwell", 328, 1)
book.status()
book.open()
book.status()
book.read(50)
book.status()
book.close()
book.read(50)