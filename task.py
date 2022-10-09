class Vehicle:
    speed = 0
    has_wheel = False
    wheels_number = 0

    def speed_up(self, current):
        self.speed = current + 5

    def speed_down(self, current):
        self.speed = -5

    def stop(self, current):
        self.speed = 0


class Car(Vehicle):
    speed = 5
    has_wheel = True
    wheels_number = 4

    def speed_up(self, current):
        self.speed = current + 10


class Ship(Vehicle):
    def speed_up(self, current):
        self.speed = current + 20


obj1 = Vehicle()
obj1.speed_up(10)
print(obj1.speed)
obj1.stop(10)
print(obj1.speed)



obj2 = Car()
obj2.speed_up(10)
print(obj2.speed)



obj3 = Ship()
obj3.speed_up(10)
print(obj3.speed)
