import pandas


class PlayersStreakEntry:
    def __init__(self, player_id, league_id, streak_id, value, has_ended, started, ended):
        self.player_id = player_id
        self.league_id = league_id
        self.streak_id = streak_id
        self.value = value
        self.has_ended = has_ended
        self.started = started
        self.ended = ended
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'league_id: {self.league_id}',
            f'streak_id: {self.streak_id}',
            f'value: {self.value}',
            f'has_ended: {self.has_ended}',
            f'started: {self.started}',
            f'ended: {self.ended}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersStreakEntry(*row)
        data.append(obj)

    return data
