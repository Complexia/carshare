import unittest, requests, json
from apiController import ApiController

class ApiControllerTest(unittest.TestCase):
    __apiController = ApiController()

    def setUp(self):
        self.__errorMessage = {"error":"Not found"}
        self.__carData = {'id': 99, 'make': 'Ford Falcon', 'bodyType': 'SUV', 'colour': 'Blue', 'seats': 2, 'xCoordinate': 45, \
                'yCoordinate': -12, 'costPerHour': 25.5, 'islocked': 1}
        return super().setUp()

    def testGetRequest(self):
        jsonResult = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')

        self.assertNotEqual(jsonResult, self.__errorMessage)
    
    def testBadGetRequest(self):
        jsonResult = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/card')

        self.assertEqual(jsonResult, self.__errorMessage)

    def testPostRequest(self):
        jsonResult = self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/cars', self.__carData)

        print(jsonResult.text)

        self.assertEqual(jsonResult.text['car'], self.__carData)

    def tearDown(self):
        requests.delete('http://localhost:5000/css/api/v1.0/cars/99')
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()