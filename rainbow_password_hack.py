import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Read data from the input CSV file
    users = OrderedDict()  # To maintain the order of input
    with open(input_file_name, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            name, hashed_password = row
            users[name] = hashed_password

    results = []

    # Attempt to hack each hashed password
    for name, hashed_password in users.items():
        for i in range(1000, 10000):  # Check all possible passwords
            password = str(i).encode()  # Convert the number to bytes
            hashed_attempt = hashlib.sha256(password).hexdigest()  # Hash the password
            if hashed_attempt == hashed_password:
                results.append((name, i))  # Store the name and the found password
                break  # Stop searching once the password is found

    # Write the results to the output CSV file
    with open(output_file_name, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for name, password in results:
            writer.writerow([name, password])

# Note: Do not change the function name or place any code outside of this function.
