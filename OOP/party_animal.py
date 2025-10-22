class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("I am destructed", self.x)

class FootballFan(PartyAnimal):
    def __init__(self):
        super().__init__()
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print("Points", self.points)

an = PartyAnimal()
an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))

j = FootballFan()
j.party()
j.touchdown()