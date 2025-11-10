# tests/test_polymorphism.py
"""
CST8002 - Practical Project Part 03
Professor: Stanley Pieda
Due Date: 2025-11-20
Author: Lihua Lu

Unit tests for inheritance and polymorphism features.
This test specifically tests the new inheritance and polymorphism functionality
added for Practical Project Part 3.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.seabird_record import SeabirdRecord, DetailedSeabirdRecord, CompactSeabirdRecord
from business.seabird_service import SeabirdService

class TestInheritancePolymorphism(unittest.TestCase):
    """Test cases for inheritance and polymorphism features."""
    
    def setUp(self):
        """Set up test fixtures."""
        print("Setting up test fixtures...")
        self.standard_record = SeabirdRecord(1, "Test Transect", 2023, "TEST", 100, 50.0)
        self.detailed_record = DetailedSeabirdRecord(2, "Detailed Transect", 2023, "DETL", 200, 75.0)
        self.compact_record = CompactSeabirdRecord(3, "Compact Transect", 2023, "COMP", 150, 60.0)
        self.service = SeabirdService()
    
    def test_01_inheritance_relationship(self):
        """Test that subclasses properly inherit from SeabirdRecord base class."""
        print("Testing inheritance relationships...")
        
        # Test that subclasses are instances of the base class
        self.assertIsInstance(self.detailed_record, SeabirdRecord, 
                            "DetailedSeabirdRecord should inherit from SeabirdRecord")
        self.assertIsInstance(self.compact_record, SeabirdRecord,
                            "CompactSeabirdRecord should inherit from SeabirdRecord")
        
        # Test subclass relationships
        self.assertTrue(issubclass(DetailedSeabirdRecord, SeabirdRecord),
                       "DetailedSeabirdRecord should be a subclass of SeabirdRecord")
        self.assertTrue(issubclass(CompactSeabirdRecord, SeabirdRecord),
                       "CompactSeabirdRecord should be a subclass of SeabirdRecord")
        
        print("✓ Inheritance relationships verified")
    
    def test_02_polymorphic_method_override(self):
        """Test that each subclass properly overrides the get_display_format method."""
        print("Testing polymorphic method overrides...")
        
        # Get display format from each record type
        standard_output = self.standard_record.get_display_format()
        detailed_output = self.detailed_record.get_display_format()
        compact_output = self.compact_record.get_display_format()
        
        # Each should have different format patterns specific to their class
        self.assertIn("Transect:", standard_output,
                     "Standard format should contain 'Transect:'")
        self.assertIn("DETAILED >>", detailed_output,
                     "Detailed format should contain 'DETAILED >>'")
        self.assertIn("[COMP]", compact_output,
                     "Compact format should contain '[COMP]'")
        
        # Test that outputs are actually different
        self.assertNotEqual(standard_output, detailed_output,
                          "Standard and Detailed outputs should be different")
        self.assertNotEqual(standard_output, compact_output,
                          "Standard and Compact outputs should be different")
        self.assertNotEqual(detailed_output, compact_output,
                          "Detailed and Compact outputs should be different")
        
        print("✓ Polymorphic method overrides verified")
    
    def test_03_service_polymorphic_record_creation(self):
        """Test that SeabirdService can create different record types polymorphically."""
        print("Testing polymorphic record creation in service...")
        
        # Test standard record creation
        self.service.set_record_type("standard")
        record1 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record1, SeabirdRecord,
                            "Service should create SeabirdRecord for standard type")
        self.assertNotIsInstance(record1, (DetailedSeabirdRecord, CompactSeabirdRecord),
                               "Standard record should not be subclass instance")
        
        # Test detailed record creation
        self.service.set_record_type("detailed")
        record2 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record2, DetailedSeabirdRecord,
                            "Service should create DetailedSeabirdRecord for detailed type")
        
        # Test compact record creation
        self.service.set_record_type("compact")
        record3 = self.service.create_record(1, "Test", 2023, "TST", 100, 50.0)
        self.assertIsInstance(record3, CompactSeabirdRecord,
                            "Service should create CompactSeabirdRecord for compact type")
        
        print("✓ Polymorphic record creation verified")
    
    def test_04_polymorphic_behavior_demonstration(self):
        """Test the polymorphic behavior demonstration method."""
        print("Testing polymorphic behavior demonstration...")
        
        # Add different types of records to service
        self.service.add_record(self.standard_record)
        self.service.add_record(self.detailed_record)
        self.service.add_record(self.compact_record)
        
        # Get formatted outputs - should use appropriate methods for each
        formatted_outputs = self.service.demonstrate_polymorphism()
        
        self.assertEqual(len(formatted_outputs), 3,
                        "Should have 3 formatted outputs")
        
        # Each output should reflect its specific format
        self.assertIn("Transect:", formatted_outputs[0],
                     "First output should be standard format")
        self.assertIn("DETAILED >>", formatted_outputs[1],
                     "Second output should be detailed format")
        self.assertIn("[COMP]", formatted_outputs[2],
                     "Third output should be compact format")
        
        print("✓ Polymorphic behavior demonstration verified")
    
    def test_05_record_type_management(self):
        """Test record type setting and getting functionality."""
        print("Testing record type management...")
        
        # Test initial default type
        self.assertEqual(self.service.get_record_type(), "standard",
                        "Default record type should be 'standard'")
        
        # Test setting different record types
        self.assertTrue(self.service.set_record_type("detailed"),
                       "Should successfully set record type to 'detailed'")
        self.assertEqual(self.service.get_record_type(), "detailed",
                        "Record type should be 'detailed' after setting")
        
        self.assertTrue(self.service.set_record_type("compact"),
                       "Should successfully set record type to 'compact'")
        self.assertEqual(self.service.get_record_type(), "compact",
                        "Record type should be 'compact' after setting")
        
        self.assertTrue(self.service.set_record_type("standard"),
                       "Should successfully set record type to 'standard'")
        self.assertEqual(self.service.get_record_type(), "standard",
                        "Record type should be 'standard' after setting")
        
        # Test invalid record type
        self.assertFalse(self.service.set_record_type("invalid"),
                        "Should reject invalid record type")
        self.assertEqual(self.service.get_record_type(), "standard",
                        "Record type should remain unchanged after invalid set")
        
        print("✓ Record type management verified")
    
    def test_06_polymorphic_method_signature(self):
        """Test that all record types have the same method signature for get_display_format."""
        print("Testing polymorphic method signature consistency...")
        
        # Test that all classes have the get_display_format method
        self.assertTrue(hasattr(SeabirdRecord, 'get_display_format'),
                       "SeabirdRecord should have get_display_format method")
        self.assertTrue(hasattr(DetailedSeabirdRecord, 'get_display_format'),
                       "DetailedSeabirdRecord should have get_display_format method")
        self.assertTrue(hasattr(CompactSeabirdRecord, 'get_display_format'),
                       "CompactSeabirdRecord should have get_display_format method")
        
        # Test that methods can be called with same signature (no parameters)
        try:
            result1 = self.standard_record.get_display_format()
            result2 = self.detailed_record.get_display_format()
            result3 = self.compact_record.get_display_format()
            
            # All should return strings
            self.assertIsInstance(result1, str, "Standard format should return string")
            self.assertIsInstance(result2, str, "Detailed format should return string")
            self.assertIsInstance(result3, str, "Compact format should return string")
            
        except Exception as e:
            self.fail(f"Polymorphic method call failed: {e}")
        
        print("✓ Polymorphic method signature consistency verified")


def run_tests_with_name_display():
    """Run tests with visible name display for screenshot requirements."""
    print("=" * 70)
    print("UNIT TEST EXECUTION - PRACTICAL PROJECT PART 3")
    print("Unit Testing Framework In Use: unittest")
    print("Student: Lihua Lu")
    print("Student ID: 041133202")
    print("Testing: Inheritance and Polymorphism Features")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestInheritancePolymorphism)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 70)
    print("TEST EXECUTION COMPLETE")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("Student: Lihua Lu")
    print("=" * 70)
    
    return result


if __name__ == '__main__':
    run_tests_with_name_display()