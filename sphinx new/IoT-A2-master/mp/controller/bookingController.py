from mp.controller import ApiController
from mp.controller.googleController import googleController
import datetime
class BookingController:

	def __init__(self, user):
		self.__apiController = ApiController()
		self.__urlCar = "http://localhost:5000/css/api/v1.0/cars"
		self.__urlBook = "http://localhost:5000/css/api/v1.0/bookings"
		self.__user = user
		self.__jsonDataCar = self.__apiController.requestGet(self.__urlCar)
		self.__jsonDataBook = self.__apiController.requestGet(self.__urlBook)
		
	def book(self, car, user, startMonth, startDay, endMonth, endDay):
		self.__user = user
		for x in self.__jsonDataCar["cars"]:
			if str(car).lower() == str(x["make"]).lower():
				print("Car found.")
				print("Car make: ",x["make"])
				print("Body type: ",x["bodyType"])
				print("Cost per hour: ",x["costPerHour"])
				print("-------------------")
				bookingId = len(self.__jsonDataBook["bookings"]) + 1
				
				startTime = datetime.datetime(2020, int(startMonth), int(startDay)).isoformat()
				endTime = datetime.datetime(2020, int(endMonth), int(endDay)).isoformat()
				carId = x["id"]
				userId = user.getId()
				dataBook = {"id" : bookingId, "startTime" : startTime, "endTime": endTime, "car_id" : carId, \
				"user_id" : userId, "active" : 1}
				if not self.__isCarAvailable(dataBook, carId):
					print('Sorry, this car has already been booked for these times.')
					return False
				self.__apiController.requestPost(self.__urlBook, dataBook)
				print("Booking complete. You have booked: ", x["make"])
				print("Your booking id is: ", bookingId)
				print('Adding booking to your Google calendar')
				googleController.addBookingToCalendar('{} {} Booking'.format(x["make"], x['bodyType']), '{}:{}'.format(x['location']['x'], \
					x['location']['y']), 'Booking', dataBook['startTime'], dataBook['endTime'])
				return True
		print("No such car found.")
		return False

	def cancelBooking(self):
		print("Enter booking id or car name: ")
		choice = input()
		try:
			int(choice)
			for x in self.__jsonDataBook["bookings"]:
				if x['active'] == 0 and x['id'] == choice:
					print('This booking cannot be cancelled, it has already expired or been cancelled.')
					return False
				if x["id"] == int(choice) and x["user"]["id"] == self.__user.getId():
					print("Booking found.")
					print("Cancelling booking...")
					urlUpdate = "http://localhost:5000/css/api/v1.0/bookings/{}".format(str(choice))
					self.__apiController.requestPut(urlUpdate, {'active': 0})
					#update booking active to 0
					print("Booking cancelled successfully.")
					return True
			print("No such booking found.")
			return False
		except ValueError:
			for x in self.__jsonDataCar["cars"]:
				if str(choice.lower()) in str(x["make"].lower()):
					for j in self.__jsonDataBook["bookings"]:
						if x["id"] == j["car"]["id"] and j["user"]["id"] == self.__user.getId() \
						and j["active"] == 1:
							print("Booking found.")
							print("Cancelling booking...")
							#update j active

							urlUpdate = "http://localhost:5000/css/api/v1.0/bookings/{}".format(str(j["id"]))
							self.__apiController.requestPut(urlUpdate, {'active': 0})

							print("Booking cancelled successfully.")
							return True

			print("No such booking found.")
			return False

	def showBookingsHistory(self):
		print("All past bookings: ")
		
		historyCount = 0

		for x in self.__jsonDataBook["bookings"]:
			if self.__user.getId() == x["user"]["id"] and x["active"] == 0:
				historyCount += 1
				
				print("Booking id: ", x["id"])
				print("Car: ", x["car"]["make"])
				print("Start Time: ", x["startTime"])
				print('End Time: ', x['endTime'])
				print(x['active'])
				print("--------------------")
		
		if historyCount <= 0:
			print('You have no booking history!')

	def showCurrentBookings(self):
		print("Your current bookings: ")
		bookingCount = 0
		for x in self.__jsonDataBook["bookings"]:
			if self.__user.getId() == x["user"]["id"] and x["active"] == 1:
				bookingCount += 1
				print("Booking id: ", x["id"])
				print("Car: ", x["car"]["make"])
				print("Start Time: ", x["startTime"])
				print('End Time: ', x['endTime'])
				print("--------------------")
		
		if bookingCount <= 0:
			print('You have no upcoming bookings!')

	def updateBookingsStatus(self):
		# go through all currently active bookings for logged in user to see if they have expired
		allBookings = self.__apiController.requestGet('{}?user_id={}&active={}'.format(self.__urlBook, 
			self.__user.getId(), 1))['bookings']

		for booking in allBookings:
			format =  '%a, %d %b %Y %H:%M:%S %Z'
			endTime = datetime.datetime.strptime(booking['endTime'], format).isoformat()
			currentTime = datetime.datetime.now().isoformat()
			if self.__hasBookingExpired(endTime, currentTime):
				urlUpdate = "http://localhost:5000/css/api/v1.0/bookings/{}".format(str(booking['id']))
				self.__apiController.requestPut(urlUpdate, {'active': 0})


	def __isCarAvailable(self, bookingDict, desiredCarId):
		startTime = bookingDict['startTime']
		endTime = bookingDict['endTime']
		format = '%a, %d %b %Y %H:%M:%S %Z'

		matchingBookings = self.__apiController.requestGet('{}?car_id={}'.format(self.__urlBook, desiredCarId))['bookings']

		for booking in matchingBookings:
			if self.__doTimesClash(startTime, datetime.datetime.strptime(booking['startTime'], format).isoformat(), 
				endTime, datetime.datetime.strptime(booking['endTime'], format).isoformat()):
				return False

		return True

	def __doTimesClash(self, startTime, otherStartTime, endTime, otherEndTime):
		if startTime >= otherStartTime and startTime <= otherEndTime:
			return True

		if endTime <= otherEndTime and endTime >= otherStartTime:
			return True

		if startTime <= otherStartTime and endTime >= otherEndTime:
			return True

		return False
	
	def __hasBookingExpired(self, bookingTime, currentTime):
		return bookingTime < currentTime