class Car:
    #class viables
    wheels = 4

    def __init__(self):
        # VARIABLES HERE ARE IINSTANCE VARIABLES
        # BECAUSE THEY CHANGE AS OBJECT CHANGES
        self.mil = 10
        self.com = 'BMW'



c1 = Car()

Car.wheels = 12

print(c1.wheels)