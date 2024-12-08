import csv
from datetime import datetime

def write_data_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'Gender', 'Address', 'Birth Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    filename = 'chocolate.csv'
    # Sample data
    data = [
        {'Name': 'John Doe', 'Age': 30, 'Gender': 'Male', 'Address': '123 Main St, City, Country', 'Birth Date': '1993-05-15'},
        {'Name': 'Jane Smith', 'Age': 25, 'Gender': 'Female', 'Address': '456 Elm St, Town, Country', 'Birth Date': '1998-09-22'},
        {'Name': 'Bob Johnson', 'Age': 45, 'Gender': 'Male', 'Address': '789 Oak Ave, Village, Country', 'Birth Date': '1978-12-10'}
    ]
    write_data_to_csv(filename, data)
    print(f"Data has been written to {filename}")