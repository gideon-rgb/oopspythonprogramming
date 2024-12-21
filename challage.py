class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

class Bicycle(Vehicle):
    def move(self):
        return "Pedalling"


car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()


vehicles = [car, plane, boat, bicycle]

for vehicle in vehicles:
    print(vehicle.move())
