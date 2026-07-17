# 17/06/2026 – Exception Handling

#Topic: Exception Handling

#Question 1: Handle Division by Zero


try:
  
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    
    result = first_number / second_number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Cannot divide by zero.")

#_______________________________________________________________________________________


#Question 2: Handle Invalid Number Input

try:
   
    user_input = int(input("Enter a number: "))
    print(f"You entered a valid number: {user_input}")

except ValueError:
  
    print("Invalid input. Please enter a number.")

#_______________________________________________________________________________________



#Question 3: Using try and except

numbers_list = [10, 20, 30, 40, 50]

try:
    
    index = int(input("Enter index: "))
    print(f"Element at index {index}: {numbers_list[index]}")

except IndexError:
    print("Index out of range.")
except ValueError:
    print("Invalid input. Please enter a numerical index.")


#_______________________________________________________________________________________



#Question 4: Using else Block

try:
    
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    
    result = first_number / second_number

except ZeroDivisionError:
   
    print("Cannot divide by zero.")

except ValueError:
    
    print("Invalid input. Please enter numbers only.")

else:
    print(f"Result: {result}")



#_______________________________________________________________________________________




#Question 5: Using finally Block

try:
  
  
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
   
    print("Error: The file was not found.")

finally:

    print("File operation completed.")


#_______________________________________________________________________________________




#Question 6: Multiple Exceptions

numbers = [10, 20, 30, 40, 50]

try:
  
    user_number = int(input("Enter a number to divide by: "))
    index = int(input("Enter an index to access from the list: "))
    
   
    element = numbers[index]
    
    result = element / user_number
    print(f"Result of division: {result}")

except ValueError:
    
    print("Invalid input.")

except IndexError:
   
    print("Index out of range.")

except ZeroDivisionError:
 
    print("Cannot divide by zero.")



#_______________________________________________________________________________________




#Question 7: Custom Exception

class NegativeNumberError(Exception):
    pass

try:
   
    user_number = float(input("Enter a number: "))
   
    if user_number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
        
    print(f"You entered a valid positive number: {user_number}")

except NegativeNumberError as error:
   
    print(error)

except ValueError:
    print("Invalid input. Please enter a valid number.")

 #_______________________________________________________________________________________