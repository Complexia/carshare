import unittest
from mp.controller import EncryptPassword, RegistrationController
import json, requests

class RegistrationControllerTest(unittest.TestCase):

    _registrationController = RegistrationController()

    def setUp(self):
        return super().setUp()

    def testRegister(self):
        encryptor = EncryptPassword()
        self.assertIsNotNone(self._registrationController.register('Ridoy', encryptor.hash('Abch#3'),'Mehedi','Hasan','email@email.com', 'None'))

    def tearDown(self):
        response = requests.get('http://localhost:5000/css/api/v1.0/users?email=email@email.com')
        user = json.loads(response.text)['users']
        requests.delete('http://localhost:5000/css/api/v1.0/users/{}'.format(user[0]['id']))
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
