import unittest
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from io import BytesIO
import base64
from flask import Response
import re
from plots import Plots

class PlotsTest(unittest.TestCase):

    _plots = Plots()

    def bookingsPerCar(self):
        self.assertEqual(self._plots.bookingsPerCar('toyota', 3))

    def userBasePercentages(self):
        self.assertIsNone(self._plots.userBasePercentages(6,2))

   
if __name__ == '__main__':
    unittest.main() 
