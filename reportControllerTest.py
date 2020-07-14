import unittest
from api import app

class TestBookingController(unittest.TestCase):
    __resourceFound = '<Response streamed [200 OK]>'
    __resourceCreated = '<Response streamed [201 CREATED]>'
    __reportData = None

    def setUp(self):
        self.__reportData = {
            'id': 999,
            'carId': 1,
            'description': 'N/A',
            'open': 1
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

    def testGetReport(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/reports/1'), self.__resourceFound)

    def testGetReports(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/reports'), self.__resourceFound)

    def testCreateReport(self):
        self.assertEqual(self.__postRequest('http://localhost:5000/css/api/v1.0/reports', self.__reportData), self.__resourceCreated)

    def testUpdateReport(self):
        self.assertEqual(self.__putRequest('http://localhost:5000/css/api/v1.0/reports/1', {'open': '1'}), self.__resourceFound)

    def testDeleteReport(self):
        self.assertEqual(self.__deleteRequest('http://localhost:5000/css/api/v1.0/reports/999'), self.__resourceFound)

if __name__ == '__main__':
    unittest.main() 