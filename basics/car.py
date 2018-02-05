class car (object):
  def __init__ (self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name (self):
    log_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return log_name.title()

  def read_odometer (self):
    print('this car has %s miles on it.' % self.odometer_reading)
  
  def update_odometer (self, mileage):
    self.odometer_reading = mileage

  def increment_odometer (self, miles):
    self.odometer_reading += miles

class batterys ():
  def __init__ (self, batterys_size = 80):
    self.batterys_size = batterys_size
  
  def describe_battery (self):
    print('this car has a %s kWh battery.' % self.batterys_size)

class electricCar (car):
  def __init__ (self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = 70
    self.batterys = batterys()
  
  def describe_battery (self):
    print('this car has a %s -kWh battery.' % self.battery_size)

  def fill_gas_tank (self):
    print('this car doesn\'t need a gas tank!')

# my_new_car = car('aui', 'a4', 2016)

# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

# my_tesla = electricCar('tesla', 'model s', 2016)

# print(my_tesla.get_descriptive_name())

# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.describe_battery()