import datetime
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="deez")

class Trip:
    def __init__(self):
        self.timeStart = datetime.datetime.now()
        self.pool = []

    def __repr__(self):
        return str([self.timeStart, self.pool])
    
    def addperson(self):
        destination = input("enter destination")
        username = input("enter name")
        newPerson = Person(destination, username)
        self.pool.append(newPerson.__repr__())
        newPath = newPerson.__repr__()
        #print(newPath)

class Person:
    def __init__(self, endpoint, alias):
        self.alias = alias
        self.endpoint = endpoint
        self.path = geolocator.geocode(self.endpoint)

    def __repr__(self):
        return [str(self.path), self.alias]

newTrip = Trip()
newTrip.addperson()
newTrip.addperson()
newTrip.addperson()

newtime = newTrip
print(newtime)