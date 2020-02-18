class Athlete:
    def __init__(self, name):
        self.name = name
class Footballer(Athlete):
    def __init__(self, name, team):
        super(Footballer, self).__init__(name)
        self.team = team
Player1 = Footballer("Jay", "Droylsden FC")