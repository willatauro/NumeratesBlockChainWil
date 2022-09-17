

from vehicle import Vehicle

class Car(Vehicle):


    def brag(self):
        print('Look how cool the car is and this method is only in car class')


car1 = Car()
car1.drive()

## remember Class.function is not the same as classobject.function .. read python docs
#Car.drive(car1)

## below anyone can access warnings
#car1.warnings.append('New Warning')
car1.add_warning('Access the method to add warning')
#car1.__warnings.append('New Warning')
#print(car1.__warnings)

#print object, you can use special method __dict__
#print(car1.__dict__)
print(car1)

Car.top_speed = 200
#car2 = Car()
car2 = Car(200)
car2.drive()

## since its private you cant access it outside the class using below syntax
#print(car2.__warnings)

print(car2.get_warnings())


#car3 = Car()
car3 = Car(300)
car3.drive()
#print(car3.__warnings)
print(car3.get_warnings())