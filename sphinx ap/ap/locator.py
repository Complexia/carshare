import googlemaps

class Locator:
    def __init__(self):
        self.__gmaps = googlemaps.Client(key='AIzaSyD3yIi6xf7-w-kLInP2DHHY0n7_nfsocHU')

    def getCarLocation(self, car):
        carLocation = car.getLocation()
        return self.__extractImportantGeoData(carLocation)
    
    def __extractImportantGeoData(self, carLocation):
        geoData = self.__gmaps.reverse_geocode((carLocation['x'], carLocation['y']))

        addressComponents = geoData[0]['address_components']

        location = ''

        for i in range(len(addressComponents)):
            location += self.__getCurrentAddresssComponent(addressComponents, i) + ' '

        return location

    def __getCurrentAddresssComponent(self, addressComponents, index):
        return addressComponents[index]['long_name']

locator = Locator()