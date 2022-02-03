class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}"


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self, capacity="50"):
        return f"The seating capacity of {self.name} is {capacity}" 



focus = Bus("focus", "80", "1000")
print(focus.seating_capacity())