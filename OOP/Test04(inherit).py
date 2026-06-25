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

class Bird(Animal):
    def __init__(self,name,color):
        super().__init__(name,species="Bird")
        self.color = color  

         


dog1 = Dog("Buddy","Golden Retriever")


print(f"{dog1.name} is a {dog1.species} of breed {dog1.breed}.It says: {dog1.sound()}")


