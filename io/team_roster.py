import pandas


class TeamRosterEntry:
    def __init__(self, team_id, player_id, list_id):
        self.team_id = team_id
        self.player_id = player_id
        self.list_id = list_id
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'player_id: {self.player_id}',
            f'list_id: {self.list_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TeamRosterEntry(*row)
        data.append(obj)

    return data
