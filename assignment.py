# Python File Handling & Exception Handling

# File Handling:
# Question 1 – Create and Write to a File 
# Create a file named student.txt and write
with open("student.txt","w") as file:
  file.write("Ali Hassan\n")
  file.write("18\n")
  file.write("Lahore")

print("File written successfully")

# Question 2 – Read the File
# Using read() method
print("Read the File Using read() method")
with open("student.txt","r") as file:
 print(file.read())


# Using readline() method
print("Read the File Using readline() method")
with open("student.txt","r") as file:
  print(file.readline(), file.readline(), file.readline())


# Using readlines() method
print("Read the File Using readlines() method")
with open("student.txt","r") as file:
 print(file.readlines())

# Question 3 – Append Data
# Append new data to the file
print("Append new data to the file")

with open("student.txt","a") as file:
 file.write("\nCourse: Python Programming")
with open("student.txt", "r") as file:
 print(file.read())



# Exception Handling:
# Question 4 – Handle Division Error
# Program to handle division by zero
print("Program to handle division by zero")
print("Enter two numbers for division")
try:
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   result = num1 / num2
   print("Result:", result)
except ZeroDivisionError:
   print("Cannot divide by zero.")
except ValueError:
   print("Please enter valid numbers")


# QUESTION 5 - Handle Invalid Input
# Program to handle invalid age input
print("Program to handle invalid age input")
try:
    age = int(input("Enter your age: "))
    
    if 0 <= age <= 100:
        print("Your age is:", age, "years")
    else:
        print("Please enter a valid age between 0 and 100.")
        
except ValueError:
    print("Please enter a valid number.")

# QUESTION 6 - Use else and finally
# Program using try except else finally method
print("Program using try except else finally method")
print("Enter a numbers for findind Square")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number!")
else:
    square = num * num
    print("Square of", num, ":", square)
finally:
    print("Program Finished")

# QUESTION 7 - Mini Project
# Student Result Program Using Exception Handling
print("Student Result Program Using Exception Handling")
def grades(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
    
try:
    name = input("Enter Student Name: ")
    try:
        marks = int(input("Enter Obtained Marks: "))

        # Validate marks range
        
        if marks < 0 or marks > 100:
            print("Invalid Marks")
        else:
            # Calculate and display results
            grade = grades(marks)
            print("Student Result")
            print("Student Name:", name)
            print("Obtained Marks:", marks)
            print("Grade:", grade)
    except ValueError:
        print("Please enter marks value in number.")
except Exception as e:
    print("An error occurred:", e)
