# Shopping List 
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
shop_list = ["bread"]      # Define an empty list for user to add to, starting with bread to test
def add_shop(): 
     add = input("What would you like to add to the shopping list? ") 
     shop_list.append(add) 
     print(f"We've added {add} to our list") 
    

# Task 2: Include a function to remove items from the list.
def take_away(): 
    take = input("What would you like to remove from the shopping list? ") 
    shop_list.remove(take) 
    print(f"We've removed {take} from our list") 

# Task 3: Add a function that prints out the entire list in a formatted way.
def show():  
    print("So far out shopping list has: ") 
    for items in shop_list:
        print("- " + items)  
    
# Testing 
print("Would you like to: ") 
print("1 - See Current Shopping List") 
print("2 - Add something to Shopping List") 
print("3 - Remove something from Shopping List")
print("4 - Exit Shopping List")

while True: 
    choice = input("Enter 1/2/3/4: ") 

    if choice in ('1', '2', '3', '4'): 
        if choice == '1':
            show()     
        elif choice == '2': 
            add_shop()
        elif choice == '3': 
            take_away() 
        elif choice == '4': 
            print("That's everything! Time to go shoppping.") 
            break 
        
