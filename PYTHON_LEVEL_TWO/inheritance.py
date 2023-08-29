# INHERITANCE
class Animal():

    def __int__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')

class Dog(Animal):
    def __int__(self):
        # Animal.__int__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")
    def eat(self):
        print("DOG EATING")

# mya = Animal()
# # mya.__int__()
# mya.whoAMI()
# mya.eat()
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
# mydog.eat()
# SPECIAL METHODS
