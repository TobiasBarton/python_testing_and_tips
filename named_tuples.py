from collections import namedtuple

Car = namedtuple('Car', 'colour mileage')

my_car = Car('red', 3812.4)
print(my_car.colour)
print(my_car.mileage)
print(my_car)

# Like tuples, namedtuples are immutable
# Therefore, you can't set an attribute
my_car.colour = 'blue'
