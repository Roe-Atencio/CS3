class Vehicle:
  color = "Gray"
  def __init__(self,name,passengers):
    self.name = name
    self.passengers = passengers
  def move(self):
    print(f"Vehicle {self.color, self.name} is moving.\nIt has {passengers} passengers.")

class Car(Vehicle):
  def move(self):
    print(f"Car {self.color, self.name} is traveling along the road.\nIt has {passengers} passengers.")

class Boat(Vehicle):
  def move(self):
    print(f"Boat {self.color, self.name} is sailing along the water.\nIt has {passengers} passengers.")

class Skateboard:
  def move(self):
    print("The skateboard is moving.")

car1 = Car("Toyota Altis", 5)
car1.color = "Red"
car2 = Car("BYD Sealion 5", 5)
car2.color = "Blue"
car1 = Car("Yacht", 5)
car1.color = "White"
skbd = Skateboard()

vehicles = [car1, car2, boat, skbd]
for v in vehicles:
  v.move()
