# A quick program exploring how class inheritance works in Python.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def __str__(self) -> str:
        return "I am an animal."

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "I am a fish."

    def breathe(self):
        super().breathe()
        print("Breathing water.")

    def swim(self):
        print("Swimming in water.")

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "I am a cat."

    def meow(self):
        print('I say, "Meow!"')

# Make a fish.
nemo = Fish()
print(nemo)
nemo.breathe()
nemo.swim()

print()

# Make a cat.
frumpkin = Cat()
print(frumpkin)
frumpkin.breathe()
frumpkin.meow()
