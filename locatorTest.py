import unittest
from ap.locator import locator
from ap.carPool import carPool

class LocatorTest(unittest.TestCase):
    def setUp(self):
        self.__car = carPool.getCar(1)
        return super().setUp()

    def testGetCarLocation(self):
        self.assertIsNotNone(locator.getCarLocation(self.__car))

if __name__ == '__main__':
    unittest.main() 