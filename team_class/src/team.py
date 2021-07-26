class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        return self.players.append(new_player)
        
    def has_player(self, name):
        if name in self.players:
            return True
        else:
            return False

    def play_game(self, result):
    
        if result == True:
            self.points += 3
        else:
            self.points += 0