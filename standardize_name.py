def stand_name():
    while True:
        try:
            name = input("Enter a name: ")
            if not name.isalpha():
                raise ValueError
            name = name.lower()
            return name.capitalize()
        except ValueError:
            print("Invalid input. Please enter a valid name.")

names = []
for i in range(10):
    standardized_name = stand_name()
    names.append(standardized_name)

for name in names:
    print(name)


# def standardize_names():
#     nam = []  # Initialize the list to store names
#     for i in range(2):  # Loop to read 2 names
#         names = input("Enter names: ")  # Read user input
#         # Split the name into words, standardize each word, and join them back
#         standardized_name = ' '.join(word.lower().capitalize() for word in names.split())
        
#         nam.append(standardized_name)  # Append the standardized name to the list

#     # Print all standardized names
#     for name in nam:
#         print(name)

# standardize_names()