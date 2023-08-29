# INHERITANCE
# class Animal():
#
#     def __int__(self):
#         print("ANIMAL CREATED")
#
#     def whoAmI(self):
#         print("ANIMAL")
#
#     def eat(self):
#         print('EATING')
#
#
# class Dog(Animal):
#     def __int__(self):
#         # Animal.__int__(self)
#         print("DOG CREATED")
#
#     def bark(self):
#         print("WOOF")
#
#     def eat(self):
#         print("DOG EATING")
#
#
# # mya = Animal()
# # # mya.__int__()
# # mya.whoAMI()
# # mya.eat()
# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()


# mydog.eat()

# SPECIAL METHODS
# class Book():
#     def __int__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author,self.pages)
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print("a book is destroyed!")
#
#     b = Book("Python","Jose",200)
# del b
# len(len(b))
# print(b)
# # mylist = [1, 2, 3]
# # print(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")

# b = Book()
b = Book("Python", "jose", 200)
del b
# print(len(b))
# print(b)
