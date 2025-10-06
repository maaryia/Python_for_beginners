def calculate_distance(locations):
    distance = abs(locations[1] - locations[0]) + abs(locations[2] - locations[1])
    return distance

def main():
    while True:
        try:
            locations = []
            for i in range(3):
                location = int(input(f"Enter location {i+1}: "))
                locations.append(location)
            minimum_distance = calculate_distance(locations)
            print("The minimum distance is:", minimum_distance)
            break
        except ValueError:
            print("Please enter numbers.")

if __name__ == "__main__":
    main()


# # Function to calculate the minimum distance
# def calculate_min_distance(positions):
#     # Sort the positions
#     sorted_positions = sorted(positions)
#     # Calculate the minimum distance
#     min_distance = sorted_positions[2] - sorted_positions[0]  # Largest - Smallest
#     return int(min_distance)  # Return as an integer

# # Main part of the program
# if __name__ == "__main__":
#     # Step 1: Read input from the user
#     input_values = input("Enter the positions of the friends (x1, x2, x3): ")

#     # Step 2: Use map to convert the input string to a list of integers
#     positions = list(map(int, input_values.split()))

#     # Step 3: Calculate the minimum distance
#     result = calculate_min_distance(positions)

#     # Step 4: Print the result
#     print(result)   