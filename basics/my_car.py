from car import car, electricCar

my_new_car = car('audi', 'a4', 2016)
my_tesla = electricCar('tesla', 'roadster', 2017)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1000)
my_new_car.read_odometer()

print(my_tesla.get_descriptive_name())