class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('Im in me mums', self.model + ', Vroom Vroom')

    def stop(self):
        print("Get out me", self.model + ". Aww")


Car_1 = Car('Honda', 'Civic', '1998', 'Red')

Car_1.stop()

print(Car_1.make)