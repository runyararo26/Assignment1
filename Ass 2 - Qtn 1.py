class Vehicle:
    def move(self):
        return "Vehicle moves"

class Car(Vehicle):
    def move(self):  # override
        return "Car drives on roads"

class Bike(Vehicle):
    def move(self):  # override
        return "Bike is pedaled"

# Demo
v = Vehicle()
c = Car()
b = Bike()
print(v.move())
print(c.move())
print(b.move())