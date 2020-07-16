class Csgo_stats():

    def __init__(self, hours, total_kills, total_deaths, defused_bombs, planted_bombs, money_earned, mvps, total_wins, knife_kills, shots_fired, shots_hit):
        self.hours = hours
        self.total_kills = total_kills
        self.total_deaths = total_deaths
        self.defused_bombs = defused_bombs
        self.planted_bombs = planted_bombs
        self.money_earned = money_earned
        self.mvps = mvps
        self.total_wins = total_wins
        self.knife_kills = knife_kills
        self.shots_fired = shots_fired
        self.shots_hit = shots_hit
        self.accuracy = self.calc_accuracy()
        self.kd_ratio = self.calc_kd_ratio()

    def to_json(self):
        return {
            'hours': self.hours,
            'total_kills': self.total_kills,
            'total_deaths': self.total_deaths,
            'defused_bombs': self.defused_bombs,
            'planted_bombs': self.planted_bombs,
            'money_earned': self.money_earned,
            'mvps': self.mvps,
            'total_wins': self.total_wins,
            'knife_kills': self.knife_kills,
            'shots_fired': self.shots_fired,
            'shots_hit': self.shots_hit,
            'accuracy': self.accuracy,
            'kd_ratio': self.kd_ratio
        }

    def calc_accuracy(self):
        return round((self.shots_hit / self.shots_fired) * 100, 2)

    def calc_kd_ratio(self):
        return round(self.total_kills / self.total_deaths, 2)