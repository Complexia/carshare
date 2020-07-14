import unittest
from api import app
import datetime

class TestBookingController(unittest.TestCase):
    __resourceFound = '<Response streamed [200 OK]>'
    __resourceCreated = '<Response streamed [201 CREATED]>'
    __bookingData = None

    def setUp(self):
        self.__bookingData = {
            'id': 999,
            'startTime': datetime.datetime(2020, int(11), int(4)).isoformat(),
			'endTime': datetime.datetime(2020, int(11), int(6)).isoformat(),
            'user_id': 1,
            'car_id': 1,
            'active': 1
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

    def testGetBooking(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/bookings/1'), self.__resourceFound)

    def testGetBookings(self):
        self.assertEqual(self.__getRequest('http://localhost:5000/css/api/v1.0/bookings'), self.__resourceFound)

    def testCreateBooking(self):
        self.assertEqual(self.__postRequest('http://localhost:5000/css/api/v1.0/bookings', self.__bookingData), self.__resourceCreated)

    def testUpdateBooking(self):
        self.assertEqual(self.__putRequest('http://localhost:5000/css/api/v1.0/bookings/1', {'active': '0'}), self.__resourceFound)

    def testDeleteBooking(self):
        self.assertEqual(self.__deleteRequest('http://localhost:5000/css/api/v1.0/bookings/999'), self.__resourceFound)

if __name__ == '__main__':
    unittest.main() 