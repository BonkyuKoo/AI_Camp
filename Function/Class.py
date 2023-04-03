class Animal:

 def __init__(self, name, species):
     self.name = name
     self.species = species

 def make_sound():
    print('The animal makes a sound')
    return
    


class Dog(Animal):
    
    def __init__(self, name, breed):
       super().__init__(name, species ='Dog')
       self.breed = breed

    def make_sound():
       print('Woof!')

class Cat(Animal):
    
    def __init__(self, name, species):
       super().init(self, name, species)

    def make_sound():
       print('Meow!')
    

dog1 = Dog('Fido', 'Golden Retriever')
cat1 = Cat('Fluffy', 'White')

print(dog1.name)
print(cat1.name)

dog1.make_sound()
cat1.make_sound()