import os
import unittest
from unittest.mock import patch, MagicMock
from data_cleaning_M1 import import_data

class TestImportDataCorrectOutput(unittest.TestCase):
    @patch('data_cleaning_M1.requests.get')
    def test_import_data_output(self, mock_get):
        # Define a dummy CSV string as expected output.
        dummy_csv = "time,other_field\n2023-01-01T12:00:00Z,sample\n"
        
        # Set up a mock response object.
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = dummy_csv
        mock_get.return_value = mock_response
        
        # Call the import_data function.
        result = import_data("http://dummyurl.com")
        
        # Check that the return value is a list.
        self.assertIsInstance(result, list, "The output should be a list of strings.")
        
        # Check that the list is not empty.
        self.assertGreater(len(result), 0, "The output list should contain at least one line.")
        
        
     

if __name__ == "__main__":
    unittest.main()