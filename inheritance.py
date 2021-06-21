class vichel:
    def __init__(self,vichel,mileage,cost):
        self.vichle = vichel
        self.mileage = mileage
        self.cost = cost

    def show_vichel_details(self):
        print("The name of the vichel is:",self.vichle)
        print("The mileage of the vicheal is:",self.mileage)
        print("The cost of the vichel is:",self.cost)

v1 = vichel("Fortuner","20km","2500k")
v2 = vichel("Swift","30km","700k")
v1.show_vichel_details()
v2.show_vichel_details()

class car(vichel):
    def show_vichel_details(self):
        print("I am a car")        
c1 = car("Safari","10Km","2500K")
c1.show_vichel_details()