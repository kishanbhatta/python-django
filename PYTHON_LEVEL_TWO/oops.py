# Object Oriented Programming is a away to use Python to create our own objects.
# class Sample():
#     pass
# x = Sample()
# print(type(x))
print(type(()))  #It prints <type 'tuple'>
print(type([]))  #It prints <type 'list'>
print(type(200)) # It will prints <type 'int'>
print(type(20.0)) # It will prints <type 'float>
class Sample():
    pass
x = Sample()
print(type(x))  # It will print <type 'instanece'>

class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed, name):
        self.breed = breed
        self.name = name
#mydog = Dog(breed = "Lab", name = "Julie")
mydog = Dog("Lab", "julie")  # Alternative for above line of code but have to put in order
#otherdog = Dog(breed = "Huskie") # it will give us the out put as Huskie
print(type(mydog))  # it will show the output of the dog class
print(mydog.breed)  # it will show the output as the breed is Lab
print(mydog.name)
print(mydog.species)
#print(otherdog.breed)

