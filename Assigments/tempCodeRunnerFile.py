filename = "student.txt"
students_to_add = ["siddhi", "riya", "ishwari", "aarvi", "pradnya"]

# 1. Writing 5 names to the file
with open(filename, "w") as file:
    for name in students_to_add:
        file.write(name + "\n")
print("5 names have been stored.\n")

# 2. Reading and displaying the names from the file
print("Displaying students from file:")
with open(filename, "r") as file:
    for line in file:
        print("-", line.strip())