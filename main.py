class Pet():
    name = ''
    def __init__(self, name):
        self.name = name


class Cat(Pet):
    def make_noise(self):
        print('Мяу')

class Dog(Pet):
    def make_noize(self):
        print('Гав')

myAnimal = Pet('Tom')
print('his name', myAnimal.name)

myAnimal = Cat('Tom')
myAnimal.name
myAnimal.make_noise()

myAnimal = Dog('Tom')
myAnimal.name
myAnimal.make_noize()

