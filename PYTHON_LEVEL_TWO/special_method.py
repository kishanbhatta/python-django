class Book():
    def __init__(self,title,author,pages):
        print ("A bok is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s, author:%s, pages:%s"%(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "jose Portilla", 159)

print book
print len(book)
del book