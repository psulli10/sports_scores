class Player:
    
    def __init__(self, name, attributes, squad_number, position, team, id=None):
        self.name = name
        self.attributes = attributes
        self.squad_number = squad_number
        self.position = position
        self.team = team
        self.id = id