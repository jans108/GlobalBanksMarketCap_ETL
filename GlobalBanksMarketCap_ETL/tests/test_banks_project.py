import unittest
from unittest.mock import patch, Mock

import pandas as pd
from banks_project import extract

class TestBanksProject(unittest.TestCase):
    @patch('banks_project.requests.get')
    def test_extract_returns_dataframe(self, mock_get):
        sample_html = """
        <html>
            <body>
                <table><tbody></tbody></table>
                <table><tbody></tbody></table>
                <table>
                    <tbody>
                        <tr>
                            <td><a href="#">Bank A</a></td>
                            <td>Ignore this</td>
                            <td>100</td>
                        </tr>
                        <tr>
                            <td><a href="#">Bank B</a></td>
                            <td>Ignore this</td>
                            <td>200</td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        """
        # Mocking reguests.get()
        mock_response = Mock()
        mock_response.text = sample_html
        mock_get.return_value = mock_response
        # Act
        url = "https://example.com"
        data_attributes = ["Name", "MC_USD_Billion"]
        result = extract(url, data_attributes)
        # Assert
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.columns), data_attributes)
        self.assertEqual(len(result), 2)