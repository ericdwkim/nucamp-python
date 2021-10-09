class Vehicle:
    def __init__(self, num_wheels, color):
        self.num_wheels = num_wheels
        self.color = color
        self.fuel_percent = 0

    def add_fuel(self, fuel_amt):
        self.fuel_percent += fuel_amt


class Truck(Vehicle):
    def __init__(self, num_wheels, color):
        super().__init__(num_wheels, color)


motorcycle = Vehicle(2, "black")
motorcycle.add_fuel(50)
print(motorcycle.fuel_percent)


"""
    How would you create an instance of this class w/ the name of "motorcycle" and a color of "black"?
    >> motorcycle = Vehicle(2, "black")

    How would you use the method to add fuel to the instance?
    >> motorcycle.add_fuel(50)

    How would you write code to retrieve the % of fuel?
    >> motorcycle.fuel_percent

"""
