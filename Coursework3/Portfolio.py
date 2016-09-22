### Aya Ishida (MSc IT) 
### ISD Term2 Coursework 2, Submitted at 9/3/2016
### Question 2

# import all classes in VehicleClass module
from VehicleClass import * 

# main function       
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
    example3 = Motorcycle("JK78 MNP")
    example3.setMake("Kawasaki")
    example3.setEngineSize(144)
    example3.setFuel("UNLEADED PETROL")
    example3.setDrivableOffRoad(True)
    print(example3)

    portfolio = [example1, example2, example3]
    print( "*** Display Unleaded Vehicles Only ***" )
    print()
    fuel = "UNLEADED PETROL"
    DisplayVehiclesWithFuel(portfolio,fuel)

    print( "*** Display Diesel Vehicles Only ***" )
    print()
    fuel = "DIESEL"
    DisplayVehiclesWithFuel(portfolio,fuel)

# print all vehicle feature again classified by fuel type
def DisplayVehiclesWithFuel(portfolio, fuel):
    i=0
    for i in range (len(portfolio)):
        if portfolio[i].getFuel() == fuel:
            print(portfolio[i])
        i=i+1

# start the main function
if __name__ == "__main__":
    main()
