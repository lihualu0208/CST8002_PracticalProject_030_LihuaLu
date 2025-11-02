# persistence/data_handler.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-12
Author: Lihua Lu

This module handles all file I/O operations for reading and writing seabird data.
"""

import csv
import os
import uuid
from model.seabird_record import SeabirdRecord

class DataHandler:
    """
    Handles all data persistence operations for seabird records.
    """
    
    @staticmethod
    def read_seabird_data(filename, max_records=100):
        """
        Reads seabird data from a CSV file and creates SeabirdRecord objects.
        
        Parameters:
            filename (str): The path to the CSV file to read
            max_records (int): Maximum number of records to read
            
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
                
                # Skip the header rows (first two lines contain column names)
                next(csv_reader)  # English headers
                next(csv_reader)  # French headers
                
                # Read and parse data records
                for i, row in enumerate(csv_reader):
                    if i >= max_records:
                        break
                    
                    if len(row) < 6:
                        continue  # Skip incomplete rows
                    
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
    
    @staticmethod
    def save_seabird_data(records, filename=None):
        """
        Saves seabird records to a CSV file.
        
        Parameters:
            records (list): List of SeabirdRecord objects to save
            filename (str): Optional filename, will generate UUID if not provided
            
        Returns:
            str: The filename used for saving
            
        Raises:
            IOError: If there are issues writing to the file
        """
        if filename is None:
            # Generate a unique filename using UUID
            filename = f"seabird_data_{uuid.uuid4()}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                # Write header
                file.write("Transect Number,Transect Name,Year,Species code,Total bird count,Total transect distance surveyed (km)\n")
                
                # Write each record
                for record in records:
                    file.write(record.to_csv_string() + "\n")
                    
            return filename
            
        except Exception as e:
            print(f"Error saving data: {e}")
            raise