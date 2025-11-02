# tests/test_polymorphism.py
"""
CST8002 - Practical Project Part 03
Professor: Stanley Pieda
Due Date: 2025-11-16
Author: Lihua Lu

Unit tests for inheritance and polymorphism features.
"""

import unittest
from model.seabird_record import SeabirdRecord, DetailedSeabirdRecord, CompactSeabirdRecord
from business.seabird_service import SeabirdService

class TestInheritancePolymorphism(unittest.TestCase):
    """Test cases for inheritance and polymorphism features."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.standard_record = SeabirdRecord(1, "Test Transect", 2023, "TEST", 100, 50.0)
        self.detailed_record = DetailedSeabirdRecord(2, "Detailed Transect", 2023, "DETL", 200, 75.0)
        self.compact_record = CompactSeabirdRecord(3, "Compact Transect", 2023, "COMP", 150, 60.0)
        self.service = SeabirdService()
    
    def test_inheritance_relationship(self):
        """Test that subclasses inherit from SeabirdRecord."""
        self.assertIsInstance(self.detailed_record, SeabirdRecord)
        self.assertIsInstance(self.compact_record, SeabirdRecord)
        self.assertTrue(issubclass(DetailedSeabirdRecord, SeabirdRecord))
        self.assertTrue(issubclass(CompactSeabirdRecord, SeabirdRecord))
    
    def test_polymorphic_method_calls(self):
        """Test that each record type uses its own get_display_format method."""
        standard_output = self.standard_record.get_display_format()
        detailed_output = self.detailed_record.get_display_format()
        compact_output = self.compact_record.get_display_format()
        
        # Each should have different format patterns
        self.assertIn("Transect:", standard_output)
        self.assertIn("DETAILED >>", detailed_output)
        self.assertIn("[COMP]", compact_output)
    
    def test_service_record_creation(self):
        """Test that service creates appropriate record types."""
        # Test standard record creation
        self.service.set_record_type("standard")
        record1 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record1, SeabirdRecord)
        self.assertNotIsInstance(record1, (DetailedSeabirdRecord, CompactSeabirdRecord))
        
        # Test detailed record creation
        self.service.set_record_type("detailed")
        record2 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record2, DetailedSeabirdRecord)
        
        # Test compact record creation
        self.service.set_record_type("compact")
        record3 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record3, CompactSeabirdRecord)
    
    def test_polymorphic_demonstration(self):
        """Test the polymorphic demonstration method."""
        # Add different types of records to service
        self.service.add_record(self.standard_record)
        self.service.add_record(self.detailed_record)
        self.service.add_record(self.compact_record)
        
        # Get formatted outputs - should use appropriate methods for each
        formatted_outputs = self.service.demonstrate_polymorphism()
        
        self.assertEqual(len(formatted_outputs), 3)
        
        # Each output should reflect its specific format
        self.assertIn("Transect:", formatted_outputs[0])
        self.assertIn("DETAILED >>", formatted_outputs[1])
        self.assertIn("[COMP]", formatted_outputs[2])
    
    def test_record_type_setting(self):
        """Test setting different record types in service."""
        self.assertTrue(self.service.set_record_type("standard"))
        self.assertEqual(self.service.record_type, "standard")
        
        self.assertTrue(self.service.set_record_type("detailed"))
        self.assertEqual(self.service.record_type, "detailed")
        
        self.assertTrue(self.service.set_record_type("compact"))
        self.assertEqual(self.service.record_type, "compact")
        
        self.assertFalse(self.service.set_record_type("invalid"))
        self.assertEqual(self.service.record_type, "compact")  # Should remain unchanged

if __name__ == '__main__':
    unittest.main()