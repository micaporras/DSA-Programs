# Designed Class for Lab Assignment 3.2 - ANIMALS

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print("Munch munch.")
    
    def make_noise(self, noise="Grrr"):
        print(f"{noise} says {self.name}.")
    
    def animal(self, animal_type="Animal"):
        print(f"A/An {animal_type} has been born.")
    

class Cat(Animal):
    def make_noise(self):
        return super().make_noise("Meow")
    
    def cat(self):
        return super().animal("Cat")



class Dog(Animal):
    def make_noise(self):
        return super().make_noise("Bark")
    
    def dog(self):
        return super().animal("Dog")




    



