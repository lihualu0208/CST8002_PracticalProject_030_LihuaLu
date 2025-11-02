# business/seabird_service.py
"""
CST8002 - Practical Project Part 03
Professor: Stanley Pieda
Due Date: 2025-11-16
Author: Lihua Lu

This module contains the business logic for managing seabird records
with inheritance and polymorphism support.
"""

from model.seabird_record import SeabirdRecord, DetailedSeabirdRecord, CompactSeabirdRecord

class SeabirdService:
    """
    Service class that handles business logic for seabird records
    with polymorphic record types.
    """
    
    def __init__(self):
        """Initializes the service with an empty list of records."""
        self.records = []
        self.record_type = "standard"  # Initialize with default value
    
    def set_record_type(self, record_type):
        """
        Sets the type of record to create for new entries.
        
        Parameters:
            record_type (str): "standard", "detailed", or "compact"
            
        Returns:
            bool: True if successful, False otherwise
        """
        if record_type in ["standard", "detailed", "compact"]:
            self.record_type = record_type
            return True
        return False
    
    def get_record_type(self):
        """
        Gets the current record type.
        
        Returns:
            str: Current record type
        """
        return self.record_type
    
    def create_record(self, transect_number, transect_name, year, species_code, 
                     total_bird_count, total_transect_distance):
        """
        Creates a new record using the current record type.
        
        Parameters:
            Same as SeabirdRecord constructor
            
        Returns:
            SeabirdRecord: A record of the appropriate subtype
        """
        if self.record_type == "detailed":
            return DetailedSeabirdRecord(transect_number, transect_name, year, 
                                       species_code, total_bird_count, total_transect_distance)
        elif self.record_type == "compact":
            return CompactSeabirdRecord(transect_number, transect_name, year, 
                                      species_code, total_bird_count, total_transect_distance)
        else:
            return SeabirdRecord(transect_number, transect_name, year, 
                               species_code, total_bird_count, total_transect_distance)
    
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
            loaded_records = DataHandler.read_seabird_data(filename, max_records)
            
            # Convert loaded records to current type
            self.records = []
            for record in loaded_records:
                new_record = self.create_record(
                    record.transect_number, record.transect_name, record.year,
                    record.species_code, record.total_bird_count, record.total_transect_distance
                )
                self.records.append(new_record)
                
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
    
    def demonstrate_polymorphism(self):
        """
        Demonstrates polymorphic behavior by calling get_display_format
        on all records regardless of their actual type.
        
        Returns:
            list: Formatted strings from all records
        """
        formatted_records = []
        for record in self.records:
            # This call is polymorphic - it will use the appropriate
            # get_display_format method based on the actual object type
            formatted_records.append(record.get_display_format())
        return formatted_records