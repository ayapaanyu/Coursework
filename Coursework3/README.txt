Coursework 3

A vehicle showroom needs a new inventory system which you have been tasked to write. 
The showroom contains a variety of vehicles including cars and motorcycles.

Step One: Implement Vehicle Class
First we need a class to model vehicles. Start by creating a class called Vehicle. 
Copy and paste the skeleton below:

class Vehicle:
# This class has 4 instance variables: 
# registration, make, engineSize, fuel

def __init__(self,registration): 
	# Implement this method 
	# set both make and fuel to an empty string 
	# set engineSize to integer value zero

def setRegistration(self, registration): 
	# set the engine registration 
	# Implement this method

def getRegistration(self): 
	# returns the registration 
	# Implement this method

def setMake(self, make): 
	# set the vehicle make 
	# Implement this method

def getMake(self): 
	# returns the vehicle make 
	# Implement this method

def setEngineSize(self, engineSize) : 
	# set the engine size
	# Implement this method

def getEngineSize(self): 
	# returns the engine size 
	# Implement this method

def setFuel(self, fuel): 
	# set the fuel type 
	# Implement this method

def getFuel(self): 
	# returns the fuel type 
	# Implement this method

def __repr__(self): 
	# Implement this method

Also copy and paste the following test class into another ?le called VehicleTester:

# Small test of the Vehicle class 
example = Vehicle("AB12 ABC") 
print("Vehicle Registration: " + example.getRegistration()) 
example.setMake("Audi") 
print("Make: " + example.getMake()) 
example.setEngineSize(1.6) 
print("Engine Size: " + str(example.getEngineSize())) 
example.setFuel("DIESEL") 
print("Fuel: " + example.getFuel()) 
example.setRegistration("EF34 CDE") 
print() print(example)

The Vehicle class de?nes methods to store and retrieve common vehicle details. 
However, the skeleton that we provide is incomplete. 
The VehicleTester ?le tests the methods. When you run the program, 
the output should be:

Vehicle Registration: AB12 ABC 
Make: Audi 
Engine Size: 1.6 
Fuel: DIESEL

Vehicle Registration: EF34 CDE 
Make: Audi 
Engine Size: 1.6 
Fuel: DIESEL

Complete the Vehicle class with the appropriate code to successfully run 
the VehicleTester ?le (you will need to import the class). 

Step Two: Implement Car and Motorcycle Classes
Next we construct two further classes that represent cars and motorcycles. 
Both classes inherit from our Vehicle class. 
For cars we wish to record the additional following information:
1. The number of seats (an integer)
2. The body style (a string), e.g. HATCHBACK, SALOON, FOUR DOOR, and FIVE DOOR.

For Motorcycles we wish to record the additional following information:
1. A Boolean to denote whether the motorcycle can be driven o? the road.
Copy and paste the following incomplete class de?nitions.

class Car(Vehicle): 
	# Add the missing implementation to this class

class Motorcycle(Vehicle): 
	# Add the missing implementation to this class

All the additional methods and instance variables are missing from these class de?nitions.
You will need to de?ne and implement these missing methods and instance variables. 
In order to proceed we also provide the contents of a ?le called Portfolio 
which creates a portfolio of 3 vehicles, then performs some operations 
on these vehicles. Read the script to see what methods are missing from the Car 
and Motorcycle classes.

def main(): 
	example1 = Car("AB12 ABC") 
	example1.setMake("Audi") 
	example1.setEngineSize(1.6) 
	example1.setFuel("DIESEL") 
	example1.setNumberOfSeats(4) 
	example1.setBody("HATCHBACK") 
	print(example1) 
	example2 = Car("EF34 CDE") 
	example2.setMake("Volkswagen") 
	example2.setEngineSize(2.0) 
	example2.setFuel("UNLEADED PETROL")
	example2.setNumberOfSeats(6) 
	example2.setBody("SALOON") 
	print(example2) 
	example = Motorcycle("JK78 MNP") 
	example3.setMake("Kawasaki") 
	example3.setEngineSize(144) 
	example3.setFuel("UNLEADED_PETROL") 
	example3.setDrivableOffRoad(True) 
	print(example3)

	portfolio = [example1, example2, example3] 
	print( "*** Display Unleaded Vehicles Only ***" ) 
	print() 
	fuel = "UNLEADED PETROL" 
	DisplayVehiclesWithFuel(portfolio,fuel)

	print( "*** Display Unleaded Vehicles Only ***" ) 
	print() 
	fuel = "DIESEL" 
	DisplayVehiclesWithFuel(portfolio,fuel)

def DisplayVehiclesWithFuel(portfolio, fuel): 
	#Missing function body

The Portfolio ?le also has an incomplete function called DisplayVehiclesWithFuel. 
This function takes as arguments a list of vehicles and a fuel. 
The function simply displays to the screen all the vehicles in the list that use 
that fuel type. Using this description complete the body of DisplayVehiclesWithFuel. 
The output when you run the main function of Portfolio should be similar to the following:

Vehicle Registration: AB12 ABC 
Make: Audi 
Engine Size: 1.6 
Fuel: DIESEL

Number of Seats: 4 
Body: HATCHBACK 
Vehicle Registration: EF34 CDE 
Make: Volkswagen
Engine Size: 2.0
Fuel: UNLEADED PETROL

Number of Seats: 6 
Body: SALOON 
Vehicle Registration: JK78 MNP 
Make: Kawasaki 
Engine Size: 144.0 
Fuel: UNLEADED PETROL 
Off Road: true

*** Display Unleaded Vehicles Only ***

Vehicle Registration: EF34 CDE 
Make: Volkswagen 
Engine Size: 2.0 
Fuel: UNLEADED PETROL 
Number of Seats: 6 
Body: SALOON

Vehicle Registration: JK78 MNP 
Make: Kawasaki 
Engine Size: 144.0 
Fuel: UNLEADED PETROL 
Off Road: true

*** Display Diesel Vehicles Only ***

Vehicle Registration: AB12 ABC 
Make: Audi 
Engine Size: 1.6 
Fuel: DIESEL 
Number of Seats: 4 
Body: HATCHBACK