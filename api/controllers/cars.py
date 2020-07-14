from api import db
from models import Car
from flask import jsonify

# performs request response for routes pertaining to the Car resource
class CarController:
    def getCar(self, id):
        # locate a car in the database
        carTuple = db.getObjectById('cars', id)[0]
        # use data to create a car object then jsonify it's dict
        return jsonify(Car(carTuple[0], carTuple[1], carTuple[2], carTuple[3], carTuple[4], carTuple[5], carTuple[6],
            carTuple[7], carTuple[8]).asDict())

    def getCars(self, params=None):
        cars = []
        # with no optional params all cars can be fetched 
        if not params:
            carTuples = db.getAllObjects('cars')
        # otherwise only cars matching the params will be fetched
        else:
            for param in params:
                if param not in Car.attributesAsList():
                    return jsonify({'cars': []})
            # get all cars that match the filter
            carTuples = db.getObjectsByFilter('cars', list(params.keys()), list(params.values()))

        # contsruct the fetched cars as objects
        for i in range(len(carTuples)):
            cars.append(Car(carTuples[i][0], carTuples[i][1], carTuples[i][2], carTuples[i][3], carTuples[i][4], carTuples[i][5], 
            carTuples[i][6], carTuples[i][7], carTuples[i][8]))

        # jsonify each car object's dict
        return jsonify(cars=[car.asDict() for car in cars])

    def createCar(self, params):
        # construct a car object from the gathered data
        car = Car(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8])
        # update the database with the new car and respond with a confirmation of insertion
        db.insertObject('cars', Car.attributesAsList(), car.asTuple())
        return jsonify({'car': car.asDict()}), 201

    def updateCar(self, id, fieldsToUpdate, params):
        # update the car with the specified id, indicating which fields to update and what to update them to
        db.updateObject('cars', id, fieldsToUpdate, params)
        # retrieve the newly updated car and create an object from it's data
        carTuple = db.getObjectById('cars', id)[0]
        car = Car(carTuple[0], carTuple[1], carTuple[2], carTuple[3], carTuple[4], carTuple[5], carTuple[6], carTuple[7], carTuple[8])
        # jsonify the car to confirm the update
        return jsonify({'car': car.asDict()})

    def deleteCar(self, id):
        db.deleteObject('cars', id)
        return jsonify({'result': True})

# create a single instance of a CarController to be exported
carsController = CarController()