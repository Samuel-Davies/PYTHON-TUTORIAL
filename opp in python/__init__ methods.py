class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram 

    def config(self):
        print("config is ", self.cpu, self.ram)


com1 = Computer('i7', 16)

com1.config()