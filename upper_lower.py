def up_low(string):
    lower = upper = 0
    
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return string.upper() if upper > lower else string.lower()


while True:
    # Get user input
    string = input("Enter a string (letters only): ")

    # Check if the input is valid (only letters)
    if not string.isalpha():
        print("Invalid input. Please enter only letters.")
        continue

    # Call the function and print the result
    print(up_low(string))

    # Ask if the user wants to continue
    continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        break





# def upper_lower(word):
#     while True:
#         try:
#             upper_count = sum(1 for i in word if i.isupper())
#             lower_count = sum(1 for i in word if i.islower())

#             if upper_count > lower_count:
#                 return word.upper()
#             elif upper_count < lower_count:
#                 return word.lower()
#             else:
#                 raise ValueError

#         except ValueError:
#             print("Enter a word corecty!")

#         word = input("Enter a word: ")

# word = input("Enter a word: ")
# print(upper_lower(word))

