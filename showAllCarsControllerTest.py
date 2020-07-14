import unittest
from mp.controller import ShowAllCarsController

class ShowAllCarsControllerTest(unittest.TestCase):
    __showAllCarsController = ShowAllCarsController()

    def testShowAllAvailableCars(self):
        cars = self.__showAllCarsController.showAllAvailableCars()

        return self.assertIsNotNone(cars['cars'])

    def testGetBookingsData(self):
        bookings = self.__showAllCarsController.getBookingsData()

        return self.assertIsNotNone(bookings['bookings'])

if __name__ == '__main__':
    unittest.main()