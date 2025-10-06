
from termcolor import colored

def get_laptop_info():
    """Get the price and quality of a laptop from user input."""
    while True:
        try:
            price = int(input("Enter price: "))  # Read price
            quality = int(input("Enter quality: "))  # Read quality
            return price, quality  # Return as a tuple
        except ValueError:
            print("Invalid input. Please enter numbers only.")  # Handle invalid input

def check_laptops(laptops):
    """Check for two laptops that meet Irsa's conditions."""
    for i in range(len(laptops)):
        for j in range(len(laptops)):
            # Ensure we are comparing different laptops --> i != j
            if i != j and laptops[i][0] < laptops[j][0] and laptops[i][1] > laptops[j][1]:
                return True  # Found a valid pair
    return False  # No valid pair found

def main():
    """Main function to run the program."""
    while True:
        try:
            n = int(input("Enter the number of laptops: "))  # Number of laptops
            if n > 0:
                break  # Valid input
            else:
                raise ValueError("Must be greater than zero.")
        except ValueError as e:
            print("Invalid input:", e)  # Handle invalid input

    laptops = []  # List to store laptop details
    for i in range(n):
        print(colored(f"Entering details for laptop {i + 1}", "red"))  # Print in red
        laptops.append(get_laptop_info())  # Get and store laptop details

    # Check if Irsa's claim can be proven
    if check_laptops(laptops):
        print("happy irsa")  # Conditions met
    else:
        print("poor irsa")  # Conditions not met

if __name__ == "__main__":
    main()  # Start the program




#SECOND WAY
# n = int(input("Enter laptops numbers: ")) 

# laptops = [] 

# # Read laptops information
# for _ in range(n):
#     price, quality = map(int, input("Enter quality & price:").split())
#     laptops.append((price, quality))

# # check the Conditions
# for i in range(n):
#     for j in range(n):
#         if laptops[i][0] > laptops[j][0] and laptops[i][1] < laptops[j][1]:
#             print("happy irsa")
#             exit()

# print("poor irsa")




#THIRD WAY
# def get_laptop_info():
#     """Get the price and quality of a laptop."""
#     while True:
#         try:
#             price = int(input("Enter price: "))  # Input price
#             quality = int(input("Enter quality: "))  # Input quality
#             return price, quality  # Return as a tuple
#         except ValueError:
#             print("Invalid input. Please enter numbers only.")

# def main():
#     """Main function to run the program."""
#     n = int(input("Enter the number of laptops: "))  # Number of laptops
#     laptops = []  # List to store laptop details

#     for i in range(n):
#         print(f"\033[91mEntering details for laptop {i + 1}:\033[0m")  # Print in red
#         laptops.append(get_laptop_info())  # Get laptop details

#     # Check for any two laptops that meet Irsa's conditions
#     for i in range(n):
#         for j in range(n):
#             if i != j and laptops[i][0] < laptops[j][0] and laptops[i][1] > laptops[j][1]:
#                 print("happy irsa")  # Found a valid pair
#                 return

#     print("poor irsa")  # No valid pair found

# if __name__ == "__main__":
#     main()  # Run the program