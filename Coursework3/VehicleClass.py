### Aya Ishida (MSc IT) 
### ISD Term2 Coursework 2, Submitted at 9/3/2016
### Question 1

class Vehicle:
    
    # instance variables
    def __init__(self, registration):
        self._registration = registration
        self._make = ""
        self._engineSize = 0
        self._fuel = ""
        
    # register the vehicle code
    def setRegistration(self, registration):
        self._registration = registration

    def getRegistration(self):
        return self._registration
    
    # register the make type
    def setMake(self, make):
        self._make = make
        
    def getMake(self):
        return self._make

    # register the engine size
    def setEngineSize(self, engineSize) :
        self._engineSize = engineSize
        
    def getEngineSize(self):
        return self._engineSize
    
    # register the fuel type
    def setFuel(self, fuel):
        self._fuel = fuel

    def getFuel(self):
        return self._fuel

    # display all the vehicle registration
    def __repr__(self):
        return "Vehicle Registration: " + self.getRegistration() + "\nMake: ".ljust(23) + self.getMake() + "\nEngine Size: ".ljust(23) + str(self.getEngineSize()) + "\nFuel: ".ljust(23) + self.getFuel()

### Question 2

# This is an inheritance of Vehicle class     
class Car(Vehicle):

    # instance variables
    def __init__(self, registration):
        super().__init__(registration)
        self._NumberOfSeats = 0
        self._body = ""

    # register the number of seats
    def setNumberOfSeats(self, NumberOfSeats):
        self._NumberOfSeats = NumberOfSeats

    def getNumberOfSeats(self):
        return self._NumberOfSeats

    # register the body type
    def setBody (self, body):
        self._body = body

    def getBody(self):
        return self._body

    # display all the vehicle and car registration
    def __repr__(self):
        return super().__repr__() + "\nNumber of Seats: ".ljust(23) + str(self.getNumberOfSeats()) + "\nBody: ".ljust(23) + self.getBody() 

# This is an inheritance of Vehicle class
class Motorcycle(Vehicle):

    # instance variables
    def __init__(self, registration):
        super().__init__(registration)
        self._offRoad = ""

    # register the off road type 
    def setDrivableOffRoad(self, offRoad):
        self._offRoad = offRoad

    def getDrivableOffRoad(self):
        return self._offRoad
    
    # display all the vehicle and motorcycle registration
    def __repr__(self):
        return super().__repr__() + "\nOff Road: ".ljust(23) + str(self.getDrivableOffRoad())
