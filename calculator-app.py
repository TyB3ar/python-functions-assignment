# Task 1: Create Functions for each Arithmetic Operation

def addition(a, b):     # Function for adding 2 parameters, will be input later
    sum = a + b
    return sum

def subtraction(a, b):   # Function for subtracting
    difference = a - b
    return difference

def multiplication(a, b):   # Function for multiplying
    product = a * b
    return product

def division(a, b):   # Function for dividing
    divide = a / b
    return divide 
    
print("Welcome to my calculator! Would you like to: ") 
print("1 - Add") 
print("2 - Subttract") 
print("3 - Multiply") 
print("4 - Divide")
    
# try to loop input 
while True: 
    choice = input("Enter 1/2/3/4: ")  # Ask user to pick an operation       
        
    if choice in ('1', '2', '3', '4'):    
        num_one = int(input("Enter your first number: "))
        num_two = int(input("Enter your second number: ")) 
         
        if choice == '1': 
            print(f"The sum of {num_one} and {num_two} is {addition(num_one, num_two)}")  # calls addition function if user inputs 1
        elif choice == '2': 
            print(f"The difference of {num_one} and {num_two} is {subtraction(num_one, num_two)}")  # calls subtraction function if user inputs 2
        elif choice == '3': 
            print(f"The product of {num_one} and {num_two} is equal to {multiplication(num_one, num_two)}")  # calls multiplication function if user inputs 3
        elif choice == '4': 
            if num_two == 0:
                print("Division by zero error! Please enter a different number to divide by.")   # prints error message instead of program hitting error, asks for other input
            else:
                print(f"The quotient of {num_one} and {num_two} is equal to {division(num_one, num_two)}")   # calls division funciton if user inputs 'division' and not divide by 0 error
        break
    else: 
        print("Invalid operation!")
        break
    