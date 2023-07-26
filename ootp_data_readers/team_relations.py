import pandas


class TeamRelationsEntry:
    def __init__(self, league_id, sub_league_id, division_id, team_id):
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.team_id = team_id
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'team_id: {self.team_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TeamRelationsEntry(*row)
        data.append(obj)

    return data
