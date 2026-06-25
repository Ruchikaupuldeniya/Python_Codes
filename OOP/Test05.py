class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species="Dog")
        self.breed = breed

    def sound(self):
            return "Woof !" 

class Bird:
    def sound(self):
            return "Chirp!" 
    

class Cat(Animal):
    def sound(self):
            return "Meow!" 

animals =[Dog("Rex","Labrador"),Bird(),Cat("Kiti","Cat")]


for animal in animals:
     print(f"{animal.name if hasattr(animal,'name') else 'unknown'} says:animal.sound()")
