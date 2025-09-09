from ex8a import Car
from ex8a import ElectricCar as EC

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_leaf = EC('nissan', 'leaf', 2024)