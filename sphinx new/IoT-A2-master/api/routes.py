from api import app
from api.controllers import bookingsController, carsController, reportsController, usersController
from models import Booking, Car, Report, User

from flask import make_response, jsonify, request, abort

# helper functions
def generateURI(resource=None, id=False):
    # the various interchangeable elements that compose each API url
    urlComponents = {
        'root' : '/css/api/v1.0',
        'cars' : '/cars',
        'users' : '/users',
        'bookings' : '/bookings',
        'reports': '/reports',
        'id' : '/<int:id>'
    }

    # all urls must start with a root
    url = urlComponents['root']

    # a resource allows you to perform requests for that resource
    if resource:
        url += urlComponents[resource]

    # an id is necessary when updating, deleting or viewing a single resource
    if id:
        url += urlComponents['id']

    return url

# helper method to parse the body params during a resource creation request
def parseParams(expectedParamList):
    params = []
    if not request:
        return None

    # ensure there are no invalid parameters
    for param in request.form:
        if param not in expectedParamList:
            return None

    # if a param that is expected is not present in the request then it will fail
    for param in expectedParamList:
        if not request.form[param]:
            return None
        # progressively build the data needed for resource creation
        params.append(request.form[param])

    return params
# helper method to parse the body params during a resource update request
def parseOptionalParams(potentialParamList):
    fieldsToUpdate = []
    params = []

    # if a param that is allowed is in the request then it will marked as a field to update for the request
    for param in potentialParamList:
        if request.form.get(param):
            fieldsToUpdate.append(param)
            params.append(request.form[param])

    # return which fields should be changed and the new values for said fields
    return fieldsToUpdate, params

# general routes
@app.route(generateURI(), methods=['GET'])
def index():
    return 'This is the home page for the CSS API.'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# api calls regarding the car object
carParams = Car.attributesAsList()
@app.route(generateURI('cars', True), methods=['GET'])
def getCar(id):
    return carsController.getCar(id)

@app.route(generateURI('cars'), methods=['GET'])
def getCars():
    # if this request contains parameters call a modified get all function
    if request.args:
        return carsController.getCars(request.args)
    return carsController.getCars()

@app.route(generateURI('cars'), methods=['POST'])
def createCar():
    params = parseParams(carParams)
    # if the request has no body data, then it is invalid
    if not request.form:
        abort(400)
    return carsController.createCar(params)

@app.route(generateURI('cars', True), methods=['PUT'])
def updateCar(id):
    fieldsToUpdate, params = parseOptionalParams(carParams[1:])
    return carsController.updateCar(id, fieldsToUpdate, params)

@app.route(generateURI('cars', True), methods=['DELETE'])
def deleteCar(id):
    return carsController.deleteCar(id)

# api calls regarding the user object
userParams = User.attributesAsList()
@app.route(generateURI('users', True), methods=['GET'])
def getUser(id):
    return usersController.getUser(id)

@app.route(generateURI('users'), methods=['GET'])
def getUsers():
    if request.args:
        return usersController.getUsers(request.args)
    return usersController.getUsers()

@app.route(generateURI('users'), methods=['POST'])
def createUser():
    params = parseParams(userParams)
    # if the request has no body data, then it is invalid
    if params == None:
        abort(400)
    return usersController.createUser(params)

@app.route(generateURI('users', True), methods=['PUT'])
def updateUser(id):
    fieldsToUpdate, params = parseOptionalParams(userParams[1:])
    return usersController.updateUser(id, fieldsToUpdate, params)

@app.route(generateURI('users', True), methods=['DELETE'])
def deleteUser(id):
    return usersController.deleteUser(id)

# api calls regarding the booking object
bookingParams = Booking.attributesAsList()
@app.route(generateURI('bookings', True), methods=['GET'])
def getBooking(id):
    return bookingsController.getBooking(id)

@app.route(generateURI('bookings'), methods=['GET'])
def getBookings():
    # if the request is filtering by user_id call a modified version of the get all function
    if request.args:
        return bookingsController.getBookings(request.args)
    return bookingsController.getBookings()

@app.route(generateURI('bookings'), methods=['POST'])
def createBooking():
    params = parseParams(bookingParams)
    # if the request has no body data, then it is invalid
    if params == None:
        abort(400)
    return bookingsController.createBooking(params)

@app.route(generateURI('bookings', True), methods=['PUT'])
def updateBooking(id):
    fieldsToUpdate, params = parseOptionalParams(bookingParams[1:])
    return bookingsController.updateBooking(id, fieldsToUpdate, params)

@app.route(generateURI('bookings', True), methods=['DELETE'])
def deleteBooking(id):
    return bookingsController.deleteBooking(id)

reportParams = Report.attributesAsList()
@app.route(generateURI('reports', True), methods=['GET'])
def getReport(id):
    return reportsController.getReport(id)

@app.route(generateURI('reports'), methods=['GET'])
def getReports():
    if request.args:
        return reportsController.getReports(request.args)
    return reportsController.getReports()

@app.route(generateURI('reports'), methods=['POST'])
def createReport():
    params = parseParams(reportParams)
    return reportsController.createReport(params)

@app.route(generateURI('reports', True), methods=['PUT'])
def updateReport(id):
    fieldsToUpdate, params = parseOptionalParams(reportParams[1:])
    return reportsController.updateReport(id, fieldsToUpdate, params)

@app.route(generateURI('reports', True), methods=['DELETE'])
def deleteReport(id):
    return reportsController.deleteReport(id)