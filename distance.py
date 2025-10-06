def calculate_distance(locations):
    distance = abs(locations[1] - locations[0]) + abs(locations[2] - locations[1])
    return distance

def main():
    while True:
        try:
            locations = []
            for i in range(3):
                location = int(input(f"Enter location (numbers){i+1}: "))
                locations.append(location)
            minimum_distance = calculate_distance(locations)
            print("The minimum distance is:", minimum_distance)
            break
        except ValueError:
            print("Please enter numbers.")

if __name__ == "__main__":
    main()
