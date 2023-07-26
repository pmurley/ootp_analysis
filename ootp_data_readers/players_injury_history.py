import pandas


class PlayersInjuryHistoryEntry:
    def __init__(self, player_id, date, length, setbacks, day_to_day, effect, body_part):
        self.player_id = player_id
        self.date = date
        self.length = length
        self.setbacks = setbacks
        self.day_to_day = day_to_day
        self.effect = effect
        self.body_part = body_part
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'date: {self.date}',
            f'length: {self.length}',
            f'setbacks: {self.setbacks}',
            f'day_to_day: {self.day_to_day}',
            f'effect: {self.effect}',
            f'body_part: {self.body_part}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersInjuryHistoryEntry(*row)
        data.append(obj)

    return data
