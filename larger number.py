def print_larger_number():

    number1 = int(input("Please enter a first number: "))
    number2 = int(input("Please enter a second number: "))

    if number1 > number2:
        print(number1)
    elif number2 > number1:
        print(number2)
    else:
        print(number1 or number2)

print_larger_number()
