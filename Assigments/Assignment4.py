
#I have run this code and checked it

#SECTION 1: MODULES

#Challenge 1: Calculator Module
#calculator.py-*********
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#main.py_****
import calculator

num1 = 10
num2 = 5

print("Add:", calculator.add(num1, num2))
print("Subtract:", calculator.subtract(num1, num2))
print("Multiply:", calculator.multiply(num1, num2))
print("Divide:", calculator.divide(num1, num2))


#____________________________________________________________________________________________


#Challenge 2: Employee Module

#employee.py-******
name = "siddhi"
salary = 50000

def show_details():
    print("Employee Name:", name)
    print("Monthly Salary:", salary)

#main.py-*****
import employee
employee.show_details()


#_______________________________________________________________________________________________

#Challenge 3: Using the Math Module

import math


root = math.sqrt(144)
print("Square root of 144 is:", root)

pi_val = math.pi
print("Value of Pi is:", pi_val)


fact = math.factorial(6)
print("Factorial of 6 is:", fact)

#_____________________________________________________________________________________

#Challenge 4: Using the Random Module

import random


num = random.randint(1, 100)
print("Random Number:", num)


languages = ['Python', 'Java', 'React', 'Django']
choice = random.choice(languages)
print("Random Choice:", choice)

#___________________________________________________________________________

#Challenge 5: Custom Area Module
#area.py-***************
import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

#main.py-********
import area

circle_result = area.area_circle(5)
print("Circle Area:", circle_result)

rect_result = area.area_rectangle(10, 4)
print("Rectangle Area:", rect_result)



#_____________________________________________________________________________________
#SECTION 2: CLASSES & OBJECTS

#Challenge 6: Student Class
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("siddhi", 15)

print(s1.name, s1.age)

#_____________________________________________________________________________________________

#Challenge 7: Car Class

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


c1 = Car("Toyota", "Corolla")
c2 = Car("Ford", "Mustang")


print(c1.brand, c1.model)
print(c2.brand, c2.model)
#______________________________________________________________________________________________

#Challenge 8: Book Class

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("Shyamchi Aai", "sane guruji", 200)
b2 = Book("Mrityunjay", "shivaji sawant", 300)
b3 = Book("Yayati", "V.S.Khandekar",250)

print(b1.title, b1.author, b1.price)
print(b2.title, b2.author, b2.price)
print(b3.title, b3.author, b3.price)

#___________________________________________________________________________________________

#Challenge 9: Laptop Class

class Laptop:

    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

L1 = Laptop("Dell", "16GB", 800)
L2 = Laptop("Apple", "8GB", 1200)


print(L1.brand, L1.ram, L1.price)
print(L2.brand, L2.ram, L2.price)

#__________________________________________________________________________________________

#Challenge 10: Mobile Class

class Mobile:

    def __init__(self, company, model, storage):
        self.company = company
        self.model = model
        self.storage = storage


m1 = Mobile("Apple", "iPhone 15", "128GB")
m2 = Mobile("Samsung", "Galaxy S24", "256GB")
m3 = Mobile("Google", "Pixel 8", "128GB")


print(m1.company, m1.model, m1.storage)
print(m2.company, m2.model, m2.storage)
print(m3.company, m3.model, m3.storage)

#__________________________________________________________________________________________

#SECTION 3: CONSTRUCTOR (init)
#Challenge 11: Employee Class

class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

e1 = Employee(101, "John", 50000)

print(e1.id, e1.name, e1.salary)

#____________________________________________________________________________________________

#Challenge 12: BankAccount Class

class BankAccount:

    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance


a1 = BankAccount(4455, "siddhi", 1200)
a2 = BankAccount(6677, "riya", 2500)

print(a1.number, a1.name, a1.balance)
print(a2.number, a2.name, a2.balance)

#____________________________________________________________________________________________

#Challenge 13: Movie Class

class Movie:

    def __init__(self, name, hero, rating):
        self.name = name
        self.hero = hero
        self.rating = rating



m1 = Movie("Dhurandar", "Ranbir Singh", 4.8)

print(m1.name, m1.hero, m1.rating)

#________________________________________________________________________________________

#Challenge 14: Product Class

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

p1 = Product(1, "Pen", 2)
p2 = Product(2, "Book", 10)
p3 = Product(3, "Bag", 25)


