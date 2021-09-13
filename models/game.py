class Game:

    def __init__(self, home, away, home_goals, away_goals, id = None):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.result = 'To be determined...'
        self.id = id

        self.get_result()

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
                'winner': 0
            }
        
        return self.result['winner']
