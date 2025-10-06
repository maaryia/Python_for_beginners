import math
from termcolor import colored

def square_root():
    try:
        num = int(input("Enter the number of values: "))  # Number of values to process
        
        for i in range(num):
            user_num = float(input(f"Enter number {i + 1}: "))  # Read a positive number
            sqrt_value = math.sqrt(user_num)  # Calculate the square root
            print(colored(f"{sqrt_value:.4f}", "magenta"))  # Print the result formatted to 4 decimal places
    except ValueError:
        print("Invalid input")  # Handle invalid inputs

square_root()  # Call the function to execute