print(p1.id, p1.name, p1.price)
print(p2.id, p2.name, p2.price)
print(p3.id, p3.name, p3.price)

#____________________________________________________________________________________________

#Challenge 15: College Class

class College:

    def __init__(self, name, city, count):
        self.name = name
        self.city = city
        self.count = count

c1 = College("zeal", "pune", 12000)
c2 = College("JSPM", "pune", 16000)


print(c1.name, c1.city, c1.count)
print(c2.name, c2.city, c2.count)

#________________________________________________________________________________________

#SECTION 4: self KEYWORD
#Challenge 16: Person Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

p1 = Person("siddhi", 20)
p1.show()

#______________________________________________________________________________________________

#Challenge 17: Animal Class

class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print(self.name, self.color)



a1 = Animal("Lion", "Yellow")
a1.info()

#_______________________________________________________________________________________

#Challenge 18: Vehicle Class

class Vehicle:

    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print(self.company, self.model)


v1 = Vehicle("Tesla", "Model 3")
v1.display()

#_________________________________________________________________________________________

#Challenge 19: Teacher Class

class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def details(self):
        print(self.name, self.subject)


t1 = Teacher("shewta", "Math")
t1.details()

#_______________________________________________________________________________________________

#Challenge 20: Player Class

class Player:

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def print_details(self):
        print(self.name, self.team)


p1 = Player("Messi", "Miami")
p1.print_details()

#________________________________________________________________________________________

#SECTION 5: INSTANCE ATTRIBUTES
#Challenge 21: Student Class

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


# Create three objects
s1 = Student("siddhi", 10, 85)
s2 = Student("riya", 11, 92)
s3 = Student("ishwari", 12, 78)


print(s1.name, s1.roll_no, s1.marks)
print(s2.name, s2.roll_no, s2.marks)
print(s3.name, s3.roll_no, s3.marks)
#_____________________________________________________________________________________________

#Challenge 22: Employee Class

class Employee:

    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

e1 = Employee(101, "siddhi", "HR")
e2 = Employee(102, "ishwari", "IT")

print(e1.id, e1.name, e1.dept)
print(e2.id, e2.name, e2.dept)

#_________________________________________________________________________________________

#Challenge 23: Hospital Class

class Hospital:

    def __init__(self, doctor, special):
        self.doctor = doctor
        self.special = special


s
d1 = Hospital("Dr. Siddhi", "Heart")
d2 = Hospital("Dr. riya", "Brain")
d3 = Hospital("Dr. ishwari", "Eyes")

print(d1.doctor, d1.special)
print(d2.doctor, d2.special)
print(d3.doctor, d3.special)

#_____________________________________________________________________________________

#Challenge 24: Course Class

class Course:

    def __init__(self, name, duration, fees):
        self.name = name
        self.duration = duration
        self.fees = fees

c1 = Course("Python", "2 Months", 100)

print(c1.name, c1.duration, c1.fees)

#______________________________________________________________________________________________


#Challenge 25: CricketPlayer Class

class CricketPlayer:

    def __init__(self, name, runs, matches):
        self.name = name
        self.runs = runs
        self.matches = matches

p1 = CricketPlayer("Kohli", 13000, 290)

print(p1.name, p1.runs, p1.matches)

#___________________________________________________________________________________________-

#Challenge 26: Rectangle Class

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


r1 = Rectangle(5, 4)
print(r1.calculate_area())

#_____________________________________________________________________________________________-


#Challenge 27: Circle Class

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

c1 = Circle(7)
print(c1.calculate_area())

#_______________________________________________________________________________________


#Challenge 28: Employee Class

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  

    def annual_salary(self):
        return self.salary * 12

e1 = Employee("siddhi", 4000)
print(e1.annual_salary())

#____________________________________________________________________________________


#Challenge 29: Student Class

class Student:

    def __init__(self, name, marks, total):
        self.name = name
        self.marks = marks
        self.total = total

    def calculate_percentage(self):
        return (self.marks / self.total) * 100



s1 = Student("siddhi", 450, 500)
print(s1.calculate_percentage())

#_______________________________________________________________________________________


#Challenge 30: BankAccount Class

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

print(account.balance)

#________________________________________________________________________________________________

