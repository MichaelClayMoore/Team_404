import geocoder
import json
import requests

class geocodeUtility:
	def __init__(self):
		self.key = '903089c411a84a9198467beb0268fcc4'
		self.tamuURL = "http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP/default.aspx?lat=" #32.417037,-97.759602
		self.tamuURL2 = "&state=tx&apikey=903089c411a84a9198467beb0268fcc4&format=json&notStore=false&version=4.01"

	def getLatLong(self, locAddress):
		try:
			g = geocoder.tamu(locAddress.get('address1'), city=locAddress.get('city'), state=locAddress.get('state'), zipcode=locAddress.get('zip'), key=self.key)
			if (g.json.get('accuracy') == 'GPS' or g.json.get('accuracy') == 'BuildingCentroid' or g.json.get('accuracy') == 'Parcel' or g.json.get('accuracy') == 'StreetSegment' or g.json.get('accuracy') == 'StreetIntersection' or g.json.get('accuracy') == 'StreetCentroid'):
				f = {}
				f['latitude'] = g.json.get('output_geocode').get('Latitude')
				f['longitude'] = g.json.get('output_geocode').get('Longitude')
				f['accuracy'] = g.json.get('accuracy')
				f['error'] = 'true'
				return f
			else:
				f = {}
				f['latitude'] = g.json.get('output_geocode').get('Latitude')
				f['longitude'] = g.json.get('output_geocode').get('Longitude')
				f['accuracy'] = g.json.get('accuracy')
				f['error'] = 'false'
				return f
		except Exception as e:
			print("*********************************************")
			print(e)
			print("*********************************************")
			return dict()

	def getAddress(self, locAddress):
		try:
			lat = locAddress.get('latitude')
			lon = locAddress.get('longitude')
			#create the URL
			urlFinal = self.tamuURL + str(lat) + '&lon=' + str(lon) + self.tamuURL2
			myResponse = requests.get(urlFinal)
			jData = {}
			if(myResponse.ok):
				jData = json.loads(myResponse.content)
			finalData = jData['StreetAddresses'][0]
			return {'StreetAddress' : finalData.get('StreetAddress'), 'City' : finalData.get('City'), 'State' : finalData.get('State'), 'Zip' : finalData.get('Zip')}
		except Exception as e:
			print("*********************************************")
			print(e)
			print("*********************************************")
			return dict()
