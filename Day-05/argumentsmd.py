
import sys

# Function to perform addition
def addition(num1, num2):
    result = num1 + num2
    return result


# Function to perform subtraction
def subtraction(num1, num2):
    result = num1 - num2
    return result


# Function to perform multiplication
def multiplication(num1, num2):
    result = num1 * num2
    return result


# Get input values from the command line
# Example: python3 calculator.py 10 add 20

num1 = int(sys.argv[1])       # First number
operation = sys.argv[2]       # Mathematical operation
num2 = int(sys.argv[3])       # Second number


# Check which operation the user wants to perform
if operation == "add":

    # Call addition function
    output = addition(num1, num2)
    print("Addition Result:", output)

elif operation == "sub":

    # Call subtraction function
    output = subtraction(num1, num2)
    print("Subtraction Result:", output)

elif operation == "mul":

    # Call multiplication function
    output = multiplication(num1, num2)
    print("Multiplication Result:", output)

else:
    print("Invalid operation! Please use add, sub or mul.")
