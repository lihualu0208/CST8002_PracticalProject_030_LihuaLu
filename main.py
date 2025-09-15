# main.py
"""
CST8002 - Practical Project 1
Professor: Stanley Pieda
Due Date: 2025-09-21
Author: Lihua Lu

This is the main program that reads the seabird population dataset,
creates record objects, and displays them on screen.
"""

import csv
import os
from seabird_record import SeabirdRecord

def read_seabird_data(filename, max_records=10):
    """
    Reads seabird data from a CSV file and creates SeabirdRecord objects.
    
    This function demonstrates File-IO, exception handling, and data parsing
    from the specified CSV file. It reads the data and creates record objects
    stored in a list data structure.
    
    Parameters:
        filename (str): The path to the CSV file to read
        max_records (int): Maximum number of records to read (default: 5)
    
    Returns:
        list: A list of SeabirdRecord objects
    
    Raises:
        FileNotFoundError: If the specified file cannot be found
        ValueError: If there are issues parsing the data
    """
    records = []
    
    try:
        # Use latin-1 encoding which handles French characters better
        with open(filename, 'r', newline='', encoding='latin-1') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Skip the header row (first two lines contain column names)
            next(csv_reader)  # English headers
            next(csv_reader)  # French headers
            
            # Read and parse data records
            for i, row in enumerate(csv_reader):
                if i >= max_records:
                    break
                
                # Parse each field from the CSV row
                transect_number = int(row[0])
                transect_name = row[1]
                year = int(row[2])
                species_code = row[3]
                total_bird_count = int(row[4])
                total_transect_distance = float(row[5])
                
                # Create a new SeabirdRecord object
                record = SeabirdRecord(
                    transect_number, transect_name, year, species_code,
                    total_bird_count, total_transect_distance
                )
                
                # Add to our list of records
                records.append(record)
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise
    except ValueError as e:
        print(f"Error parsing data: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    
    return records

def display_records(records):
    """
    Displays seabird records on the screen.
    
    This function demonstrates looping through a data structure (list)
    and outputting information to the console.
    
    Parameters:
        records (list): A list of SeabirdRecord objects to display
    """
    print("\n" + "="*90)
    print("SEABIRD POPULATION RECORDS")
    print("="*90)
    
    # Loop through each record and display it
    for i, record in enumerate(records, 1):
        print(f"{i}. {record}")
    
    print("="*90)

def main():
    """
    Main function that orchestrates the program execution.
    
    This function demonstrates the use of variables, method calls,
    exception handling, and program flow control.
    """
    # Display programmer name (always visible)
    programmer_name = "Lihua Lu"  # Replace with your actual name
    print(f"Programmer: {programmer_name}")
    print("-" * 60)
    
    # Define the filename of our dataset
    data_file = "pacific_rim_nrp_coastalmarine_seabird_populations_1994-2017_data.csv"
    
    # Check if file exists first
    if not os.path.isfile(data_file):
        print(f"ERROR: File '{data_file}' not found!")
        print(f"Current directory: {os.getcwd()}")
        print("Please make sure the CSV file is in the same directory.")
        return
    
    try:
        # Read data from file and create record objects
        seabird_records = read_seabird_data(data_file)
        
        # Display the records on screen
        display_records(seabird_records)
        
    except Exception as e:
        print(f"Program terminated due to error: {e}")
    
    # Keep programmer name visible at the end
    print(f"\nProgrammer: {programmer_name}")

# API library usage example (standard Python library)
if __name__ == "__main__":
    """
    Entry point of the program when executed directly.
    This demonstrates the use of the standard Python library API.
    """
    main()