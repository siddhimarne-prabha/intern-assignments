 
#02/06/2026
#Q1

student_info = {
    "Student name": "siddhi marne",
    "Age": 18,
    "Course": "AIML",
    "City": "India"
}
# Printing
print("Dictionary Values:")
for value in student_info.values():
    print(value)
#_______________________________________________________________________________________



#Q2

employee_info = {
    "Employee name": "Siddhi Marne",
    "Salary": 85000,
    "Department": "Engineering"
}

name = employee_info["Employee name"]
salary = employee_info["Salary"]
dept = employee_info["Department"]

# Print
print("Employee Name:", name)
print("Salary: $", salary)
print("Department:", dept)    

#________________________________________________________________________

#Q3


student_info = {
    "Student name": "Siddhi Marne",
    "Age": 18,
    "Course": "AIML",
    "City": "India"
}

student_info["email"] = "siddhi.marne@gmail.com"
print(student_info)
#_____________________________________________________________________________________-


#Q4

student_info = {
    "Student name": "siddhi marne",
    "Age": 17,
    "Course": "AIML"
}
# Update 
student_info["Age"] = 18
print("Updated Dictionary:", student_info)

#________________________________________________________________________________________

#Q5

#using pop()
employee_info = {"Name": "siddhi", "Salary": 85000, "Dept": "IT"}
removed_salary = employee_info.pop("Salary")
print("Dictionary after pop():", employee_info)
print("Removed Value:", removed_salary)

#using del()
employee_info = {"Name": "Jordan", "Salary": 85000, "Dept": "IT"}
del employee_info["Dept"]
print("Dictionary after del:", employee_info)

#________________________________________________________________________________________-


#Q6
device_info = {
    "Brand": "Apple",
    "Model": "iPhone 15",
    "Storage": "128GB"
}

# 1. Print all Keys
print("--- Keys ---")
for key in device_info.keys():
    print(key)

# 2. Print all Values
print("\n--- Values ---")
for value in device_info.values():
    print(value)

# 3. Print all Key-Value Pairs
print("\n--- Key-Value Pairs ---")
for key, value in device_info.items():
    print(f"{key}: {value}")

#____________________________________________________________________________________

#Q7

student_marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 88,
    "Computer Science": 95
}
num_subjects = len(student_marks)
print(f"Total number of subjects: {num_subjects}")

#_________________________________________________________________________________________-

#Q8

student_marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 84,
    "Geography": 89
}

# total marks 
total_marks = sum(student_marks.values())

# Print the results
print("Result")
for subject, mark in student_marks.items():
    print(f"{subject}: {mark}")
print("-------------------")
print(f"Total Marks: {total_marks}")

#____________________________________________________________________________________

#Q9
list = {
    "Laptop": 12,
    "Mouse": 50,
    "Keyboard": 25
}


search_key = "Mouse"


if search_key in list:
    print(f"Yes,this key exists in the dictionary.")
else:
    print(f"No,this key does not exist in the dictionary.")

#____________________________________________________________________________________

#Q10
products = {
    "Smart Watch": 250,
    "Smartphone": 699,
    "Tablet": 450,
    "Laptop": 1200,
    "Bluetooth Speaker": 150
}

print("Products with a price greater than 500:")
print("---------------------------------------")

for product, price in products.items():
    if price > 500:
        print(f"- {product}: {price}")

#___________________________________________________________________________________________

#Q11
numbers = {10, 20, 30, 40, 50}
for num in numbers:
    print(num)

#_______________________________________________________________________________________


#Q12

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#_____________________________________________________________________________________

#Q13
#using remove()
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("After remove():", numbers)

#using discard()
numbers = {1, 2, 4, 5}
numbers.discard(5)
numbers.discard(100)
print("After discard():", numbers)

#_____________________________________________________________________________________

#Q14
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

# All unique elements from both sets
union_set = set_A | set_B  

# Elements present in both sets
intersection_set = set_A & set_B  

# Elements in set_A but not in set_B
difference_set = set_A - set_B 

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)

#______________________________________________________________________________________-

#Q15
group1 = {"siddhi", "riya", "ishwari"}
group2 = {"ishwari", "ritu", "siddhi"}
common = group1 & group2
print("Common elements:", common)

#_________________________________________________________________________________________

#Q16
colors = {"red", "green", "blue"}
if "green" in colors:
    print("Yes, 'green' is in the set!")
else:
    print("No, 'green' is not in the set.")
#__________________________________________________________________________________________

#Q17

numbers = [1, 2, 2, 3, 4, 4, 4, 5]

unique_set = set(numbers)

print("Original List:", numbers)
print("Converted Set (Unique):", unique_set)

#________________________________________________________________________________________

#Q18
students = {"siddhi ", "ishwari", "siddhi", "riya", "ishwari"}
total_unique = len(students)
print("Unique Students:", students)
print("Total number of unique students:", total_unique)

#_____________________________________________________________________________________

#Q19

set1 = {10, 20, 30}
set2= {30, 10, 20}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")

#____________________________________________________________________________________-

#Q20

numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)
numbers.clear()
print("Set after clear():", numbers)

#_________________________________________________________________________________

#Q21
def message():
    print("Welcome to Python Programming")
message()
#_____________________________________________________________________________

#Q22
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum is:",result)
add_numbers(15, 25)

#___________________________________________________________________________________

#Q23

def greet_user(name):
    print(f"Hello, {name}")
greet_user("siddhi")

#_______________________________________________________________________________________


#Q24
def square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")

square(6)

#_______________________________________________________________________________________

#Q25

def check_even_odd(number):
    if number % 2 == 0:
        print("number is Even")
    else:
        print("number is Odd")

check_even_odd(7)
check_even_odd(12)

#_____________________________________________________________________________________________

#Q26

def calculate_rectangle_area(length, width):
    return length * width

print(calculate_rectangle_area(5, 10)) 

#____________________________________________________________________________________________

#Q27
def get_greater_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(get_greater_number(15, 42)) 

#___________________________________________________________________________________________

#Q28
def print_one_to_ten():
    for i in range(1, 11):
        print(i)

print_one_to_ten()

#________________________________________________________________________________________

#Q29
def calculate_list_sum(numbers_list):
    return sum(numbers_list)

print(calculate_list_sum([1, 2, 3, 4, 5])) 

#___________________________________________________________________________________

#Q30

def check_pass_or_fail(marks):
    if marks >= 35:
        return "Pass"
    else:
        return "Fail"
print(check_pass_or_fail(78))  
print(check_pass_or_fail(28))  

#_____________________________________________________________________________________

#Q31
def greet_user(name, city="Pune"):
    print("Hello", name ,"from", city,"!")

greet_user("Amit")          
greet_user("Neha", "Mumbai") 

#________________________________________________________________________________
#Q32

def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} named {pet_name}.")


describe_pet(animal_type="Cat", pet_name="GOGO")

#___________________________________________________________________________

#Q33
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(10, 20, 30, 40)

#_____________________________________________________________________________

#Q34
def get_max_and_min(numbers_list):
    if not numbers_list:
        return None, None  
    
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    return max_num, min_num

maximum, minimum = get_max_and_min([5, 12, 1, 84, 23])
print(f"Max: {maximum}, Min: {minimum}") 

#_________________________________________________________________________________-

#Q35

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels("Hello World")) 

#_________________________________________________________________________________