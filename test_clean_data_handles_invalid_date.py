# formative-data-cleaning-task
import unittest
import csv
from io import StringIO
from datetime import datetime
from data_cleaning_M1 import clean_data


class TestCleanDataHandlesInvalidDate(unittest.TestCase):
    def test_clean_data_handles_invalid_date(self):
        """
        Test that clean_data handles an invalid date by leaving it unchanged.
        """
        # Sample input with an invalid date
        sample_csv = [
            "time,latitude\n",        # Header
            "invalid_date,34.0\n"     # Row with invalid date
        ]
        
        # Expected output (invalid date remains unchanged)
        expected = [
            "time,latitude\n",
            "invalid_date,34.0\n"
        ]
        
        # Run the function and verify the result
        cleaned_lines = clean_data(sample_csv)
        self.assertEqual(cleaned_lines, expected)

if __name__ == '__main__':
    unittest.main()