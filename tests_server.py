import unittest
import json
from server import app, my_message

class FlaskTestCase(unittest.TestCase):

    # Test the GET method
    def test_get(self):
        tester = app.test_client(self)
        response = tester.get('/get')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Hi there!'})

    # Test the POST method
    def test_post(self):
        tester = app.test_client(self)
        response = tester.post(
            '/post',
            json={'message': 'Hello, Isha!'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'response': 'You sent: Hello, Isha!'})

    # Test the PUT method
    def test_put(self):
        tester = app.test_client(self)
        new_message = 'New message for testing PUT'
        response = tester.put(
            '/put',
            data=json.dumps({'message': new_message}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_message['message'], new_message)

 # Test the DELETE method
    def test_delete(self):
        tester = app.test_client(self)

        # Ensure there is a message to delete initially
        response = tester.get('/get')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'message', response.data)
                
        # Send DELETE request
        response = tester.delete('/delete')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['response'], 'Yayy! Message deleted!')      

if __name__ == '__main__':
    unittest.main()