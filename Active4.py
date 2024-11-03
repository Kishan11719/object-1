class Parrot:

    # instance attributes
    def __init__(self, name, age):
         self.name = name
         self.age = age

    # instance method
    def sing(self, song):
        return "{} is now dancing".format(song)

    def dance(self):
        return "{} is now dancing".format(self.name) 

# instantiate the object
blu = Parrot("Blu", 10)

# call our instantiat methods
print(blu.sing(" 'Happy' "))
print(blu.dance())