# Age old animals example to learn about objects

class Dog:
    # Class attributes
    species = "Canine"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"Hi! I am {self.name} and I'm {self.age} years old."

    def speak(self, sound):
        return f"{self.name} barks "+f"{sound} "*2


class Terrier(Dog):
    def speak(self, sound='Woof'):
        # Inherit parent class method
        return super().speak(sound)
    

class Bulldog(Dog):
    def speak(self, sound="Rufff"):
        # Override parent class method
        return f"{self.name} says "+f"{sound} "*2

if __name__ == "__main__":
    miles = Bulldog("Miles", 4)
    print(type(miles))
    simba = Terrier("Simba", 6)
    # print(miles.name)
    # print(simba.age)
    # simba.age = 8
    # print(simba.age)
    # print(miles.species)
    
    # Call instance methods
    print(simba)
    print(simba.speak())
    print(miles)
    print(miles.speak())