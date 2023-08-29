# class Dog():
#
#     def __int__(self, dogBreed, dogEyeColor):
#         self.breed = dogBreed
#         self.eyeColor = dogEyeColor
# tomita = Dog("Fox Terrirer","brown")
# print("This dog is a",tomita.breed,"and its eyes are",tomita.eyeColr)

class Dog:
    def __int__(self, dogBreed="German Shepherd", dogEyeColor="Brown"):
        self.breed = dogBreed
        self.eyeColor = dogEyeColor
tomita = Dog()
print("This dog is a ",tomita.breed,"and its eyes are",tomita.eyeColor)