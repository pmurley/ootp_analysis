import pandas


class LeaguePlayoffFixture:
    def __init__(self, league_id, team_id0, team_id1, winner, finished, best_of, played, round, result0, result1):
        self.league_id = league_id
        self.team_id0 = team_id0
        self.team_id1 = team_id1
        self.winner = winner
        self.finished = finished
        self.best_of = best_of
        self.played = played
        self.round = round
        self.result0 = result0
        self.result1 = result1
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'team_id0: {self.team_id0}',
            f'team_id1: {self.team_id1}',
            f'winner: {self.winner}',
            f'finished: {self.finished}',
            f'best_of: {self.best_of}',
            f'played: {self.played}',
            f'round: {self.round}',
            f'result0: {self.result0}',
            f'result1: {self.result1}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeaguePlayoffFixture(*row)
        data.append(obj)

    return data
