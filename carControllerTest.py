import unittest
from api import app

class TestCarController(unittest.TestCase):
    __resourceFound = '<Response streamed [200 OK]>'
    __resourceCreated = '<Response streamed [201 CREATED]>'
    __carData = None

    def setUp(self):
        self.__carData = {
            'id': 999,
            'make': 'Toyota Corolla',
            'bodyType': 'SUV',
            'colour': 'White',
            'seats': 4,
            'xCoordinate': 15.5,
            'yCoordinate': 25.6,
            'costPerHour': 30,
            'isLocked': 0
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

    def testGetCar(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/cars/1'), self.__resourceFound)

    def testGetCars(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/cars'), self.__resourceFound)

    def testCreateCar(self):
        self.assertEqual(self.__postRequest('http://localhost:5000/css/api/v1.0/cars', self.__carData), self.__resourceCreated)

    def testUpdateCar(self):
        self.assertEqual(self.__putRequest('http://localhost:5000/css/api/v1.0/cars/1', {'bodyType': 'SUV'}), self.__resourceFound)

    def testDeleteCar(self):
        self.assertEqual(self.__deleteRequest('http://localhost:5000/css/api/v1.0/cars/999'), self.__resourceFound)

if __name__ == '__main__':
    unittest.main() 