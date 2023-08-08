# Test Program for Lab Assignment 3.2 - ANIMALS

from Animals import Animal, Cat, Dog

def main():
    # Create a Cat
    cat = Cat("MingMing")
    cat.cat()
    cat.eat()
    cat.make_noise()
    print("---------------------------")

    # Create a two Dogs
    dog1 = Dog("Browny")
    dog1.dog()
    dog1.eat()
    dog1.make_noise()
    print("---------------------------")

    dog2 = Dog("Pinky")
    dog2.dog()
    dog2.eat()
    dog2.make_noise()
    print("---------------------------")

    # Create an Animal
    animal = Animal("Chuchu")
    animal.animal()
    animal.eat()
    animal.make_noise()

main()
