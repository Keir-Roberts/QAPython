class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return int(self.capacity) * 100


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)

    def fare(self):
        amount = super().fare()
        maintamount = amount * 1.1
        return maintamount


schoolbus = Bus("School", 60, 1000, 50)

print(schoolbus.fare())




