# =========================================================================================== #
#                    Fundamentals of Object Oriented Programming in Python                    #
# =========================================================================================== #

# Define a string & an integer object
number = 1 # int
name = 'Gorkem' # str

# Check the type of them
print(type(number))
print(type(name))
# Note: As we may see they're just the objects of their classes. Meaning, e.g. Gorkem is an object of the string class.

# Define a function and check its type
def sayHello():
    print('Hello')

print(type(sayHello)) # It's an object of the function class.

# Define a string and use its methods
welcome = 'Welcome!'
print(welcome.upper())

# So, we've seen built-in classes so far. Now we're going to create our own classes.
class Dog:
    def barkTwice(self):
        print('bark' + ' ' + 'bark')

    def bark(self):
        print('bark')

# Create an object of the class dog & check its type as we did before
d = Dog()
print(type(d))

# Use the methods of the dog class
d.bark()
d.barkTwice()

# Define another class to do addition and subtraction operations.
class mathOperations:
    def addOne(self, x):
        return x + 1
    def subOne(self, x):
        return x - 1

# Let's see if it works correctly
number = mathOperations()
print(number.addOne(5))
print(number.subOne(2))

# Create another class with mutliple attributes
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def sayMeow(self):
        print('Meow')

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

# Create an object of the cat class
c = Cat('Princess', 2)

# To get the name of the cat we could use two ways
print(f'The name of the cat is {c.name}')
print(f'The name of the cat is {c.getName()}')

# Create another cat called c2
c2 = Cat('Coffee', 3)

# Get the name of the cat 2
print(f'The name of the second cat is {c2.getName()}')

# Change the age of the cat one using setAge method that we defined
c2.setAge(5)

# Check its age after we change it
print(f'The age of the first cat right after we change it: {c2.getAge()}')

# So we've worked with a single class so far. Let's jump into working with multiple classes
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # between 1-100

    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        return False

    def getAverageGrade(self):
        averageGrade = 0
        for student in self.students:
            averageGrade += student.getGrade()

        return averageGrade / len(self.students)

# Define a couple of students
s1 = Student('Gorkem', 25, 96)
s2 = Student('Recep', 25, 90)
s3 = Student('Ali', 23, 88)

# Create a course & add the students that we created
course = Course('Physics', 2)
course.addStudent(s1)
course.addStudent(s2)

# Check the Average grade of the Physics Course
print(course.getAverageGrade())