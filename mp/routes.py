from flask import redirect, render_template, request, Response
from mp.middleware import middleware
from mp.webApp import app
from mp.plots import plots
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

@app.context_processor
def injectLoggedInUser():
    return dict(loggedInUser=middleware.loggedInUser())

@app.context_processor
def injectIsAdmin():
    return dict(isAdmin=middleware.isAdmin())

@app.context_processor
def injectUsernameById():
    def _injectUsernameById(id):
        return middleware.usernameById(id)
    return dict(usernameById=_injectUsernameById)

@app.context_processor
def injectCarById():
    def _injectCarById(id):
        return middleware.carById(id)
    return dict(carById=_injectCarById)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
def index():
    return middleware.index()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return middleware.login()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return middleware.register()

@app.route('/logout', methods=['GET'])
def logout():
    return middleware.logout()

@app.route('/users/<int:id>', methods=['GET'])
def user(id):
    return middleware.getUser(id)

@app.route('/users', methods=['POST'])
def users():
    return middleware.getUsers()

@app.route('/users/new', methods=['GET', 'POST'])
def newUser():
    return middleware.newUser()

@app.route('/users/<int:id>/update', methods=['GET', 'POST'])
def updateUser(id):
    return middleware.updateUser(id)

@app.route('/users/<int:id>/delete', methods=['GET'])
def deleteUser(id):
    return middleware.deleteUser(id)

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    return middleware.getAllCars()

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    return middleware.voiceSearch()

@app.route('/cars/<int:id>', methods=['GET'])
def car(id):
    return middleware.getCar(id)

@app.route('/cars/new', methods=['GET', 'POST'])
def newCar():
    return middleware.newCar()

@app.route('/cars/<int:id>/update', methods=['GET', 'POST'])
def updateCar(id):
    return middleware.updateCar(id)

@app.route('/cars/<int:id>/delete', methods=['GET'])
def deleteCar(id):
    return middleware.deleteCar(id)

@app.route('/cars/<int:id>/book', methods=['GET', 'POST'])
def bookCar(id):
    return middleware.bookCar(id)

@app.route('/cars/<int:id>/report', methods=['GET', 'POST'])
def reportCar(id):
    return middleware.reportCar(id)

@app.route('/cars/<int:id>/viewreports', methods=['GET', 'POST'])
def viewReportCar(id):
    return middleware.viewReportCar(id)

@app.route('/report/<int:id>', methods=['GET', 'POST'])
def viewReport(id):
    return middleware.viewReport(id)

@app.route('/report/<int:id>/location', methods=['GET', 'POST'])
def viewLocation(id):
    return middleware.viewLocation(id)

@app.route('/bookings', methods=['GET'])
def bookings():
    return middleware.getAllBookings()

@app.route('/bookings/history', methods=['GET'])
def bookingHistory():
    return middleware.getBookingHistory()

@app.route('/bookings/<int:id>', methods=['GET'])
def booking(id):
    return middleware.getBooking(id)

@app.route('/bookings/<int:id>/cancel', methods=['POST'])
def cancelBooking(id):
    return middleware.cancelBooking(id)

@app.route('/bar.png')
def plotBar():
    params = request.args
    return plots.bookingsPerCar(params['carIds'], params['rentalAmounts'])

@app.route('/line.png')
def plotLine():
    params = request.args
    return plots.bookingsPerMonth(params['months'], params['bookingCounts'])

@app.route('/pie.png')
def plotPie():
    params = request.args
    return plots.userBasePercentages(params['userTypes'], params['userCounts'])