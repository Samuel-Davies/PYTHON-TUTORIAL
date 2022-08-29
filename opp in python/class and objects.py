
# class definition below
class Computer:
    #attributes 

    #methods / functions
    def config(self):
        print("i5, 16GB, 1TB")

# object definition below

computer1 = Computer()
computer2 = Computer()

#accessing methods in python
Computer.config(computer1)
Computer.config(computer2)

# mostly the below syntax is more used or employed
computer1.config()
