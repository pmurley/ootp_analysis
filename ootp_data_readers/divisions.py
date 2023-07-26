import pandas


class Division:
    def __init__(self, league_id, sub_league_id, division_id, name, gender):
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.name = name
        self.gender = gender
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'name: {self.name}',
            f'gender: {self.gender}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = Division(*row)
        data.append(obj)

    return data
