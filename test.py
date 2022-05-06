import unittest
import requests

class test_book(unittest.TestCase): 
     def test_connection(self):
        response = requests.get('http://localhost:5000/api/books')
        response.status_code
        self.assertEqual(response.status_code, 200 )

     def test_delete_data(self):
         response = requests.delete('http://localhost:5000/api/books/11')
         responseGet = requests.get('http://localhost:5000/api/books/11')
         self.assertEqual(responseGet.status_code, 404)
    
     def test_update(self):
         response = requests.put('http://localhost:5000/api/books/10')
         responseGet = requests.get('http://localhost:5000/api/books/10')
         self.assertEqual(responseGet.status_code, 200)

     def test_create(self):
         response = requests.post('http://localhost:5000/api/books')
         responseGet = requests.get('http://localhost:5000/api/books')
         self.assertEqual(responseGet.status_code, 200)
         
if __name__ == '__main__':
    unittest.main() 