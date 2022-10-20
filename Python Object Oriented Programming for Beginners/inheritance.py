# =========================================================================================== #
#                                The Concept of the Inheritance                               #
# =========================================================================================== #

# Define two classes called cat & dog
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Meow!')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Bark!')

# As we may see the only difference between them is the speak method. So, instead of writing the same properties separately, we could use another way called inheritance.
# Inheritance basically allows us to define a class that inherits all the methods and properties from another class.

# Let's create a parent class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print('I dunno what to say') # If there is a method defined in the lower class that has the same name, it'll automatically overwrite that method.

# Create the child class called Dog
class Dog(Pet):
    def speak(self):
        print('Bark!')

# Create the other child class called Cat
class Cat(Pet):
    def speak(self):
        print('Meow!')

# Create an object of the Pet Class
p1 = Pet('Prenses', 2)
p1.show()

# Let's check if the Cat class inherits the properties from the Pet Class
c1 = Cat('Balim', 2)
c1.show()

# Do the same for Dog Class
d1 = Dog('Blue', 3)
d1.show()

# Check the speak methods
c1.speak()
d1.speak()

# Create another child class without any methods
class Fish(Pet):
    pass

# Define an object of the Fish Class & use the methods of the parent class
f1 = Fish('Jake', 5)
f1.show()

# Create another class and add another attribute called color
class Bird(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old. Also I am {self.color}')

# Create an object of Bird Class
b1 = Bird('Honey', 6, 'Green')
b1.show()

# Let's dive into attributes a little more
# Create another class called Person
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # This method is not going to be specific to an instance. Meaning, they act on the class itself, they don't have access to any instance.
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# Create a couple of objects of the Person Class
p1 = Person('Recep')
p2 = Person('Ali')
print(Person.number_of_people_())