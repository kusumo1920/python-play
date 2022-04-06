class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name & age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to command."""
        print(f"{self.name} rolled over.")

my_dog = Dog('Doge', 7)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")