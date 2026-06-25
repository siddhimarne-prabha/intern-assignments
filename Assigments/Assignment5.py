
 # 08/06/2026 – OOP


#Q1

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age   


student1 = Student("siddhi", 20)
student2 = Student("ishwari", 22)
student3 = Student("riya", 19)

print(f"Student 1: Name: {student1.name}, Age: {student1.age}")
print(f"Student 2: Name: {student2.name}, Age: {student2.age}")
print(f"Student 3: Name: {student3.name}, Age: {student3.age}")


#________________________________________________________________________________________________


#Q2
class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary


emp1 = Employee("E101", "siddhi marne", 65000)
print(f"ID: {emp1.employee_id} | Name: {emp1.employee_name} | Salary: {emp1.salary}")

#________________________________________________________________________________________________

#Q3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

car1.display_details()
car2.display_details()


#________________________________________________________________________________________________

#Q4
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.\n New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
        print("_________________________________________________")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}.\n Remaining Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")
        print("____________________________________________________________")

account = BankAccount("Siddhi marne", 500.0)
account.deposit(200)
account.withdraw(150)
account.withdraw(600)  



#________________________________________________________________________________________________
#Q5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

library = [
    Book("shyamchi aai", "sane guruji", 1960),
    Book("yayati", " v.s.khandekar", 1949),
    
]

print("Library Catalog:")
print("*-*-*-*-*-*-*-*-*-*-")
for book in library:
    print(book)

#________________________________________________________________________________________________
#Q6
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Mobile: {self.brand} {self.model} | Price: {self.price}")


phone1 = Mobile("Apple", "iPhone 15", 799)
phone2 = Mobile("Samsung", "Galaxy S24", 849)

phone1.display_details()
phone2.display_details()

#________________________________________________________________________________________________

#Q7
class Company:
   
    company_name = "TechCorp Solutions"

    def __init__(self, employee_name, role):
        self.employee_name = employee_name
        self.role = role


emp1 = Company("siddhi marne", "Developer")
emp2 = Company("ishwari shejul", "Designer")

print(f"{emp1.employee_name} works at {emp1.company_name}")
print(f"{emp2.employee_name} works at {emp2.company_name}")
print("_____________________________________________________")
print(f"Official Company Name: {Company.company_name}")


#________________________________________________________________________________________________

#Q8
class Product:
    
    tax_rate = 0.05

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    
    def calculate_final_price(self):
        final_price = self.base_price + (self.base_price * Product.tax_rate)
        return final_price


prod1 = Product("Laptop", 1000)
prod2 = Product("Headphones", 100)

print(f"{prod1.name} Final Price: ${prod1.calculate_final_price()}")
print(f"{prod2.name} Final Price: ${prod2.calculate_final_price()}")

#________________________________________________________________________________________________

#Q9
class Student:
  
    school_name = "Chavan School"

    def __init__(self, name):
        self.name = name

    
    @classmethod
    def update_school(cls, new_school_name):
        cls.school_name = new_school_name


s1 = Student("ishu")
s2 = Student("riya")
print(f"{s1.name} goes to {s1.school_name}")  

Student.update_school("zeal school")


print(f"{s1.name} now goes to {s1.school_name}")  
print(f"{s2.name} now goes to {s2.school_name}")  


#________________________________________________________________________________________________

#Q10
class Vehicle:
  
    vehicle_count = 0

    def __init__(self, brand):
        self.brand = brand
        
        Vehicle.vehicle_count += 1

print(f"Vehicles created so far: {Vehicle.vehicle_count}") 


v1 = Vehicle("suzuki")
v2 = Vehicle("Honda")
v3 = Vehicle("BMW")


print(f"Vehicles created so far: {Vehicle.vehicle_count}") 


#________________________________________________________________________________________________


#Q11
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

print("Addition (10 + 5):", Calculator.add(10, 5))
print("Subtraction (10 - 5):", Calculator.subtract(10, 5))
print("Multiplication (10 * 5):", Calculator.multiply(10, 5))
print("Division (10 / 0):", Calculator.divide(10, 0))

#________________________________________________________________________________________________

#Q12
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        # Formula: (C * 9/5) + 32
        return (celsius * 9/5) + 32

# Converting a temperature without creating a class instance
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")



#________________________________________________________________________________________________

#Q13
class Utility:
    @staticmethod
    def is_even(number):
        
        return number % 2 == 0

num1 = 42
num2 = 7

print(f"Is {num1} even? {Utility.is_even(num1)}")  
print(f"Is {num2} even? {Utility.is_even(num2)}")  


#________________________________________________________________________________________________

#Q14
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    pass 

student_obj = Student("siddhi", 21)
student_obj.display_person_info()


#________________________________________________________________________________________________


#Q15
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
       
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def display_bike_details(self):
        print(f"Brand: {self.brand} | Max Speed: {self.speed} km/h | Type: {self.bike_type}")

my_bike = Bike("Yamaha", 150, "Sports")
my_bike.display_bike_details()


#________________________________________________________________________________________________

