from PythonQ1 import Vehicle

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)


    def __repr__(self):
        return "Name: " + self.name + "\n \t" + "Max speed: " + self.max_speed + "\n \t" + "Mileage: " + self.mileage


Arriva = Bus('Arriva', '50', '1000')

print(Arriva)