# 1. Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
# Method: fare. It should calculate the price of the trip.
# Formula: total_capacity * 100. Example, total_capacity = 50 => fare = 5000

class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100


# 2. Create classes Bus and Car that inherit Vehicle.

class Bus(Vehicle):

    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity

    def check_capacity(self):
        if self.total_capacity > self.used_capacity:
            pass
        raise Exception('Error capacity overlimit')

    def fare(self):
        return self.total_capacity * 110

    def __len__(self):
        return len(self.name)

class Car(Vehicle):
    pass


# 3. Create 3 car objects and 2 bus objects

car_1 = Car('Honda', 1200, 40)

car_2 = Car('Mercedes', 20, 10)

car_3 = Car('Zaz', 120, 30)

bus_1 = Bus('Buss', 40, 70, 60)

bus_2 = Bus('Buus', 60, 70, 71)


# 4. Check: if car_1 is instance of Car.  if car_2 is instance of Vehicle.
# if bus_1 is instance of Car. if bus_1 is instance of Vehicle.

def check(x, y):
    if isinstance(x, y) == True:
        print('{} is instance to class {}'.format(x.name, y.__name__))
    else:
        print('{} is not instance to class {}'.format(x.name, y.__name__))

check(car_1, Car)
check(car_2, Vehicle)
check(bus_1, Car)
check(bus_1, Vehicle)


# 5. Override fare method for Bus class.
# Here we need to add an extra 10% to the fare.
# Formula: total_fare + 10% of total_fare.
# Example, fare = 50 => total_fare = 5500

# Не знайшов інформації як додавати методи в існуючі класи поза межами класів, тому просто додав в класс вище

# 6. Add used_capacity attribute for Bus. It means how many people are on the bus.
# If used_capacity > total_capacity raise an error.

# Аналогічно все в автобусі

# 7. Write a magic method to Bus that would be triggered when len() function is called.
# To figure out what magic method you should implement,
# take a look at the full list of magic methods: https://www.tutorialsteacher.com/python/magic-methods-in-python.
# Play around with other dunder methods

# Аналогічно все в автобусі

# 8. Create class Engine with attribute volume and method get_volume() that will return volume.

class Engine(Car):
    def __init__(self, name, max_speed, total_capacity, volume):
        super().__init__(name, max_speed, total_capacity)
        self.volume = volume

    def get_volume(self):
        return self.volume

# 9. Inherit Engine by Car class.

# Аналогічно все в класі двигун

# 10. Check what is inheritance order of the Car class

print (f"Engine is inherit of Car - {issubclass(Engine, Car)}")