#Q16
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def display_circle(self):
        print(f"Circle -> Color: {self.color}, Radius: {self.radius}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def display_rectangle(self):
        print(f"Rectangle -> Color: {self.color}, Dimensions: {self.length}x{self.width}")


circle1 = Circle("Red", 5)
rect1 = Rectangle("Blue", 10, 20)

circle1.display_circle()
rect1.display_rectangle()



#________________________________________________________________________________________________
#Q17
class Animal:
    def make_sound(self):
       
        print("Some generic animal sound")

class Dog(Animal):
    
    def make_sound(self):
        print("Dog says: Woof! Woof!")

class Cat(Animal):
    
    def make_sound(self):
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.make_sound()  
cat.make_sound()  

#________________________________________________________________________________________________
#Q18
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Error: Salary must be a positive amount.")


person = Person("siddhi", 50000)

print(f"{person.name}'s Current Salary: ${person.get_salary()}")

person.set_salary(55000)
print(f"{person.name}'s Updated Salary: ${person.get_salary()}")



#________________________________________________________________________________________________

#Q19
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  

    def check_balance(self):
        return f"Account Holder: {self.account_holder} | Balance: ${self.__balance}"

   
    def apply_interest(self, rate):
        if rate > 0:
            interest = self.__balance * rate
            self.__balance += interest
            print(f"Interest of ${interest:.2f} applied.")
        else:
            print("Invalid interest rate.")

account = BankAccount("siddhi marne", 1000.0)

print(account.check_balance())

account.apply_interest(0.05)
print(account.check_balance())


#________________________________________________________________________________________________

#Q20
class Employee:
    def __init__(self, name, rating):
        self.name = name
        self.__performance_rating = rating 

    def get_rating(self):
        return self.__performance_rating

    def update_rating(self, new_rating):
        if 1 <= new_rating <= 5:
            self.__performance_rating = new_rating
            print(f"Performance rating for {self.name} updated to {new_rating}.")
        else:
            print("Rejected: Rating must be an integer between 1 and 5.")

emp = Employee("siddhi", 3)


print(f"Initial Rating: {emp.get_rating()}")

emp.update_rating(6) 
emp.update_rating(5)  

print(f"Final Rating: {emp.get_rating()}")



#________________________________________________________________________________________________

#Q21
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: '{book.title}' to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"Success: You have borrowed '{book.title}'.")
                return
        print(f"Sorry: '{title}' is either unavailable or doesn't exist.")

lib = Library()
lib.add_book(Book("Python Basics", "John Doe"))
lib.borrow_book("Python Basics")
lib.borrow_book("Python Basics")  


#________________________________________________________________________________________________

#Q22
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Doctor(Person):
    def __init__(self, name, id_number, specialization):
        super().__init__(name, id_number)
        self.specialization = specialization

class Patient(Person):
    def __init__(self, name, id_number, diagnosis):
        super().__init__(name, id_number)
        self.__diagnosis = diagnosis  

    def get_diagnosis(self):
        return self.__diagnosis

doc = Doctor("Dr. ishwari shejul", "D991", "Cardiologist")
patient = Patient("riya margale", "P442", "Chronic Fatigue")

print("Doctor:",doc.name)
print("Specialty:",doc.specialization)
print("\nPatient:",patient.name) 
print("Condition:",patient.get_diagnosis())


#________________________________________________________________________________________________

#Q23

class Student:
    school_name = "Topper Academy"
    student_count = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.student_count += 1

    
    def get_details(self):
        return f"Student: {self.name} | Grade: {self.grade} | School: {self.school_name}"

  
    @classmethod
    def get_total_students(cls):
        return f"Total Enrolled Students: {cls.student_count}"


s1 = Student("riya", "A")
s2 = Student("ishwari", "B")

print(s1.get_details())
print(Student.get_total_students())



#________________________________________________________________________________________________
#Q24
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return f"{self.name} - {self.price} rupees"

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months

    
    
    def get_description(self):
        return f"{self.name} - {self.price} ({self.warranty_months} months warranty)"


generic_item = Product("Notebook", 5)
tech_item = ElectronicProduct("Smartphone", 699, 24)

print(generic_item.get_description())
print(tech_item.get_description())

#________________________________________________________________________________________________

#Q25
class ATM:
    def __init__(self, initial_balance, pin):
        self.__balance = initial_balance  # Encapsulated
        self.__pin = pin                  # Encapsulated

    def withdraw(self, entered_pin, amount):
        if entered_pin != self.__pin:
            print("Access Denied: Incorrect PIN.")
            return

        if amount > self.__balance:
            print("Transaction Failed: Insufficient funds.")
        elif amount <= 0:
            print("Transaction Failed: Invalid amount requested.")
        else:
            self.__balance -= amount
            print(f"Success: Withdrew ${amount}. Remaining balance: ${self.__balance}")


my_atm = ATM(1000, 1234)

my_atm.withdraw(9999, 100)   # Test incorrect PIN
my_atm.withdraw(1234, 1500)  # Test overdrawing
my_atm.withdraw(1234, 200)   # Test successful execution
#________________________________________________________________________________________________