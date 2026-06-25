
# 04/06/2026

#Q1
print("Q1_______________________________________________________________________")
class Student:
    school_name = "Zeal College"  

    def __init__(self, name, age, course):
        self.name = name  
        self.age = age
        self.course = course

    def display_student(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("course:",self.course)
        print("Name:",Student.school_name)

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


s1 = Student("siddhi", 16, "CS")
s2 = Student("ishwari", 17, "Math")
s1.display_student()

Student.change_school_name("MIT College")

s1.display_student()
s2.display_student()

#______________________________________________________________________________________________

#Q2
print("Q2_______________________________________________________________________")
class Employee:
   
    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        
        Employee.employee_count += 1

    
    def display_employee(self):
        print("ID:",self.emp_id)
        print("Name:",self.emp_name)
        print("Salary:",self.salary)

    @classmethod
    def show_total_employees(cls):
        print("Total Employees:",cls.employee_count)

emp1 = Employee(101, "siddhi marne", 75000)
emp2 = Employee(102, "ishwari shejul", 82000)
emp3 = Employee(103, "riya margale", 64000)

print("--- Employee Details ---")
emp1.display_employee()
print("___________________________________")
emp2.display_employee()
print("___________________________________")
emp3.display_employee()
print("___________________________________")

Employee.show_total_employees()


#_____________________________________________________________________________________________

#Q3
print("Q3_______________________________________________________________________")
class BankAccount:
  
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
       
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited!",amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawn successfully from Account ")
        else:
            print("Insufficient balance in Account!")

    def check_balance(self):
        print("Balance:",self.balance)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


acc1 = BankAccount(1001, "Siddhi", 500)
acc2 = BankAccount(1002, "riya", 300)

print("--- Account Details ---")
acc1.check_balance()
acc2.check_balance()
print("_________________________")

acc1.deposit(200)       
acc2.withdraw(100)     
acc2.withdraw(500)      
print("\n--- Balance After Transactions ---")
acc1.check_balance()
acc2.check_balance()
print("____________________")
BankAccount.change_bank_name("SBI Global Bank")
print("\n--- After Changing Bank Name ---")
acc1.check_balance()
acc2.check_balance()



#_______________________________________________________________________________________

#Q4
print("Q4_______________________________________________________________________")
class Mobile:
    
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


    def display_mobile(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)

    def calculate_discount_price(self):
        discount = (self.price * Mobile.discount_percentage) / 100
        return self.price - discount
    
    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount

p1 = Mobile("Apple", "iPhone 15", 800)
p2 = Mobile("Samsung", "S24", 700)
p3 = Mobile("OnePlus", "Nord", 300)

print("--- 10% Discount Prices ---")
p1.display_mobile()
print(f"Discounted Price: {p1.calculate_discount_price()}\n")

p2.display_mobile()
print(f"Discounted Price: {p2.calculate_discount_price()}\n")

p3.display_mobile()
print(f"Discounted Price: {p3.calculate_discount_price()}\n")

Mobile.change_discount(20)

print("--- New 20% Discount Prices ---")
print(f"{p1.model} New Price: ${p1.calculate_discount_price()}")
print(f"{p2.model} New Price: ${p2.calculate_discount_price()}")
print(f"{p3.model} New Price: ${p3.calculate_discount_price()}")
#______________________________________________________________________________________

#Q5
print("Q5_______________________________________________________________________")
class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
       print("Book_ID:",self.book_id)
       print("Title:",self.title)
       print("Author:",self.author)
       print("Library:",Book.library_name )
       print("________________")
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

book1 = Book(101, "shyamchi aai", "sane guruji")
book2 = Book(102, "yayati", " v.s.khandekar")



print("--- Before Changing Library Name ---")
book1.display_book_info()

book2.display_book_info()

print("\n...Changing library name using class method...\n")

Book.change_library_name("Central Technical Library")

print("--- After Changing Library Name ---")
book1.display_book_info()
book2.display_book_info()
