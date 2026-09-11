# Section: 9 - Pinatubo        Score:____________
# C# / Name: #18 Atencio       Date: 08/15/2026

class Glassware:
  def __init__(self, glassware_type):
    self.glassware_type = glassware_type
    print("Glassware removed from cabinet.")
  def __del__(self):
    print(glassware_type, "shattered on the floor.")

class Beaker(Glassware):
  def __init__(self, glassware_type, liquid_amount):
    super().__init__(glassware_type)
    self.liquid_amount = liquid_amount
class Tray:
  def __init__(self):
    print("Tray removed from cabinet.")
