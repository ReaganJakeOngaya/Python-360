from Car import Car, ElectricCar

my_new_car = Car("Volvo", "TX4", 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 33
my_new_car.read_odometer()

my_electrict_car = ElectricCar("Tesla", "Model S", 2022)
print(my_electrict_car.get_descriptive_name())