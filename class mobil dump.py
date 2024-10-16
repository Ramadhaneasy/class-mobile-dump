#define a class
class Truck:
    name = ""
    spion = 0
    bak = 0
#create object of classes
#instansiasi dari kelas mobil dump
mobildump = Truck()
#access attributes and assign new value
mobildump.spion = 2
mobildump.bak = 1
mobildump.name = "mobildump rama"
print(f"Name : {mobildump.name}, spion : {mobildump.spion}, bak : {mobildump.bak}")
