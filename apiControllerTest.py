import unittest, requests, json
from mp.controller import ApiController

class ApiControllerTest(unittest.TestCase):
    __apiController = ApiController()

    def setUp(self):
        self.__errorMessage = {"error":"Not found"}
        self.__createdMessage = '<Response [201]>'
        self.__badRequest = '<Response [400]>'
        self.__internalError = '<Response [500]>'
        self.__carData = {
                'id': 99, 
                'make': 'Ford Falcon', 
                'bodyType': 'SUV', 
                'colour': 'Blue', 
                'seats': 2, 
                'xCoordinate': 45.7, 
                'yCoordinate': 12.5, 
                'costPerHour': 25.5, 
                'isLocked': 'true'
            }
        return super().setUp()

    def testGetRequest(self):
        jsonResult = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')

        self.assertNotEqual(jsonResult, self.__errorMessage)
    
    def testBadGetRequest(self):
        jsonResult = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/card')

        self.assertEqual(jsonResult, self.__errorMessage)

    def testPostRequest(self):
        jsonResult = self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/cars', self.__carData)

        self.assertEqual(str(jsonResult), self.__createdMessage)

    def testBadPostRequest(self):
        jsonResult = self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/cars', {'id': None})

        self.assertEqual(str(jsonResult), self.__badRequest)

    def tearDown(self):
        requests.delete('http://localhost:5000/css/api/v1.0/cars/99')
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()