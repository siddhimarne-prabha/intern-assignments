
#  01/06/2026
# Q1
print("my name is siddhi")
print("my favourite programming language is python")


#Q2
name=input("enter your name")
age=int(input("enter your age"))
print("hello",name,"you are",age,"years old")


#Q3
student_name="siddhi"
roll_no=42
percentage=87.60
passed_status=True
print("student details:")
print("name:",student_name)
print("Roll_no:",roll_no)
print("percentage:",percentage)
print("passed:",passed_status)

#Q4
"""
    - 1name     -   INVALID - name1
    -student-name   -  INVALID  -   student_name
    -class  -    INVALID    -   class_name
    -total marks    -   INVALID     -   total_marks
    -user_name  -   VALID
"""
#Q5


a = 25
b = 19.99
c = "Hello World"
d = True
  
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#Q6


number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")


sum_result = float(number1) + float(number2)


print("The sum is:", sum_result)

#Q7


num = float(input("Enter a decimal: "))


a = int(num)
b = str(num)


print("Int:", a)
print("Str:", b)

#Q8

x = input("Enter age: ")

if x.isdigit():
    print("Type: integer")
else:
    print("Type: string")



#Q9


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)


#Q10

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Greater than:", x > y)
print("Less than:", x < y)
print("Equal to:", x == y)
print("Not equal to:", x != y)



#Q11

u = input("Username: ")
p = input("Password: ")

if u == "admin" and p == "1234":
    print("Login success")
else:
    print("Login failure")


#Q12

x = float(input("Enter a number: "))

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


#Q13

x = float(input("Enter marks: "))

if x >= 90:
    print("Grade: A")
elif x >= 75:
    print("Grade: B")
elif x >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

#Q14

x = int(input("Enter a number: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q15

x = int(input("Enter age: "))

if x < 13:
    print("Child")
elif x < 20:
    print("Teenager")
elif x < 60:
    print("Adult")
else:
    print("Senior Citizen")


#Q16

x = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
y = float(input("Enter second number: "))

if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")


#Q17

for i in range(1, 21):
    print(i)


#Q18

for i in range(2, 51, 2):
    print(i)

#Q19

x = int(input("Enter a number: "))

for i in range(1, 11):
    print(x, "x", i, "=", x * i)

#Q20

i = 10
while i >= 1:
    print(i)
    i -= 1

#Q21

s = 0
for i in range(1, 101):
    s += i
print(s)



#Q22

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1

num = abs(num)

while num > 0:
    count += 1
    num = num // 10

print(count)




#Q23

for i in range(1, 21):
    if i == 15:
        break
    print(i)




#Q24

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)



#Q25

while True:
    password = input("Enter password: ")
    if password == "python123":
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")



#Q26

for i in range(1, 6):
    print("*" * i)




#Q27

for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


#Q28

for i in range(1, 5):
    for j in range(4):
        print(i, end="")
    print()



#Q29

students = ["Siddhi", "Riya", "Ishwari", "Pradnya", "Anushka"]

print("First student:", students[0])
print("Last student:", students[-1])
print("Total number of students:", len(students))


#Q30
numbers = []
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

print("List of numbers:", numbers)


#Q31


my_list = [40, 10, 30, 20]

my_list.append(50)
print("After append(50):", my_list)

my_list.remove(30)
print("After remove(30):", my_list)

popped_val = my_list.pop()
print("After pop():", my_list)

my_list.sort()
print("After sort():", my_list)



#Q32

items = ["apple", "banana", "cherry", "date"]

for item in items:
    print(item)



#Q33

nums = [15, 42, 7, 89, 23]

print("Maximum value:", max(nums))
print("Minimum value:", min(nums))
print("Sum of all elements:", sum(nums))


#Q34


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 elements:", numbers[:5])
print("Last 3 elements:", numbers[-3:])
print("Alternate elements:", numbers[::2])


#Q35

user_info = ("siddhi", 19, "India")

print("Name:", user_info[0])
print("Age:", user_info[1])
print("City:", user_info[2])


#Q36

my_tuple = (1, 2, 3)

try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error observed:", e)


#Q37

numbers = (12, 45, 7, 89, 23)

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Total sum:", sum(numbers))


#Q38


student_tuple = ("Siddhi", 101, "A+")


name, roll_no, grade = student_tuple

print("Unpacked Details:")
print("Name:", name)
print("Roll No:", roll_no)
print("Grade:", grade)



#Q39

balance = 1000.0

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: ${balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount > 0:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")



#Q40

marks = []
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_subjects):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)


total_marks = sum(marks)
average_marks = total_marks / num_subjects
highest_mark = max(marks)


if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
else:
    grade = "F"


print("\n--- Student Result Summary ---")
print("All Marks:", marks)
print(f"Highest Marks: {highest_mark}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Final Grade: {grade}")