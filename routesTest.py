import unittest
from mp import app
from mp.controller import EncryptPassword

class RoutesTest(unittest.TestCase):
    __validTemplateResponse = '<Response streamed [200 OK]>'
    __validGetResponse = '<Response streamed [302 FOUND]>'
    __encryptor = EncryptPassword()

    def __getRequest(self, url):
        return str(app.test_client().get(url))

    def __postRequest(self, url, params):
        return str(app.test_client().post(url, data=params))

    def testGetIndex(self):
        self.assertEqual(self.__getRequest('/'), self.__validTemplateResponse)
    
    def testGetLogin(self):
        self.assertEqual(self.__getRequest('/login'), self.__validTemplateResponse)

    def testPostLogin(self):
        postRequest = self.__postRequest('/login', {'email': 'cherry@email.com', 'password': self.__encryptor.hash('Green3#H')})
        self.assertEqual(postRequest, self.__validGetResponse)

    def testGetRegister(self):
        self.assertEqual(self.__getRequest('/register'), self.__validTemplateResponse)

    def testGetLogout(self):
        self.assertEqual(self.__getRequest('/logout'), self.__validGetResponse)

    def testGetUser(self):
        self.assertEqual(self.__getRequest('/users/1'), self.__validTemplateResponse)

    def testGetNewUser(self):
        self.assertEqual(self.__getRequest('/users/new'), self.__validGetResponse)

    def testGetUpdateUser(self):
        self.assertEqual(self.__getRequest('/users/1/update'), self.__validGetResponse)

    def testGetDeleteUser(self):
        self.assertEqual(self.__getRequest('users/1/delete'), self.__validGetResponse)

    def testGetCars(self):
        self.assertEqual(self.__getRequest('/cars'), self.__validTemplateResponse)
    
    def testGetVoice(self):
        self.assertEqual(self.__getRequest('/voice'), self.__validGetResponse)

    def getCar(self):
        self.assertEqual(self.__getRequest('/cars/1'), self.__validTemplateResponse)

    def testGetNewCar(self):
        self.assertEqual(self.__getRequest('/cars/new'), self.__validGetResponse)

    def testGetUpdateCar(self):
        self.assertEqual(self.__getRequest('/cars/1/update'), self.__validGetResponse)

    def testGetDeleteCar(self):
        self.assertEqual(self.__getRequest('/cars/1/delete'), self.__validGetResponse)

    def testGetBookCar(self):
        self.assertEqual(self.__getRequest('/cars/1/book'), self.__validGetResponse)

    def testGetReportCar(self):
        self.assertEqual(self.__getRequest('/cars/1/report'), self.__validGetResponse)

    def testGetBookings(self):
        self.assertEqual(self.__getRequest('/bookings'), self.__validTemplateResponse)

    def testGetBookingHistory(self):
        self.assertEqual(self.__getRequest('/bookings/history'), self.__validGetResponse)

    def testGetBooking(self):
        self.assertEqual(self.__getRequest('/bookings/1'), self.__validTemplateResponse)

if __name__ == '__main__':
    unittest.main() 