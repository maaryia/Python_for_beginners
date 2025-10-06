while True:
    try:
        user_input = input("Enter a sentence (letters only): ")

        # Check for invalid characters (numbers or symbols)
        if not user_input.replace(" ", "").isalpha():
            raise ValueError("Only letters and spaces are allowed!")

        counter = {}
        for char in user_input:
            if char != " ":  # Skip counting spaces
                counter[char] = counter.get(char, 0) + 1

        for char, count in counter.items():
            print(f"'{char}' appeared {count} times")

        break  # Exit if everything is valid

    except ValueError as e:
        print(e)
        print("Please try again.\n")



