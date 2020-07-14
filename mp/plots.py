import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from io import BytesIO
import base64
from flask import Response
import re

class Plots:
    def __init__(self):
        rcParams.update({'figure.autolayout': True})

    # displays the number of unique users over a specified range
    def bookingsPerCar(self, carNames, totalBookings):
        cars, bookings = self.__convertListStrings(carNames, totalBookings)
        fig, ax = plt.subplots()
        ax.set_title('Most Popular Rental Cars', pad=20)
        ax.bar(cars, bookings)
        ax.tick_params(axis='x', rotation=70)
        ax.set_ylabel('Rental Count')

        return self.__renderGraph(fig)
    
    def bookingsPerMonth(self, months, bookings):
        allMonths, bookingValues = self.__convertListStrings(months, bookings)
        fig, ax = plt.subplots()
        ax.set_title('Number of Bookings by Month', pad=20)
        ax.plot(allMonths, bookingValues)
        ax.tick_params(axis='x', rotation=70)
        ax.set_ylabel('No. Bookings')

        return self.__renderGraph(fig)

    def userBasePercentages(self, userTypes, userCounts):
        types, userValues = self.__convertListStrings(userTypes, userCounts)
        fig, ax = plt.subplots()
        ax.set_title('Userbase Composition', pad=20)
        ax.pie(x=userValues, labels=types)

        return self.__renderGraph(fig)

    def __convertListStrings(self, labels, values):
        labels = re.sub('[\[\]\' ]', '', labels).split(',')
        valueStrings = re.sub('[\[\]\ ]', '', values).split(',')
        intValues = []

        for string in valueStrings:
            intValues.append(int(string))

        return labels, intValues

    def __renderGraph(self, fig):
        output = BytesIO()
        FigureCanvas(fig).print_png(output)

        return Response(output.getvalue(), mimetype='image/png')

plots = Plots()
        

        