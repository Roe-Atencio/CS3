class Sauce:
  def __init__(self, name, taste):
    self.name = name
    self.taste = taste

class Tusoktusok:
  name = ""
  sauce = []
  def __init__(self, name):
    self.name = name
  def dip(self, sauce):
    self.sauce.append(sauce)
  def eat(self):
    print(f"I ate {self.name} with {self.sauce.name} and it tastes {self.sauce.taste}.")

fishball = Tusoktusok("fishball")
vinegar = Sauce("vinegar", "sour")
sweet = Sauce("sweet sauce", "sweet")
spicy = ("spicy sauce", "spicy")
fishball.dip(vinegar)
fishball.dip(sweet)
fishball.dip(spicy)
