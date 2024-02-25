import datetime
import copy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="deez")

class Users:
    def __init__(self):
        self.userList = []
    
    def addUser(self, newUser):
        if self.userList.length == 0:
            self.userList.insert(newUser)
        else:
            for i, existingUser in enumerate(self.userList):
                if newUser.upper < existingUser.upper():
                    self.userList.insert(i, newUser)
                    break
            
class Trip:
    def __init__(self, driver, startLocation, destination, startTime):
        self.startTime = startTime
        self.rideRequests = []
        self.riders = []
        self.driver = driver
        self.startLocation = startLocation
        self.destination = destination
        
    def __repr__(self):
        return str([self.startTime.strftime("%Y-%m-%d %H:%M:%S"), self.driver , self.riders])
    
    def requestRide(self, riderinfo):
        self.rideRequests.append(riderinfo)
    
    def getStartTime(self):
        return self.startTime
    
    def addRider(self, rider):
        #self.rideRequests.pop(rider)
        self.riders.append(rider)

class Account:
    def __init__(self, username):
        self.username = username
        self.tripHistory = []
        self.plannedTrips = []
        self.currentTrip = None
        self.path = 'placeholder'
        self.stopTime = None

    def __repr__(self):
        return str([self.path, self.username])
    
    def newDriverTrip(self):
        startLocation = geolocator.geocode(input("Enter Start Location: "))
        destination = geolocator.geocode(input("Enter Driver Destination: "))
        startTime = datetime.datetime.now()
        thisTrip = Trip(self, startLocation, destination, startTime)
        self.plannedTrips.append(thisTrip)
        #startTime = input("Enter Start Time: ") 
        return thisTrip

    def riderTripRequest(self, trip):
        destination = geolocator.geocode(input("Enter Destination: "))
        self.currentTrip = destination
        trip.requestRide((self.username , destination))

    def acceptRequest(self, trip: Trip, rider):
        trip.addRider(rider)
        fullTrip = copy.deepcopy(trip)
        trip.rideRequests.remove((rider.username, rider.currentTrip))
        return fullTrip

    def requestFulfilled(self, trip):
        self.stopTime = datetime.datetime.now()
        

driver = Account("driver")
rider1 = Account("rider1")
rider2 = Account("rider2")

trip = driver.newDriverTrip()

rider1.riderTripRequest(trip)
rider2.riderTripRequest(trip)

print(trip.rideRequests)

driver.acceptRequest(trip, rider2)
print(trip.rideRequests)

#rider2.requestFulfilled(trip)

#print(trip.rideRequests)
#print(fullTrip.rideRequests)