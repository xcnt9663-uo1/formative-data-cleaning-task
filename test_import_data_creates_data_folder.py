import unittest
from unittest.mock import patch
import os
from data_cleaning_M1 import import_data

class TestImportDataCreatesDataFolder(unittest.TestCase):
    @patch('requests.get')
    def test_import_data_creates_data_folder(self, mock_get):
        """Test that import_data creates the data/ folder if it doesn't exist."""
        # Arrange: Ensure data folder doesn’t exist
        if os.path.exists('data'):
            os.rmdir('data')  # Assumes folder is empty
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "header\nline1\nline2\n"

        # Act
        import_data("http://example.com/data.csv")

        # Assert
        self.assertTrue(os.path.exists('data'))

if __name__ == '__main__':
    unittest.main()