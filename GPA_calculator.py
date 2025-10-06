import csv
from statistics import mean 
from collections import OrderedDict

# Sample data to create the input CSV
data = [
    ["mandana", 5, 7, 3, 15],
    ["hamid", 3, 9, 4, 20, 9, 1, 8, 16, 0, 5, 2, 4, 7, 2, 1],
    ["sina", 19, 10, 19, 6, 8, 14, 3],
    ["sara", 0, 5, 20, 14],
    ["soheila", 13, 2, 5, 1, 3, 10, 12, 4, 13, 17, 7, 7],
    ["ali", 1, 9],
    ["sarvin", 0, 16, 16, 13, 19, 2, 17, 8]
]

# Create input CSV file
with open('input.csv', mode='w', newline='') as file:
    writer = csv.writer(file)  # Create a CSV writer object
    writer.writerows(data)      # Write the sample data to the CSV file

def calculate_averages(input_file_name, output_file_name):
    """Calculate averages from a CSV input file and save to an output file."""
    print(f"Calculating averages from {input_file_name}...")
    scores = OrderedDict()  # Store names and their corresponding grades
    
    # Read scores from the input CSV file
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)  # Create a CSV reader object
        for row in reader:          # Iterate through each row in the CSV
            name = row[0]           # The first element is the name
            grades = list(map(float, row[1:]))  # Convert remaining elements to floats
            scores[name] = grades    # Store name and grades in the dictionary

    # Calculate averages for each name
    averages = OrderedDict()
    for name, grades in scores.items():
        averages[name] = mean(grades)  # Use the mean function to calculate the average

    # Write the averages to the output CSV file
    with open(output_file_name, mode='w') as file:
        for name, avg in averages.items():
            file.write(f"{name},{avg}\n")  # Write each name and its average
    print(f"Averages saved to {output_file_name}")

def calculate_sorted_averages(input_file_name, output_file_name):
    """Calculate and save sorted averages from a CSV input file."""
    print(f"Calculating sorted averages...")
    scores = OrderedDict()  # Store names and their corresponding grades

    # Read scores from the input CSV file
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Get the name
            grades = list(map(float, row[1:]))  # Convert grades to floats
            scores[name] = grades  # Store in dictionary
    
    # Calculate averages for each name
    averages = OrderedDict()
    for name, grades in scores.items():
        averages[name] = mean(grades)  # Calculate average for each name
    
    # Sort averages by score (ascending) and then by name (alphabetical)
    sorted_averages = sorted(averages.items(), key=lambda x: (x[1], x[0]))
    
    # Write sorted averages to the output CSV file
    with open(output_file_name, mode='w') as file:
        for name, avg in sorted_averages:
            file.write(f"{name},{avg}\n")  # Write each name and its sorted average
    print(f"Sorted averages saved to {output_file_name}")

def calculate_three_best(input_file_name, output_file_name):
    """Calculate and save the three best averages from a CSV input file."""
    print(f"Calculating three best averages...")
    scores = OrderedDict()  # Store names and their corresponding grades
    
    # Read scores from the input CSV file
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Get the name
            grades = list(map(float, row[1:]))  # Convert grades to floats
            scores[name] = grades  # Store in dictionary
    
    # Calculate averages for each name
    averages = OrderedDict()
    for name, grades in scores.items():
        averages[name] = mean(grades)  # Calculate average for each name
    
    # Get the top three averages, sorted by score (highest first)
    top_averages = sorted(averages.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    # Write the top three averages to the output CSV file
    with open(output_file_name, mode='w') as file:
        for name, avg in top_averages:
            file.write(f"{name},{avg}\n")  # Write each name and its average
    print(f"Three best averages saved to {output_file_name}")

def calculate_three_worst(input_file_name, output_file_name):
    """Calculate and save the three worst averages from a CSV input file."""
    print(f"Calculating three worst averages...")
    scores = OrderedDict()  # Store names and their corresponding grades
    
    # Read scores from the input CSV file
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Get the name
            grades = list(map(float, row[1:]))  # Convert grades to floats
            scores[name] = grades  # Store in dictionary
    
    # Calculate averages for each name
    averages = OrderedDict()
    for name, grades in scores.items():
        averages[name] = mean(grades)  # Calculate average for each name
    
    # Get the bottom three averages, sorted by score (lowest first)
    bottom_averages = sorted(averages.items(), key=lambda x: (x[1], x[0]))[:3]
    
    # Write the bottom three averages to the output CSV file
    with open(output_file_name, mode='w') as file:
        for _, avg in bottom_averages:
            file.write(f"{avg}\n")  # Write only averages, no names
    print(f"Three worst averages saved to {output_file_name}")

def calculate_average_of_averages(input_file_name, output_file_name):
    """Calculate and save the overall average of averages from a CSV input file."""
    print(f"Calculating average of averages...")
    scores = OrderedDict()  # Store names and their corresponding grades
    
    # Read scores from the input CSV file
    with open(input_file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Get the name
            grades = list(map(float, row[1:]))  # Convert grades to floats
            scores[name] = grades  # Store in dictionary
    
    # Calculate average of averages
    averages = [mean(grades) for grades in scores.values()]  # List of averages for each name
    overall_mean = mean(averages)  # Calculate the overall average
    
    # Write the overall average to the output CSV file
    with open(output_file_name, mode='w') as file:
        file.write(f"{overall_mean}\n")  # Write the overall average
    print(f"Average of averages saved to {output_file_name}")

# Main execution block
if __name__ == "__main__":
    # Execute each function to perform the calculations and save results
    calculate_averages('input.csv', 'task1_output.csv')
    calculate_sorted_averages('input.csv', 'task2_output.csv')
    calculate_three_best('input.csv', 'task3_output.csv')
    calculate_three_worst('input.csv', 'task4_output.csv')
    calculate_average_of_averages('input.csv', 'task5_output.csv')
    print("All tasks completed.")