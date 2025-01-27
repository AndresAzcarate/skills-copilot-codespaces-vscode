# Generar test para el siguiente Curl
#curl -L \
#  -H "Accept: application/vnd.github+json" \
#  -H "Authorization: Bearer <YOUR-TOKEN>" \
#  https://api.github.com/enterprises/PaloItAmericas/GitHub Copilot/usage


import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from curl_test import app

class TestCurl(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('curl_test.requests.get')
    def test_get_odd_numbers(self, mock_get):
        mock_get.return_value.json.return_value = [1, 3, 5, 7, 9]
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()
