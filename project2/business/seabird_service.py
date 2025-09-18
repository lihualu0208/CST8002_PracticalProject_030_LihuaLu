# business/seabird_service.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-19
Author: Lihua Lu

This module contains the business logic for managing seabird records.
"""

from model.seabird_record import SeabirdRecord

class SeabirdService:
    """
    Service class that handles business logic for seabird records.
    """
    
    def __init__(self):
        """Initializes the service with an empty list of records."""
        self.records = []
    
    def load_records_from_file(self, filename, max_records=100):
        """
        Loads records from a file using the DataHandler.
        
        Parameters:
            filename (str): The path to the CSV file
            max_records (int): Maximum number of records to load
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            from persistence.data_handler import DataHandler
            self.records = DataHandler.read_seabird_data(filename, max_records)
            return True
        except Exception as e:
            print(f"Error loading records: {e}")
            return False
    
    def get_all_records(self):
        """
        Returns all records.
        
        Returns:
            list: All seabird records
        """
        return self.records
    
    def get_record_by_index(self, index):
        """
        Returns a record by its index.
        
        Parameters:
            index (int): The index of the record
            
        Returns:
            SeabirdRecord: The record at the specified index, or None if invalid
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None
    
    def add_record(self, record):
        """
        Adds a new record to the collection.
        
        Parameters:
            record (SeabirdRecord): The record to add
        """
        self.records.append(record)
    
    def update_record(self, index, record):
        """
        Updates a record at the specified index.
        
        Parameters:
            index (int): The index of the record to update
            record (SeabirdRecord): The updated record
            
        Returns:
            bool: True if successful, False otherwise
        """
        if 0 <= index < len(self.records):
            self.records[index] = record
            return True
        return False
    
    def delete_record(self, index):
        """
        Deletes a record at the specified index.
        
        Parameters:
            index (int): The index of the record to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False
    
    def save_records_to_file(self, filename=None):
        """
        Saves records to a file using the DataHandler.
        
        Parameters:
            filename (str): Optional filename
            
        Returns:
            str: The filename used for saving, or None if failed
        """
        try:
            from persistence.data_handler import DataHandler
            return DataHandler.save_seabird_data(self.records, filename)
        except Exception as e:
            print(f"Error saving records: {e}")
            return None