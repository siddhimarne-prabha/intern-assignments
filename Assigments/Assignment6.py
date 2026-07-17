# 09/06/2026 -oop
#SECTION 1: HYBRID INHERITANCE

#________________________________________________________________________________________________
#Q1

class Person:
    def __init__(self, n, a):
        self.n = n  # name
        self.a = a  # age

class Teacher(Person):
    def __init__(self, n, a, sub):
        Person.__init__(self, n, a)
        self.sub = sub  

class Student(Person):
    def __init__(self, n, a, id):
        Person.__init__(self, n, a)
        self.id = id 

class TA(Teacher, Student):
    def __init__(self, n, a, sub, id, lab):
        Teacher.__init__(self, n, a, sub)
        Student.__init__(self, n, a, id)
        self.lab = lab  

    def show(self):
        print("TeachingAssistant:", self.n),
        print("Age:", self.a)
        print("ID:", self.id)
        print("Subject:",self.sub) 
        print("Lab:",self.lab)

# Test code
obj = TA("siddhi", 23, "CS", "101", "Lab-A")
obj.show()



#_______________________________________________________________________________________


#Q2
class Vehicle:
    def __init__(self, b):
        self.b = b  # brand

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, b, mod):
        super().__init__(b)
        self.mod = mod  # model

class ElecCar(Car):
    def __init__(self, b, mod, bat):
        super().__init__(b, mod)
        self.bat = bat  # battery

class SportsElec(ElecCar):
    def __init__(self, b, mod, bat, spd):
        super().__init__(b, mod, bat)
        self.spd = spd  # speed

    def show(self):
        print("Car:",self.b,self.mod)
        print("Battery:",self.bat,"kWh")
        print("Speed:",self.spd,"mph")


obj = SportsElec("Tesla", "S", 100, 200)
obj.show()



#_______________________________________________________________________________________

#Q3
class Emp:
    def __init__(self, n):
        self.n = n

class Dev(Emp):
    def code(self):
        return f"{self.n} is coding"

class Mgr(Emp):
    def manage(self):
        return f"{self.n} is managing"

class Lead(Dev, Mgr):
    def __init__(self, n, tech):
        super().__init__(n)
        self.tech = tech  # technology focus

    def show(self):
        print(f"Lead: {self.n}, Focus: {self.tech}")
        print(self.code())
        print(self.manage())


obj = Lead("Siddhi", "Python")
obj.show()

#_______________________________________________________________________________________

#Q4
class Person:
    def __init__(self, n):
        self.n = n

class Doctor(Person):
    def __init__(self, n, lic):
        super().__init__(n)
        self.lic = lic 

class Nurse(Person):
    def __init__(self, n, shf):
        super().__init__(n)
        self.shf = shf  # shift (Day/Night)

class HeadNurse(Nurse):
    def __init__(self, n, shf, dept):
        super().__init__(n, shf)
        self.dept = dept 

    def show(self):
        print("Head Nurse:",self.n)
        print("Shift:",self.shf)
        print("Dept:",self.dept)


obj = HeadNurse("siddhi", "Night", "ICU")
obj.show()


#_______________________________________________________________________________________
#SECTION 2: HIERARCHICAL INHERITANCE

#Q5
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"


dog = Dog("sketch")
cat = Cat("mani")
cow = Cow("rupa")

print(f"{dog.name} says {dog.sound()}")
print(f"{cat.name} says {cat.sound()}")
print(f"{cow.name} says {cow.sound()}")


#_______________________________________________________________________________________
#Q6
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, balance, months):
        super().__init__(account_number, balance)
        self.months = months


savings = SavingsAccount("SAV123", 5000, 4.0)
current = CurrentAccount("CUR456", 2000, 1000)
fixed = FixedDepositAccount("FIX789", 10000, 12)

print(f"Savings Account {savings.account_number} Interest Rate: {savings.interest_rate}%")
print(f"Current Account {current.account_number} Overdraft Limit: ${current.overdraft_limit}")
print(f"Fixed Deposit {fixed.account_number} Duration: {fixed.months} months")

