import unittest
from mp.middleware import middleware
from mp import app
from mp.controller import ApiController

class MiddlewareTest(unittest.TestCase):
    __apiController = ApiController()
    __bookings = __apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings')['bookings']
    __cars = __apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')['cars']
    __users = __apiController.requestGet('http://localhost:5000/css/api/v1.0/users')['users']

    def testCarById(self):
        self.assertIsNotNone(middleware.carById(1))

    def testGetMostPopularCars(self): 
        result = middleware.getMostPopularCars(10, self.__bookings, self.__cars)
        self.assertEqual(len(result[0]), len(result[1]))

    def testGetBookingsPerMonth(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        result = middleware.getBookingsPerMonth(self.__bookings)
        validMonths = result[0] == months
        validBookings = len(result[1]) > 0
        self.assertTrue(validMonths and validBookings)

    def testGetUserTypeCount(self):
        userTypes = ['admin', 'manager', 'engineer', 'customer']
        result = middleware.getUserTypeCount(self.__users)
        validUserTypes = result[0] == userTypes
        validAmounts = len(result[1]) > 0
        self.assertTrue(validUserTypes and validAmounts)

if __name__ == '__main__':
    unittest.main() 