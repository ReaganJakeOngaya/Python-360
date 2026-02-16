class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting down.')
        
    def roll(self):
        print(f'{self.name} is now rolling over.')
        
my_dog = Dog('Buddy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll()