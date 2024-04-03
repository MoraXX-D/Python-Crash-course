class Car():
    def __init__(self,make,model,year) -> None:
        '''initialize attribute to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.ododmeter_reading = 0

    def get_description_name(self):
        '''return a nearly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''print a message shoing car mileage'''
        print("This car has " + str(self.ododmeter_reading) + " mileage on it")

    def update_odometer_reading(self,mileage):
        '''this function update odometer reading using a method and preventing roll back'''
        if mileage > self.ododmeter_reading:
            self.ododmeter_reading = mileage
        else:
            print("You cannot roll back the reading.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    '''represent aspect of car, specific to EVs'''
    def __init__(self,make,model,year):
        super.__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        '''describing battery'''
        print("This car has a " + str(self.battery_size) + "-kwh battery")
