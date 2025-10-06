# def substring(input_string):
#     if 'AB' in input_string and 'BA' in input_string:
#         index_AB = input_string.index('AB')
#         index_BA = input_string.index('BA')
#         if abs(index_AB - index_BA) > 1:
#             return 'YES'
#     return 'NO'

# while True:
#     # Get input from the user
#     input_string = input("Enter a string: ")

#     # Check if the input contains only alphabetic characters
#     if input_string.isalpha():
#         break
#     else:
#         print("Invalid input! The string should only contain alphabetic characters.")

# # Check the string and display the output
# print(substring(input_string))


def can_find_ab_ba():
    user_input = input("Enter a string: ")

    # Check for "AB" and then "BA" after it
    if "AB" in user_input:
        if "BA" in user_input[user_input.index("AB") + 2:]:
            print("YES")
            return

    # Check for "BA" and then "AB" after it
    if "BA" in user_input:
        if "AB" in user_input[user_input.index("BA") + 2:]:
            print("YES")
            return

    print("NO")

can_find_ab_ba()