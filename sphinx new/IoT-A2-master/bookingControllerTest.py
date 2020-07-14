import unittest
from mp.controller import ApiController, BookingController
from mp.controller.googleController import googleController
from models import User
import json, requests
import datetime

class BookingControllerTest(unittest.TestCase):

    __bookingController = None
    __apiController = ApiController()

    def setUp(self):
        googleController.authenticateGoogleUser()
        googleController.fetchCalendar()
        uDict = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/1')
        self.__user = User(uDict['id'], uDict['username'], uDict['password'], uDict['firstName'], uDict['lastName'], uDict['email'], uDict['faceId'])
        self.__bookingController = BookingController(self.__user)
        return super().setUp()

    def testbook(self):
        self.assertTrue(self.__bookingController.book('Holden', self.__user, 12, 1, 12, 7))

    def tearDown(self):
        bookingId = len(self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings')['bookings'])
        requests.delete('http://localhost:5000/css/api/v1.0/bookings/{}'.format(bookingId))
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
