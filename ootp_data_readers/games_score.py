import pandas


class GameScore:
    def __init__(self, game_id, team, inning, score):
        self.game_id = game_id
        self.team = team
        self.inning = inning
        self.score = score
    
    def __str__(self):
        return "\n".join([
            f'game_id: {self.game_id}',
            f'team: {self.team}',
            f'inning: {self.inning}',
            f'score: {self.score}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = GameScore(*row)
        data.append(obj)

    return data
