import pandas


class PlayersIndividualBattingStatsEntry:
    def __init__(self, player_id, opponent_id, ab, h, hr):
        self.player_id = player_id
        self.opponent_id = opponent_id
        self.ab = ab
        self.h = h
        self.hr = hr
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'opponent_id: {self.opponent_id}',
            f'ab: {self.ab}',
            f'h: {self.h}',
            f'hr: {self.hr}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersIndividualBattingStatsEntry(*row)
        data.append(obj)

    return data
