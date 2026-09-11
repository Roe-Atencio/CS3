# Section: 9 - Pinatubo        Score:____________
# C# / Name: #18 Atencio       Date: 08/15/2026

class Glassware:
    def __init__(self, name, glassware_type):
        self.name = name
        self.glassware_type = glassware_type
        print(f"{name} removed from cabinet.")

    def __del__(self):
        print(f"{self.name} has been lost to the floor.")

class Beaker(Glassware):
    def __init__(self, name, glassware_type, volume):
        super().__init__(name, glassware_type)
        self.volume = volume
        print(f"{name} is holding {volume} mL of liquid.")

class Tray:
    def __init__(self, name, beakers):
        self.name = name
        print(f"{name} removed from cabinet.")
        self.beakers = beakers

    def __del__(self):
        print(f"OH NO!! {self.name} fell on the floor! That's so tragic.")
        self.beakers = []

beaker_list = [Beaker("Beaker 1", "Beaker", 10),
              Beaker("Beaker 2", "Beaker", 20),
              Beaker("Beaker 3", "Beaker", 30),
              Beaker("Beaker 4", "Beaker", 40),
              Beaker("Beaker 5", "Beaker", 50),]

tray = Tray("tray", beaker_list)
del tray
