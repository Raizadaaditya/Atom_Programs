'''
Introducing how class and object works
'''


class Parrot:
    # class attribute
    species = 'bird'

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiating the Parrot class
blue = Parrot('Blue', 10)
woo = Parrot('Woo', 15)

# accessing class attribute
print("Blue is a {}".format(blue.__class__.species))

print("Woo is also a {}".format(woo.__class__.species))

# accessing instance attribute
print("{} is {} years old".format(blue.name, blue.age))

print("{} is {} years old".format(woo.name, woo.age))
