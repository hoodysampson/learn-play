class Animal:

    def reply(self):
        print(self.msg)


class Mammal(Animal):
    msg='mama'
    
    def speak(self):
        super().reply()

class Cat(Mammal):
    msg='meow'

    def speak(self):
        super().reply()


class Dog(Mammal):
    msg = 'woof'

    def speak(self):
        super().reply()


class Primate(Mammal):
    msg = 'Hello World'

    def speak(self):
        super().reply()


class Hacker(Primate):
    pass


c=Cat()
c.speak()
m=Mammal()
m.speak()
h=Hacker()
h.reply()