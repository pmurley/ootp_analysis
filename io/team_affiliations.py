import pandas


class TeamAffiliationEntry:
    def __init__(self, team_id, affiliated_team_id):
        self.team_id = team_id
        self.affiliated_team_id = affiliated_team_id
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'affiliated_team_id: {self.affiliated_team_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TeamAffiliationEntry(*row)
        data.append(obj)

    return data
