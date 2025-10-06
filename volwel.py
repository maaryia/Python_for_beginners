def volwels():
    vowels = "aeiouAEIOU"

    while True:
        input_str = input("Enter a string: ")
        if not input_str.isalpha():
            print("Invalid input. Please enter only letters.")
            continue
        else:
            break

    output_str = ""

    for char in input_str:
        if char in vowels:
            continue
        else:
            output_str += "."
            if char.islower():
                output_str += char
            else:
                output_str += char.lower()

    print(output_str)

volwels()
#2 def modify_string(input_string):
#     vowels = "aeiouAEIOU"
#     modified_string = ""
    
#     for char in input_string:
#         if char.isalpha():
#             if char.lower() not in vowels:
#                 modified_string += "." + char.lower()
#         else:
#             modified_string += char

#     return modified_string


# input_string = input("Enter a string: ")
# result = modify_string(input_string)
# print("Modified string:", result)



#3 volwel = ["a", "o", "i","u", "e"]

# input = input("Input: ").strip()
# output = ""

# for i in input:
#     if i.lower() not in volwel:
#         output += i

# print(f"Output: {output}")