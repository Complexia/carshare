from api import db
from flask import jsonify
from models import Booking, Car, User

# performs request response for routes pertaining to the Booking resource
class BookingController:
    # booking controller must be able to obtain users to construct a booking object
    def __getUser(self, id):
        userTuple = db.getObjectById('users', id)[0]
        if not userTuple:
            return None
        return User(userTuple[0], userTuple[1], userTuple[2], userTuple[3], userTuple[4], userTuple[5], userTuple[6])

    # booking controller must be able to obtain cars to construct a booking object
    def __getCar(self, id):
        carTuple = db.getObjectById('cars', id)[0]
        if not carTuple:
            return None
        return Car(carTuple[0], carTuple[1], carTuple[2], carTuple[3], carTuple[4], carTuple[5], carTuple[6], carTuple[7], carTuple[8])

    def getBooking(self, id):
        # locate a booking in the database
        bookingTuple = db.getObjectById('bookings', id)[0]
        # use data to create a booking object then jsonify it's dict
        return jsonify(Booking(bookingTuple[0], bookingTuple[1], bookingTuple[2], self.__getUser(bookingTuple[3]), 
            self.__getCar(bookingTuple[4]), bookingTuple[5]).asDict())

    def getBookings(self, params=None):
        bookings = []
        # with no optional params all bookings can be fetched
        if not params:
            bookingTuples = db.getAllObjects('bookings')
        # otherwise only bookings matching the params may be fetched
        else:
            for param in params:
                if param not in Booking.attributesAsList():
                    return jsonify({'bookings': []})
            # obtain booking history for user_id param
                bookingTuples = db.getObjectsByFilter('bookings', list(params.keys()), list(params.values()))

        # construct the fetched bookings as objects
        for i in range(len(bookingTuples)):
            bookings.append(Booking(bookingTuples[i][0], bookingTuples[i][1], bookingTuples[i][2], self.__getUser(bookingTuples[i][3]), 
                self.__getCar(bookingTuples[i][4]), bookingTuples[i][5]))

        # jsonify each booking object's dict
        return jsonify(bookings=[booking.asDict() for booking in bookings])

    def createBooking(self, params):
        # fetch the user and car corresponding to the user_id and car_id in the request body
        user = self.__getUser(params[3])
        car = self.__getCar(params[4])
        # construct a booking object from the gathered data
        booking = Booking(params[0], params[1], params[2], user, car, params[5])
        # update the database with the new booking and respond with a confirmation of insertion
        db.insertObject('bookings', Booking.attributesAsList(), booking.asTuple())
        return jsonify({'booking': booking.asDict()}), 201

    def updateBooking(self, id, fieldsToUpdate, params):
        # update the booking with the specified id, indicating which fields to update and what to update them to
        db.updateObject('bookings', id, fieldsToUpdate, params)
        # retrieve the newly updated booking and create an object from it's data
        bookingTuple = db.getObjectById('bookings', id)[0]
        booking = Booking(bookingTuple[0], bookingTuple[1], bookingTuple[2], self.__getUser(bookingTuple[3]), 
            self.__getCar(bookingTuple[4]), bookingTuple[5])
        # jsonify the booking to confirm the update
        return jsonify({'booking': booking.asDict()})

    def deleteBooking(self, id):
        db.deleteObject('bookings', id)
        return jsonify({'result': True})

# create a single instance of a BookingController to be exported
bookingsController = BookingController()