# 11.01
class Dog:
    def __init__(self, name):
        self.name = name
dog = Dog('Charlie')
print('his name', dog.name)

#11.02
class Dog:
    def __init__(self, name):
        self.name = name
dog = Dog('Charlie')
print('his name', dog.name)

class Dog_1(Dog):
    def make_noize(self):
        print('Gav')
dog = Dog_1('Charlie')
dog.make_noize()

#11.03
class Dog:
    def jump():
        print('Jump')
    def run():
        print('Run')
Dog.jump()
Dog.run()

#11.04
class Dog:
    def __init__(self, name, age, heigth, weigth):
        self.name = name
        self.age = age
        self.heigth = heigth
        self.weigth = weigth
    def dog_parametrs(self):
        print(f'Dog perametrs: name -  {self.name}, age - {self.age}, heigth - {self.heigth}, weigth - {self.weigth}')
    def jump(self):
        print('Jump')
    def run(self):
        print('Run')
    def bark(self):
        print('Woof Woof')
dog = Dog('Charlie', 10, 2, 25)
dog.dog_parametrs()
dog.jump()
dog.run()
dog.bark()
#11.05
class New_name(Dog):
    def change_name(self, name, age, heigth, weigth):
        self.name = name
        self.age = age
        self.heigth = heigth
        self.weigth = weigth
        print('new name is', self.name)
dog = New_name('Tomas', 10, 2, 25)
dog.change_name('Tomas', 10, 2, 25)



