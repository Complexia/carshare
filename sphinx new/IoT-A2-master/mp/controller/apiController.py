import requests, json
## this class provides functions which connect to the API
class ApiController:
	#perorm a get request on the database, getting the data as json
	def requestGet(self, requestUrl):
		response = requests.get(requestUrl)
		jsonData = json.loads(response.text)
		return jsonData

	#perform a post request on the database, inserting data
	def requestPost(self, requestUrl, data):
		response = requests.post(requestUrl, data=data)
		return response
	
	def requestPut(self, requestUrl, data):
		response = requests.put(requestUrl, data=data)
		return response

	def requestDelete(self, requestUrl):
		response = requests.delete(requestUrl)
		return response
	
