class MainMenuController:

	def __init__(self):
		return None

	def select(self, option):

		#show booking history
		if int(option) == 1:
			
			self.__bookingConsole.showHistory()
		#show all available cars
		elif int(option) == 2:
			self.__showCarsConsole.showAllAvailableCars()
			
		#search a car
		elif int(option) == 3:
			self.__showCarsConsole.searchCar()

		#book a car
		elif int(option) == 4:
			self.__bookingConsole.printBookingMenu()

		#view current bookings
		elif int(option) == 5:
			self.__bookingConsole.showCurrentBookings()
		#cancel a booking
		elif int(option) == 6:
			self.__bookingConsole.cancelBooking()
		#logout
		elif int(option) == 7:
			return None
		#go back
		elif int(option) == 8:
			return None

		return self.__user
	def setShowCarsConsole(self,showCarsConsole):
		self.__showCarsConsole = showCarsConsole

	def setUser(self, user):
		self.__user = user

	def setBookingConsole(self, bookingConsole):
		self.__bookingConsole = bookingConsole
		
