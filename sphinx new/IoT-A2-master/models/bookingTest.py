import unittest
from .model import Model

class BookingModelTest(unittest.TestCase):

    __Model = Model()

    def testattributesAsList(self):
        self.assertTrue(self.__Model.attributesAsList('456', 'Green3#H','456', 'Green3#H','456', 'True))

if __name__ == '__main__':
    unittest.main()
