#16/06/2026 – Abstraction

#Question 1: Abstract Class & Abstract Method

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Child Class implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car is starting.........")


car_object = Car()
car_object.start()

#_______________________________________________________________________________________

#Question 2: Abstract Class with Multiple Child Classes

from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog_object = Dog()
cat_object = Cat()

dog_object.sound()
cat_object.sound()

#_______________________________________________________________________________________

#Question 3: Polymorphism Using Method Overriding

class Shape:
    def draw(self):
        print("Drawing a generic shape")

# Child class 1 overrides draw()
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

# Child class 2 overrides draw()
class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

circle_object = Circle()
rectangle_object = Rectangle()

circle_object.draw()
rectangle_object.draw()


#_______________________________________________________________________________________


#Question 4: Polymorphism with Loop

class Bird:
    def fly(self):
        print("Bird is flying")

# Child class 1 overrides fly()
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies low")

# Child class 2 overrides fly()
class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")


birds_list = [Sparrow(), Eagle()]


for bird in birds_list:
    bird.fly()


#_______________________________________________________________________________________


#Question 5: Abstract Class + Polymorphism

from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

# Child class 1 implements work()
class Developer(Employee):
    def work(self):
        print("Developer writes code")

# Child class 2 implements work()
class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")


employees_list = [Developer(), Designer()]

for employee in employees_list:
    employee.work()

 #_______________________________________________________________________________________