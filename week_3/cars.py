# this is a class that describes cars

class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,color,horse_power):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.color = color
        self.horse_power = horse_power

    def print_make(self,make):
        print(" The car is of {0} make" .format(self.make))

    
    def set_make(self,make):
        self.make = make

    def get_make(self):
        return self.make
    
    def set_color(self,color):
        self.color = color

    def get_color(self):
        return self.color



my_car = car("Impalla ","Chrevolet","1969","2500 cc","lilac","390 HP")

friends_car = car("Note ","Nissan","2014","1400 cc","black","150 HP")

my_car.print_make("Nissan")

my_car.set_make("Ford")
friends_car.set_make("Toyota")

print(my_car.get_make())
print(friends_car.get_make())

my_car.set_color("Blue")
friends_car.set_color("Gray")


print(my_car.get_color())
print(friends_car.get_color())


