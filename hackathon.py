import datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="deez")

pool = []

class Trip:
    def __init__(self):
        timeStart = datetime.datetime.now()

class Person:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.path = geolocator.geocode(self.endpoint)

    def __repr__(self):
        return self.path
      
def addperson(endpoint):
    newPerson = Person(endpoint)
    pool.append(newPerson)
    newPath = newPerson.__repr__()
    print(newPath)


addperson("Worcester Polytechnic Institute, Worcester, Massachusetts")
#stores everything as ints



