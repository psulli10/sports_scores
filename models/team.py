from models.attribute import Attribute

class Team:

    def __init__(self, name, attributes, wins = 0, draws = 0, defeats = 0, players = None, id = None):
        self.name = name
        self.attributes = attributes
        self.wins = wins
        self.draws = draws
        self.defeats = defeats
        self.players = players
        self.id = id

    def add_player(self, player):
        if self.players is None:
            self.players = []
        self.players.append(player)

    def remove_player(self, player):
        if self.players is None:
            return None
        self.players.remove(player)

    def get_total_players(self):
        if self.players is None:
            return 0
        return len(self.players)

    def set_team_attributes(self):

        total_players = self.get_total_players()
        attributes_to_update_list = vars(self.attributes).keys()
        
        for player in self.players:
            for attribute in attributes_to_update_list:
                if attribute != 'id': 
                    player_attribute = getattr(player.attributes, attribute)
                    team_attribute = getattr(self.attributes, attribute)
                    new_attribute_total = team_attribute + player_attribute
                    setattr(self.attributes, attribute, new_attribute_total)

        for attribute in attributes_to_update_list:
            if attribute != 'id':
                team_attribute = getattr(self.attributes, attribute)
                new_attribute_average = team_attribute / total_players
                setattr(self.attributes, attribute, new_attribute_average)


    def update_result(self, result_to_update):
        attribute_to_update = getattr(self, result_to_update)
        new_total = attribute_to_update + 1
        setattr(self, result_to_update, new_total)