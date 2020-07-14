from .apiController import ApiController
class ShowAllCarsController:

	def __init__(self):
		self.__apiController = ApiController()


	def showAllAvailableCars(self):
		url = "http://localhost:5000/css/api/v1.0/cars"
		jsonData = self.__apiController.requestGet(url)
		return jsonData

	def getBookingsData(self):
		url = "http://localhost:5000/css/api/v1.0/bookings"
		jsonData = self.__apiController.requestGet(url)
		return jsonData