import datetime
import copy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="deez")
#the quick brown fox jumps over the lazy dog

userList = []
    
def addUser(newUser):
        if userList.count == 0:
            userList.append(newUser)
        else:
            for i, existingUser in enumerate(userList):
                if newUser.upper < existingUser.upper():
                    userList.insert(i, newUser)
                    break
            
class Trip:
    def __init__(self, driver, startLocation, destination, startTime):
        self.startTime = startTime
        self.rideRequests = []  #list of all active requests
        self.riders = []    #list of all active riders in the carpool
        self.driver = driver
        self.startLocation = startLocation
        self.destination = destination
        
    def __repr__(self):
        return str([self.startTime.strftime("%Y-%m-%d %H:%M:%S"),"Driver: ", self.driver ,"Riders: ", self.riders])
    
    def getStartTime(self):
        return self.startTime
    
    def addRider(self, rider):
        #adds a rider to the trip
        self.riders.append(rider)

class Account:
    def __init__(self, username):
        self.username = username
        self.tripHistory = []
        self.plannedTrips = []
        self.currentTrip = None
        self.path = 'placeholder'
        self.stopTime = None
        addUser(self)

    def __repr__(self):
        return str([self.path, self.username])
    

    #called when a driver account creates a new trip
    def newDriverTrip(self):
        #gets the gps location from the user
        startLocation = geolocator.geocode(input("Enter Start Location: "))
        destination = geolocator.geocode(input("Enter Driver Destination: "))
        #gets the time
        startTime = datetime.datetime.now()

        #creates a new trip with all the parameters
        thisTrip = Trip(self, startLocation, destination, startTime)

        #adds the current trip to a list of planned trips (trips that aren't archived)
        self.plannedTrips.append(thisTrip)
        return thisTrip


    #called when a rider requests to join a driver's trip
    def riderTripRequest(self, trip):
        #gets the gps location from the user
        destination = geolocator.geocode(input("Enter Rider Destination: "))
        self.currentTrip = destination

        #appends the rider's request to a list of requests the driver can accept or deny
        trip.rideRequests.append((self.username , destination))


    def acceptRequest(self, trip: Trip, rider):
        #adds the rider to the trip, and removes their request
        trip.addRider(rider)
        fullTrip = copy.deepcopy(trip)
        trip.rideRequests.remove((rider.username, rider.currentTrip))
        return fullTrip
    

    def denyRequest(self, trip: Trip, rider):
        #removes the rider's request without adding them to the trip
        trip.rideRequests.remove((rider.username, rider.currentTrip))


    def requestFulfilled(self, trip):
        #gets the endtime of the trip for each rider, allowing for personalized data collection
        self.stopTime = datetime.datetime.now()
        


#creates the driver and rider accounts
driver = Account("Milo")
rider1 = Account("Max")
rider2 = Account("Charlie")
rider3 = Account("Scott Gurney")

trip = driver.newDriverTrip()

rider1.riderTripRequest(trip)
rider2.riderTripRequest(trip)
rider3.riderTripRequest(trip)

print(trip.rideRequests)

#since all requests are accepted, the riderequests list is now empty
driver.acceptRequest(trip, rider1)
driver.acceptRequest(trip, rider2)
driver.acceptRequest(trip, rider3)
print(trip.rideRequests)
