class Game:

    def __init__(self, home, away, home_goals, away_goals, id = None):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.result = 'To be determined...'
        self.id = id

    def get_result(self):
        if self.home_goals > self.away_goals:
            self.result = {
                'winner': self.home.id
            }
        elif self.home_goals < self.away_goals:
            self.result = {
                'winner': self.away.id
            }
        else:
            self.result = {
                'winner': None
            }
        
        return self.result['winner']
