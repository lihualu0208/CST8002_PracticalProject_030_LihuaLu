# model/seabird_record.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-19
Author: Lihua Lu

This file contains the SeabirdRecord class which represents a single record
from the Pacific Rim seabird population dataset.
"""

class SeabirdRecord:
    """
    A class to represent a single seabird observation record from the dataset.
    
    Attributes:
        transect_number (int): The transect number where observation was made
        transect_name (str): The name of the transect
        year (int): The year of observation
        species_code (str): The code representing the bird species
        total_bird_count (int): Total number of birds observed
        total_transect_distance (float): Distance surveyed in kilometers
    """
    
    def __init__(self, transect_number, transect_name, year, species_code, 
                 total_bird_count, total_transect_distance):
        """
        Constructs all the necessary attributes for the seabird record object.
        
        Parameters:
            transect_number (int): The transect number
            transect_name (str): The name of the transect
            year (int): The year of observation
            species_code (str): The species code
            total_bird_count (int): Total bird count
            total_transect_distance (float): Distance surveyed in km
        """
        self.transect_number = transect_number
        self.transect_name = transect_name
        self.year = year
        self.species_code = species_code
        self.total_bird_count = total_bird_count
        self.total_transect_distance = total_transect_distance
    
    def __str__(self):
        """
        Returns a string representation of the seabird record.
        
        Returns:
            str: Formatted string containing all record attributes
        """
        return (f"Transect: {self.transect_number} ({self.transect_name}), "
                f"Year: {self.year}, Species: {self.species_code}, "
                f"Count: {self.total_bird_count}, Distance: {self.total_transect_distance}km")
    
    def to_csv_string(self):
        """
        Returns a CSV string representation of the seabird record.
        
        Returns:
            str: CSV formatted string
        """
        return (f"{self.transect_number},{self.transect_name},{self.year},"
                f"{self.species_code},{self.total_bird_count},{self.total_transect_distance}")