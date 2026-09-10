# Section: 9 - Pinatubo        Score:____________
# C# / Name: #18 Atencio       Date: 08/15/2026

class Lab:
  def __init__(self, room_number):
    self.room_number = room_number

class Technician:
  def __init__(self, name):
    self.name = name
  def assigned_lab(self, lab_obj):
    self.assigned_lab = lab_obj

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)

print(mr_cruz.assigned_lab.room_number)
