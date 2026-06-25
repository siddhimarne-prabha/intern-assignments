#11/06/2026 – OOP

#QUESTION 1: ABSTRACT CLASS & ABSTRACT METHOD

from abc import ABC, abstractmethod
# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Child Class
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

# Testing the code
car_object = Car()
car_object.start()

#_______________________________________________________________________________________



#QUESTION 2: Abstract Class with Multiple Child Classes

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




#QUESTION 3: POLYMORPHISM USING METHOD OVERRIDING

class Shape:
    def draw(self):
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

circle_obj = Circle()
rectangle_obj = Rectangle()


circle_obj.draw()
rectangle_obj.draw()
#_______________________________________________________________________________________



#QUESTION 4: POLYMORPHISM WITH LOOP

class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")


birds_list = [Sparrow(), Eagle()]
for bird in birds_list:
    bird.fly()
#_______________________________________________________________________________________



#QUESTION 5: ABSTRACT CLASS + POLYMORPHISM

from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")


employees_list = [Developer(), Designer()]


for employee in employees_list:
    employee.work()

    