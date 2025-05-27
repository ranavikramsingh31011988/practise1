class Animal:
    def speak(self):
        print("Animal speaks")
class Mammal(Animal):
    def breathe(self):
        print("Mammal breathes")
class Bird(Animal):
    def fly(self):
        print("Bird fly and fly")
class Bat(Mammal, Bird):  # Bat inherits from both Mammal and Bird
    def hang(self):
        print("Bat hangs upside down")
# Creating an object of the Bat class
bat = Bat()
bat.speak()  # Inherited from Animal
bat.breathe()  # Inherited from Mammal
bat.fly()  # Inherited from Bird
bat.hang()  # Defined in Bat
