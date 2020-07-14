import unittest
from ap.carPool import carPool
from mp.controller import ApiController
from models import Car, Customer

class CarPoolTest(unittest.TestCase):
    __apiController = ApiController()
    __expectedCar = Car(1, 'Holden Commodore', 'SUV', 'Red', 4, 35.0, 21.0, 13.0, 0)

    def setUp(self):
        userId = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings/3')['user']['id']
        userDict = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/{}'.format(userId))
        self.__user = Customer(userId, userDict['username'], userDict['password'], userDict['firstName'], userDict['lastName'], userDict['email'], userDict['faceId'])
        return super().setUp()

    def testGetCar(self):
        self.assertEqual(carPool.getCar(1).asDict(), self.__expectedCar.asDict())
    
    def testLockCar(self):
        self.assertFalse(carPool.lockCar(self.__user))

    def testUnlockCar(self):
        self.assertFalse(carPool.unlockCar(self.__user))

if __name__ == '__main__':
    unittest.main() 