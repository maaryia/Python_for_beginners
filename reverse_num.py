def reverse_double():
    while True:  # Start an infinite loop
        try:
            number = input("Please enter a three-digit number: ")

            # Check if the input is a three-digit number
            if len(number) != 3 or not number.isdigit():
                raise ValueError("Enter a three-digit number only")
            
            # Reverse the number and double it
            reverse_number = int(number[::-1])
            doubled_value = reverse_number * 2
            
            return doubled_value  # Return the valid result
        except ValueError as e:
            print(e)  # Print the error message and continue the loop

# Call the function
number = reverse_double()
print("The doubled reversed number is:", number)

