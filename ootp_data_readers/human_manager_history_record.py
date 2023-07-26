import pandas


class HumanManagerHistoryRecord:
    def __init__(self, human_manager_id, team_id, year, league_id, sub_league_id, division_id, g, w, l, pos, pct, gb, streak, magic_number):
        self.human_manager_id = human_manager_id
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.g = g
        self.w = w
        self.l = l
        self.pos = pos
        self.pct = pct
        self.gb = gb
        self.streak = streak
        self.magic_number = magic_number
    
    def __str__(self):
        return "\n".join([
            f'human_manager_id: {self.human_manager_id}',
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'g: {self.g}',
            f'w: {self.w}',
            f'l: {self.l}',
            f'pos: {self.pos}',
            f'pct: {self.pct}',
            f'gb: {self.gb}',
            f'streak: {self.streak}',
            f'magic_number: {self.magic_number}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = HumanManagerHistoryRecord(*row)
        data.append(obj)

    return data
