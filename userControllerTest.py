import unittest
from api import app
from mp.controller import EncryptPassword

class TestUserController(unittest.TestCase):
    __encryptor = EncryptPassword()
    __resourceFound = '<Response streamed [200 OK]>'
    __resourceCreated = '<Response streamed [201 CREATED]>'
    __userData = None

    def setUp(self):
        self.__userData = {
        'id': 999,
        'username': 'BrakaMonoga',
        'password': self.__encryptor.hash('Doitsu3#G'),
        'firstName': 'Rudol',
        'lastName': 'Stroheim',
        'email': 'cyborg@deutschland.com',
        'faceId': 'None',
        'type': 'admin'
    }
        return super().setUp()
    
    def __getRequest(self, url):
        return str(app.test_client().get(url))
    
    def __postRequest(self, url, data):
        return str(app.test_client().post(url, data=data))

    def __putRequest(self, url, data):
        return str(app.test_client().put(url, data=data))

    def __deleteRequest(self, url):
        return str(app.test_client().delete(url))

    def testGetUser(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/users/1'), self.__resourceFound)

    def testGetUsers(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/users'), self.__resourceFound)

    def testCreateUser(self):
        self.assertEqual(self.__postRequest('http://localhost:5000/css/api/v1.0/users', self.__userData), self.__resourceCreated)

    def testUpdateUser(self):
        self.assertEqual(self.__putRequest('http://localhost:5000/css/api/v1.0/users/1', {'username': 'Tenmei'}), self.__resourceCreated)

    def testDeleteUser(self):
        self.assertEqual(self.__deleteRequest('http://localhost:5000/css/api/v1.0/users/999'), self.__resourceFound)

if __name__ == '__main__':
    unittest.main() 