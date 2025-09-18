# presentation/menu_system.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-19
Author: Lihua Lu

This module contains the menu system for user interaction with seabird records.
"""

import os
from business.seabird_service import SeabirdService

class MenuSystem:
    """
    Handles the presentation layer and user interaction.
    """
    
    def __init__(self):
        """Initializes the menu system with a seabird service."""
        self.service = SeabirdService()
        self.programmer_name = "Lihua Lu"
    
    def display_programmer_name(self):
        """Displays the programmer's name."""
        print(f"\nProgram by {self.programmer_name}")
        print("-" * 50)
    
    def display_menu(self):
        """Displays the main menu options."""
        print("\n=== SEABIRD RECORDS MANAGEMENT SYSTEM ===")
        print("1. Load records from file")
        print("2. Display all records")
        print("3. Display a single record")
        print("4. Add a new record")
        print("5. Edit a record")
        print("6. Delete a record")
        print("7. Save records to file")
        print("8. Reload data from dataset")
        print("0. Exit")
        print("-" * 50)
    
    def display_records(self, records):
        """
        Displays seabird records.
        
        Parameters:
            records (list): List of SeabirdRecord objects to display
        """
        if not records:
            print("No records to display.")
            return
        
        print(f"\nDisplaying {len(records)} records:")
        print("=" * 90)
        
        # Display programmer name every 10 records
        for i, record in enumerate(records, 1):
            print(f"{i}. {record}")
            if i % 10 == 0:
                print(f"\nProgram by {self.programmer_name}")
                print("-" * 50)
        
        print("=" * 90)
        print(f"Program by {self.programmer_name}")
    
    def display_single_record(self, index):
        """
        Displays a single record.
        
        Parameters:
            index (int): The index of the record to display
        """
        record = self.service.get_record_by_index(index)
        if record:
            print(f"\nRecord {index + 1}:")
            print("=" * 90)
            print(record)
            print("=" * 90)
            print(f"Program by {self.programmer_name}")
        else:
            print("Invalid record index.")
    
    def get_record_input(self):
        """
        Gets user input for creating a new record.
        
        Returns:
            SeabirdRecord: A new SeabirdRecord object, or None if input is invalid
        """
        try:
            print("\nEnter record details:")
            transect_number = int(input("Transect Number: "))
            transect_name = input("Transect Name: ")
            year = int(input("Year: "))
            species_code = input("Species Code: ")
            total_bird_count = int(input("Total Bird Count: "))
            total_transect_distance = float(input("Total Transect Distance (km): "))
            
            from model.seabird_record import SeabirdRecord
            return SeabirdRecord(transect_number, transect_name, year, 
                               species_code, total_bird_count, total_transect_distance)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return None
    
    def run(self):
        """Runs the main menu system."""
        data_file = "data/pacific_rim_nrp_coastalmarine_seabird_populations_1994-2017_data.csv"
        
        # Try to load data on startup
        if os.path.exists(data_file):
            print("Loading data on startup...")
            if self.service.load_records_from_file(data_file):
                print(f"Successfully loaded {len(self.service.get_all_records())} records.")
            else:
                print("Failed to load data on startup.")
        else:
            print("Data file not found. Please load data manually.")
        
        while True:
            self.display_programmer_name()
            self.display_menu()
            
            try:
                choice = input("Enter your choice (0-8): ")
                
                if choice == "0":
                    print("Goodbye!")
                    break
                
                elif choice == "1":
                    filename = input("Enter filename (or press Enter for default): ").strip()
                    if not filename:
                        filename = data_file
                    
                    max_records = input("Enter maximum records to load (default 100): ").strip()
                    max_records = int(max_records) if max_records else 100
                    
                    if self.service.load_records_from_file(filename, max_records):
                        print(f"Successfully loaded {len(self.service.get_all_records())} records.")
                    else:
                        print("Failed to load records.")
                
                elif choice == "2":
                    records = self.service.get_all_records()
                    self.display_records(records)
                
                elif choice == "3":
                    try:
                        index = int(input("Enter record index: ")) - 1
                        self.display_single_record(index)
                    except ValueError:
                        print("Invalid index.")
                
                elif choice == "4":
                    record = self.get_record_input()
                    if record:
                        self.service.add_record(record)
                        print("Record added successfully.")
                    else:
                        print("Failed to add record.")
                
                elif choice == "5":
                    try:
                        index = int(input("Enter record index to edit: ")) - 1
                        record = self.service.get_record_by_index(index)
                        if record:
                            print(f"Editing record {index + 1}:")
                            print(record)
                            new_record = self.get_record_input()
                            if new_record and self.service.update_record(index, new_record):
                                print("Record updated successfully.")
                            else:
                                print("Failed to update record.")
                        else:
                            print("Invalid record index.")
                    except ValueError:
                        print("Invalid index.")
                
                elif choice == "6":
                    try:
                        index = int(input("Enter record index to delete: ")) - 1
                        if self.service.delete_record(index):
                            print("Record deleted successfully.")
                        else:
                            print("Invalid record index.")
                    except ValueError:
                        print("Invalid index.")
                
                elif choice == "7":
                    filename = input("Enter filename (or press Enter to generate): ").strip()
                    if not filename:
                        filename = None
                    
                    saved_file = self.service.save_records_to_file(filename)
                    if saved_file:
                        print(f"Records saved to {saved_file}.")
                    else:
                        print("Failed to save records.")
                
                elif choice == "8":
                    if self.service.load_records_from_file(data_file):
                        print(f"Successfully reloaded {len(self.service.get_all_records())} records.")
                    else:
                        print("Failed to reload data.")
                
                else:
                    print("Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
                
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")