#_______________________________________________________________________________________

#Q7
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "Doing general company work"

class Developer(Employee):
    def work(self):
        return "Writing computer programs and fixing bugs"

class Tester(Employee):
    def work(self):
        return "Testing applications to ensure quality"

class Designer(Employee):
    def work(self):
        return "Creating user interfaces and visual layouts"


dev = Developer("siddhi")
tester = Tester("ishwari")
designer = Designer("riya")

print(f"{dev.name}: {dev.work()}")
print(f"{tester.name}: {tester.work()}")
print(f"{designer.name}: {designer.work()}")

#_______________________________________________________________________________________


#Q8
class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def calculate_area(self):
        return self.side * self.side


circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(4)

print(f"{circle.shape_name} Area: {circle.calculate_area()}")
print(f"{rectangle.shape_name} Area: {rectangle.calculate_area()}")
print(f"{square.shape_name} Area: {square.calculate_area()}")


#_______________________________________________________________________________________
#SECTION 3: POLYMORPHISM

#Q9
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Storing different shapes in a list
shapes_list = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes_list:
    print(f"Area of {shape.name}: {shape.area()}")

#_______________________________________________________________________________________


#Q10

class Payment:
    def pay(self, amount):
        print(f"Processing generic payment of ${amount}")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} securely using Credit Card.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} instantly via UPI QR Code.")

class NetBankingPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} through Net Banking portal.")


payments = [CreditCardPayment(), UPIPayment(), NetBankingPayment()]

for option in payments:
    option.pay(150)



#_______________________________________________________________________________________

#Q11
class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email Sent: '{message}'")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS Alert Sent: '{message}'")

class PushNotification(Notification):
    def send(self, message):
        print(f"App Push Notification Sent: '{message}'")


alerts = [EmailNotification(), SMSNotification(), PushNotification()]

for alert in alerts:
    alert.send("Your order has shipped!")

#_______________________________________________________________________________________
#Q12
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

zoo = [Dog("dubi"), Cat("gogo"), Lion("Simba")]

for animal in zoo:
    print(f"{animal.name} the says: {animal.make_sound()}")

#_______________________________________________________________________________________

#Q13
class Employee:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "General Employee"

class Developer(Employee):
    def role(self):
        return "Software Developer (Writes code)"

class Tester(Employee):
    def role(self):
        return "QA Engineer (Tests applications)"

class Manager(Employee):
    def role(self):
        return "Project Manager (Leads team)"


team = [Developer("siddhi"), Tester("ishwari"), Manager("riya")]

for member in team:
    print(f"{member.name} works as a {member.role()}")

#_______________________________________________________________________________________

#Q14
class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        return "Vehicle is starting"

class Car(Vehicle):
    def start(self):
        return "Engine purrs smoothly."

class Bike(Vehicle):
    def start(self):
        return "Kickstart engaged. Engine revs up!"

class Bus(Vehicle):
    def start(self):
        return "Heavy diesel engine rumbles to life."


garage = [Car("Sedan"), Bike("Cruiser"), Bus("Shuttle")]

for vehicle in garage:
    print(f"{vehicle.name}: {vehicle.start()}")

#_______________________________________________________________________________________


#SECTION 4: POLYMORPHISM + INHERITANCE
#Q15

class Device:
    def __init__(self, brand):
        self.brand = brand

    def use(self):
        return "Using a generic electronic device."

class Camera(Device):
    def use(self):
        return f"Taking a high-resolution photo with the {self.brand} lens."

class Phone(Device):
    def use(self):
        return f"Making a voice call using the {self.brand} network connection."

class SmartPhone(Phone,Camera): 
    def use(self):
        return f"Browsing apps, {self.brand} camera features, and calling contacts."

device_list = [
    Camera("Canon"),
    Phone("Nokia"),
    SmartPhone("iPhone")
]

print("--- Runtime Polymorphism Demonstration ---")

for device in device_list:
    print("_________________________________________________________")
    print(f"{device.brand} Device: {device.use()}")
          
#_______________________________________________________________________________________