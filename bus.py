from vehicle import Vehicle
class Bus(Vehicle):
        ### Below is an class variable/attribute and not instance variable , all instances will share the same attribute
    # top_speed = 100
    # warnings = []

#We use constructor so that we can use instance variables instead of class variables 
### __ (double underscore) is called dunder , below is special method and there are many other
    def __init__(self, starting_top_speed = 100):
        
        # super gives access to base class
        super().__init__(starting_top_speed)
        ## since we have extra attibute we kept the constructor for inheritance 
        self.passengers =[]


    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 =Bus(100)

bus1.add_group(['Wi','Alisa','Wilbur'])
bus1.add_warning('checking inheritance using super keyword')
print(bus1.passengers)
bus1.drive()
