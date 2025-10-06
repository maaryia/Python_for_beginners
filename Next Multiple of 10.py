def multiple():
    while True:
        try:
            number = input("Enter the number: ")  # Get input as a string

            if not number.isdigit():  # Check if the input is a valid number
                raise ValueError("Enter only a number!")

            number = int(number)  # Convert to integer
            next_num = ((number // 10) + 1) * 10  # Calculate the next multiple of 10

            return next_num  # Return the calculated next multiple

        except ValueError as e:
            print(e)  # Print the error message and continue the loop

# Call the function and print the result
next_num = multiple()
print("The next multiple number is:", next_num)
