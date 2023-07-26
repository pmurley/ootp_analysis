import pandas


class SubLeague:
    def __init__(self, league_id, sub_league_id, name, abbr, gender, designated_hitter):
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.name = name
        self.abbr = abbr
        self.gender = gender
        self.designated_hitter = designated_hitter
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'name: {self.name}',
            f'abbr: {self.abbr}',
            f'gender: {self.gender}',
            f'designated_hitter: {self.designated_hitter}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = SubLeague(*row)
        data.append(obj)

    return data
