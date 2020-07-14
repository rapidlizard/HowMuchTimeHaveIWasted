class Csgo_stats():

    def __init__(self, hours, total_kills, defused_bombs, planted_bombs, money_earned, mvps, total_wins, knife_kills, shots_fired, shots_hit):
        self.hours = hours
        self.total_kills = total_kills
        self.defused_bombs = defused_bombs
        self.planted_bombs = planted_bombs
        self.money_earned = money_earned
        self.mvps = mvps
        self.total_wins = total_wins
        self.knife_kills = knife_kills
        self.shots_fired = shots_fired
        self.shots_hit = shots_hit

    def to_json(self):
        return {
            'hours': self.hours,
            'total_kills': self.total_kills,
            'defused_bombs': self.defused_bombs,
            'planted_bombs': self.planted_bombs,
            'money_earned': self.money_earned,
            'mvps': self.mvps,
            'total_wins': self.total_wins,
            'knife_kills': self.knife_kills,
            'shots_fired': self.shots_fired,
            'shots_hit': self.shots_hit
        }
