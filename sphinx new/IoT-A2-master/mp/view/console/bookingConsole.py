class bookingConsole:

	def __init__(self, bookingController, user):
		self.__bookingController = bookingController
		self.__user = user
		self.__car = None

	def printBookingMenu(self):

		print("Booking menu: ")
		self.__car = input('Search for a car: ')
		self.book()

	def book(self):
		print('Please provide a starting date for your booking:')
		self.__startMonth = input('Enter a month: ')
		self.__startDay = input('Enter a day: ')
		print('Please provide an ending date for your booking:')
		self.__endMonth = input('Enter a month: ')
		self.__endDay = input('Enter a day: ')
		print("Attemping to book this car...")
		self.__bookingController.book(self.__car, self.__user, self.__startMonth, self.__startDay, self.__endMonth, self.__endMonth)

	def cancelBooking(self):
		self.__bookingController.cancelBooking()

	def showHistory(self):
		self.__bookingController.showBookingsHistory()

	def showCurrentBookings(self):
		self.__bookingController.showCurrentBookings()