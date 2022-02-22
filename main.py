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

tom = Cat('Tom')
tom.name
tom.make_noise()

Tom = Dog('Tom')
Tom.name
Tom.make_noize()

