import unittest
from mp.plots import plots

class PlotsTest(unittest.TestCase):
    def testBookingsPerCar(self):
        self.assertIsNotNone(plots.bookingsPerCar('[toyota]', '[3]'))

    def testBookingsPerMonth(self):
        self.assertIsNotNone(plots.bookingsPerMonth('[January]', '[2]'))

    def testUserBasePercentages(self):
        self.assertIsNotNone(plots.userBasePercentages('[user]', '[2]'))

   
if __name__ == '__main__':
    unittest.main() 