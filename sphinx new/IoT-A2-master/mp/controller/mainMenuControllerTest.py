import unittest

from mainMenuController import MainMenuController

class mainMenuControllerTest(unittest.TestCase):

    __MainMenuController = MainMenuController()

    def testselect(self):
        self.assertFalse(self.__MainMenuController.select('1'))

if __name__ == '__main__':
    unittest.main()
