from flask import redirect, render_template, request, url_for
from mp.controller import ApiController, BookingController, googleController, LoginController, EncryptPassword, \
    RegistrationController, VerificationController
from mp.forms import BookingForm, LoginForm, RegisterForm, SearchForm, UserForm, CarForm, ReportForm
from datetime import date
from datetime import timedelta
from models import Car, User
from mp.VoiceSearch import VoiceSearch
import time

class Middleware:
    def __init__(self):
        self.__apiController = ApiController()
        self.__loginController = LoginController()
        self.__registerController = RegistrationController()
        self.__encryptPassword = EncryptPassword()
        self.__verificationController = VerificationController()
        self.__voiceSearch = VoiceSearch()

    def index(self):
        if not self.__isUserLoggedIn():
            return render_template('index.html')
        userType = self.__getUserType()
        users = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users')['users']
        cars = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')['cars']
        bookings = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings')['bookings']
        if userType == 'customer':
            return render_template('customerDashboard.html')
        elif userType == 'engineer':
            return render_template('engineerDashboard.html')
        elif userType == 'manager':
            carIds, rentalAmounts = self.getMostPopularCars(10, bookings, cars)
            months, bookingCounts = self.getBookingsPerMonth(bookings)
            userTypes, userCounts = self.getUserTypeCount(users)
            return render_template('managerDashboard.html', carIds=carIds, rentalAmounts=rentalAmounts, months=months, \
                bookingCounts=bookingCounts, userTypes=userTypes, userCounts=userCounts)
        elif userType == 'admin':
            return render_template('adminDashboard.html', users=users, cars=cars)
        else:
            return render_template('index.html')

    def login(self):
        form = LoginForm()
        if request.method == 'POST':
            email = request.form['email']
            password = self.__encryptPassword.hash(request.form['password'])
            user = self.__loginController.login(email, password)
            if user:
                googleController.authenticateGoogleUser()
                googleController.fetchCalendar()
                bookingController = BookingController(user)
                bookingController.updateBookingsStatus()
                return redirect(url_for('index'))
            return redirect(url_for('login'))
        return render_template('login.html', form=form)

    def logout(self):
        if self.__isUserLoggedIn():
            self.__loginController.logout()
        return redirect(url_for('index'))

    def register(self):
        form = RegisterForm()
        if request.method == 'POST':
            formData = request.form
            if not self.__validateRegister(formData['username'], formData['password'], formData['firstName'], formData['lastName'], formData['email']):
                return redirect(url_for('register'))
            username = formData['username']
            password = self.__encryptPassword.hash(formData['password'])
            firstName = formData['firstName']
            lastName = formData['lastName']
            email = formData['email']
            user = self.__registerController.register(username, password, firstName, lastName, email, 'None')
            if user:
                self.__loginController.setLoggedInUser(user)
                return redirect(url_for('index'))
            return redirect(url_for('register'))
        return render_template('register.html', form=form)
    
    def __validateRegister(self, username, password, firstName, lastName, email):
        ver = self.__verificationController
        return ver.verifyUsername(username) and ver.verifyPassword(password) and ver.verifyFirstName(firstName) and \
               ver.verifyLastName(lastName) and ver.verifyEmail(email)

    def getUser(self, id):
        user = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/{}'.format(id))
        return render_template('user.html', user=user)

    # only accepted by post requests
    def getUsers(self):
        formData = request.form
        searchQuery = formData['query']
        users = self.__getMatchingUsers(searchQuery)
        return render_template('users.html', users=users, searchQuery=searchQuery)

    def newUser(self):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin():
            return redirect(url_for('index'))
        form = UserForm()
        if request.method == 'POST':  
            formData = request.form 
            userId = self.__getNextUserId()
            username = formData['username']
            password = self.__encryptPassword.hash(formData['password'])
            firstName = formData['firstName']
            lastName = formData['lastName']
            email = formData['email']
            userType = formData['userType']
            userData = {
                'id': userId,
                'username': username,
                'password': password,
                'firstName': firstName,
                'lastName': lastName,
                'email': email,
                'faceId': 'None',
                'type': userType
            }
            self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/users', userData)
            return redirect(url_for('index'))
        return render_template('newUser.html', form=form)  

    def updateUser(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin() and not self.__getLoggedInUser().getId() == id:
            return redirect(url_for('index'))
        user = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/{}'.format(id))
        form = UserForm(userType=user['type'])
        if request.method == 'POST':
            formData = request.form 
            username = formData['username']
            firstName = formData['firstName']
            lastName = formData['lastName']
            email = formData['email']
            userType = formData['userType']
            userData = {
                'username': username,
                'firstName': firstName,
                'lastName': lastName,
                'email': email,
                'type': userType
            }
            self.__apiController.requestPut('http://localhost:5000/css/api/v1.0/users/{}'.format(id), userData)
            return redirect(url_for('index'))
        return render_template('updateUser.html', form=form, user=user)

    def deleteUser(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin() and not self.__getLoggedInUser().getId() == id:
            return redirect(url_for('index'))
        self.__apiController.requestDelete('http://localhost:5000/css/api/v1.0/users/{}'.format(id))
        return redirect(url_for('index'))


    def voiceSearch(self):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin() and not self.__getLoggedInUser().getId() == id:
            return redirect(url_for('index'))
        carSearched = self.__voiceSearch.voiceSearch()
        #time.sleep(10)
        
        
        if request.method == 'POST':
            
            cars = self.__getMatchingCars(carSearched)
            redirect(url_for('cars'))
        return render_template('voice.html', cars=cars)


    def getCar(self, id):
        car = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars/{}'.format(id))
        return render_template('car.html', car=car)

    def getAllCars(self):
        cars = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')['cars']
        form = SearchForm()
        if request.method == 'POST':
            query = request.form['query']
            cars = self.__getMatchingCars(query)
        return render_template('cars.html', cars=cars, form=form)
        
    def newCar(self):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin():
            return redirect(url_for('index'))
        form = CarForm()
        if request.method == 'POST':
            formData = request.form
            carId = self.__getNextCarId()
            make = formData['make']
            bodyType = formData['bodyType']
            colour = formData['colour']
            seats = formData['seats']
            xCoordinate = formData['xCoordinate']
            yCoordinate = formData['yCoordinate']
            costPerHour = formData['costPerHour']
            carData = {
                'id': carId, 
                'make': make, 
                'bodyType': bodyType, 
                'colour': colour, 
                'seats': seats, 
                'xCoordinate': xCoordinate, 
                'yCoordinate': yCoordinate, 
                'costPerHour': costPerHour, 
                'isLocked': 1
            }
            self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/cars', carData)
            return redirect(url_for('index'))
        return render_template('newCar.html', form=form)

    def updateCar(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin():
            return redirect(url_for('index'))
        form = CarForm()
        car = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars/{}'.format(id))
        if request.method == 'POST':
            formData = request.form
            make = formData['make']
            bodyType = formData['bodyType']
            colour = formData['colour']
            seats = formData['seats']
            xCoordinate = formData['xCoordinate']
            yCoordinate = formData['yCoordinate']
            costPerHour = formData['costPerHour']
            carData = {
                'make': make, 
                'bodyType': bodyType, 
                'colour': colour, 
                'seats': seats, 
                'xCoordinate': xCoordinate, 
                'yCoordinate': yCoordinate, 
                'costPerHour': costPerHour
            }
            self.__apiController.requestPut('http://localhost:5000/css/api/v1.0/cars/{}'.format(id), carData)
            return redirect(url_for('index'))
        return render_template('updateCar.html', form=form, car=car)

    def deleteCar(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin():
            return redirect(url_for('index'))
        self.__apiController.requestDelete('http://localhost:5000/css/api/v1.0/cars/{}'.format(id))
        return redirect(url_for('index'))

    def bookCar(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for(request.referrer))
        form = BookingForm()
        if request.method == 'POST':
            userId = self.__getLoggedInUser().getId()
            carId = request.form['carId']
            startMonth = request.form['startMonth']
            startDay = request.form['startDay']
            endMonth = request.form['endMonth']
            endDay = request.form['endDay']
            userDict = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/{}'.format(userId))
            user = User(userDict['id'], userDict['username'], userDict['password'], userDict['firstName'], 
                userDict['lastName'], userDict['email'], userDict['faceId'])
            carDict = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars/{}'.format(carId))
            bookingController = BookingController(user)
            bookingController.book(carDict['make'], user, startMonth, startDay, endMonth, endDay)
            return redirect(url_for('index'))
        return render_template('carBooking.html', carId=id, userId=self.__getLoggedInUser().getId(), form=form)
    
    def reportCar(self, id):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if not self.isAdmin():
            return redirect(url_for('index'))
        form = ReportForm()
        if request.method == 'POST':
            formData = request.form
            reportId = self.__getNextReportId()
            carId = id
            description = formData['description'] if formData['description'] is not '' else 'N/A'
            reportData = {
                'id': reportId,
                'carId': carId,
                'description': description,
                'open': 1
            }
            self.__apiController.requestPost('http://localhost:5000/css/api/v1.0/reports', reportData)
            return redirect(url_for('index'))
        return render_template('carReport.html', cardId=id, form=form)

    def getAllBookings(self):
        bookings = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings')['bookings']
        return render_template('bookings.html', bookings=bookings)

    def getBooking(self, id):
        booking = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings/{}'.format(id))
        return render_template('booking.html', booking=booking)

    def getBookingHistory(self):
        if not self.__isUserLoggedIn():
            return redirect(url_for('index'))
        if self.isAdmin():
            bookingHistory = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings?active=0')['bookings']
        else:
            userId = self.__getLoggedInUser().getId()
            bookingHistory = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings?user_id={}&active=0'.format(userId))['bookings']
            
        return render_template('bookingHistory.html', bookings=bookingHistory)

    def cancelBooking(self, id):
        urlUpdate = "http://localhost:5000/css/api/v1.0/bookings/{}".format(str(id))
        self.__apiController.requestPut(urlUpdate, {'active': 0})
        return redirect(url_for('index'))

    def carById(self, id):
        return self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars/{}'.format(id))

    def usernameById(self, id):
        return self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users/{}'.format(id))['username']

    def loggedInUser(self):
        return self.__loginController.getLoggedInUser()
    
    def isAdmin(self):
        return self.__loginController.getLoggedInUserType() == 'admin'

    def isManager(self):
        return self.__loginController.getLoggedInUserType() == 'manager'

    def isEngineer(self):
        return self.__loginController.getLoggedInUserType() == 'engineer'

    def isCustomer(self):
        return self.__loginController.getLoggedInUserType() == 'customer'

    def getMostPopularCars(self, number, bookings, cars):
        carPopularity = {}

        for car in cars:
            carPopularity.update({'Car {}'.format(car['id']): 0})

        for booking in bookings:
            carId = booking['car']['id']
            oldValue = carPopularity['Car {}'.format(carId)]
            carPopularity.update({'Car {}'.format(carId): oldValue + 1})

        return list(carPopularity.keys()), list(carPopularity.values())

    def getBookingsPerMonth(self, bookings):
        months = {
            'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
            'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0
        }

        for booking in bookings:
            for month in months.keys():
                if month in booking['startTime']:
                    previousValue = months[month]
                    months.update({month: previousValue + 1})
        
        return list(months.keys()), list(months.values())

    def getUserTypeCount(self, users):
        userTypes = {
            'admin': 0, 'manager': 0, 'engineer': 0, 'customer': 0
        }

        for user in users:
            for userType in userTypes.keys():
                if userType == user['type']:
                    previousValue = userTypes[userType]
                    userTypes.update({userType: previousValue + 1})
        
        return list(userTypes.keys()), list(userTypes.values())

    def __getUserType(self):
        return self.__loginController.getLoggedInUserType()

    def __isUserLoggedIn(self):
        return self.__loginController.getLoggedInUser() is not None

    def __getLoggedInUser(self):
        return self.__loginController.getLoggedInUser()

    def __getNextBookingId(self):
        allBookings = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/bookings')['bookings']

        currentIds = []

        for booking in allBookings:
            currentIds.append(int(booking['id']))

        currentIds.sort()

        for i in range(len(currentIds)):
            if currentIds[i] != i + 1:
                return i + 1

        return len(allBookings) + 1

    def __getNextUserId(self):
        allUsers = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users')['users']

        currentIds = []

        for user in allUsers:
            currentIds.append(int(user['id']))

        currentIds.sort()

        for i in range(len(currentIds)):
            if currentIds[i] != i + 1:
                return i + 1

        return len(allUsers) + 1

    def __getNextCarId(self):
        allCars = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars')['cars']

        currentIds = []

        for car in allCars:
            currentIds.append(int(car['id']))

        currentIds.sort()

        for i in range(len(currentIds)):
            if currentIds[i] != i + 1:
                return i + 1

        return len(allCars) + 1

    def __getNextReportId(self):
        allReports = self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/reports')['reports']

        currentIds = []

        for report in allReports:
            currentIds.append(int(report['id']))

        currentIds.sort()

        for i in range(len(currentIds)):
            if currentIds[i] != i + 1:
                return i + 1

        return len(allReports) + 1

    def __getUsersByFilterParam(self, filterParam, paramValue):
        return self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/users?{}={}'.format(filterParam, paramValue))['users']

    def __getMatchingUsers(self, searchQuery):
        matchingUsers = []

        for i in range(len(User.attributesAsList()) - 2):
            currentFiltered = self.__getUsersByFilterParam(User.attributesAsList()[i], searchQuery)
            for item in currentFiltered:
                if item not in matchingUsers:
                    matchingUsers.append(item)

        return matchingUsers

    def __getCarsByFilterParam(self, filterParam, paramValue):
        return self.__apiController.requestGet('http://localhost:5000/css/api/v1.0/cars?{}={}'.format(filterParam, paramValue))['cars']

    def __getMatchingCars(self, searchQuery):
        matchingCars = []

        for i in range(len(Car.attributesAsList()) - 1):
            matchingCars.extend(self.__getCarsByFilterParam(Car.attributesAsList()[i], searchQuery))
        
        return matchingCars


middleware = Middleware()