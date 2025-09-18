# tests/test_seabird_service.py
"""
CST8002 - Practical Project Part 02
Professor: Stanley Pieda
Due Date: 2025-10-12
Author: Lihua Lu

Unit tests for the SeabirdService class.
"""

import unittest
import os
import tempfile
from business.seabird_service import SeabirdService
from model.seabird_record import SeabirdRecord

class TestSeabirdService(unittest.TestCase):
    """Test cases for SeabirdService class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.service = SeabirdService()
        self.test_record = SeabirdRecord(1, "Test Transect", 2023, "TEST", 100, 50.0)
        
        # Create a temporary CSV file for testing
        self.temp_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.temp_csv.write("Transect Number,Transect Name,Year,Species code,Total bird count,Total transect distance surveyed (km)\n")
        self.temp_csv.write("Numéro de transect,Nom du transect,Année,Code de l'espèce,Nombre total d'oiseaux,Distance totale du transect faisant l'objet du relevé (km)\n")
        self.temp_csv.write("1,WCT TRANSECT,1994,BRCO,97,349.00\n")
        self.temp_csv.write("1,WCT TRANSECT,1994,COMU,1756,349.00\n")
        self.temp_csv.close()
    
    def tearDown(self):
        """Tear down test fixtures."""
        # Remove temporary file
        if os.path.exists(self.temp_csv.name):
            os.unlink(self.temp_csv.name)
    
    def test_add_record(self):
        """Test adding a record to the service."""
        initial_count = len(self.service.get_all_records())
        self.service.add_record(self.test_record)
        self.assertEqual(len(self.service.get_all_records()), initial_count + 1)
    
    def test_get_record_by_index(self):
        """Test getting a record by index."""
        self.service.add_record(self.test_record)
        record = self.service.get_record_by_index(0)
        self.assertEqual(record.transect_number, self.test_record.transect_number)
        self.assertEqual(record.transect_name, self.test_record.transect_name)
    
    def test_update_record(self):
        """Test updating a record."""
        self.service.add_record(self.test_record)
        updated_record = SeabirdRecord(2, "Updated Transect", 2024, "UPDT", 200, 75.0)
        self.assertTrue(self.service.update_record(0, updated_record))
        
        record = self.service.get_record_by_index(0)
        self.assertEqual(record.transect_number, 2)
        self.assertEqual(record.transect_name, "Updated Transect")
    
    def test_delete_record(self):
        """Test deleting a record."""
        self.service.add_record(self.test_record)
        initial_count = len(self.service.get_all_records())
        self.assertTrue(self.service.delete_record(0))
        self.assertEqual(len(self.service.get_all_records()), initial_count - 1)
    
    def test_load_records_from_file(self):
        """Test loading records from a file."""
        success = self.service.load_records_from_file(self.temp_csv.name, max_records=2)
        self.assertTrue(success)
        self.assertEqual(len(self.service.get_all_records()), 2)
        
        # Verify the first record
        record = self.service.get_record_by_index(0)
        self.assertEqual(record.transect_number, 1)
        self.assertEqual(record.transect_name, "WCT TRANSECT")
        self.assertEqual(record.year, 1994)
        self.assertEqual(record.species_code, "BRCO")
        self.assertEqual(record.total_bird_count, 97)
        self.assertEqual(record.total_transect_distance, 349.00)
    
    def test_save_records_to_file(self):
        """Test saving records to a file."""
        self.service.add_record(self.test_record)
        
        # Save to a temporary file
        temp_output = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        temp_output.close()
        
        try:
            filename = self.service.save_records_to_file(temp_output.name)
            self.assertEqual(filename, temp_output.name)
            
            # Verify the file was created and has content
            self.assertTrue(os.path.exists(filename))
            with open(filename, 'r') as f:
                content = f.read()
                self.assertIn("Test Transect", content)
                self.assertIn("TEST", content)
        finally:
            if os.path.exists(temp_output.name):
                os.unlink(temp_output.name)

if __name__ == '__main__':
    unittest.main()