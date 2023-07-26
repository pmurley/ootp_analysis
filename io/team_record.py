import pandas


class TeamRecordEntry:
    def __init__(self, team_id, g, w, l, t, pos, pct, gb, streak, magic_number):
        self.team_id = team_id
        self.g = g
        self.w = w
        self.l = l
        self.t = t
        self.pos = pos
        self.pct = pct
        self.gb = gb
        self.streak = streak
        self.magic_number = magic_number
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'g: {self.g}',
            f'w: {self.w}',
            f'l: {self.l}',
            f't: {self.t}',
            f'pos: {self.pos}',
            f'pct: {self.pct}',
            f'gb: {self.gb}',
            f'streak: {self.streak}',
            f'magic_number: {self.magic_number}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = TeamRecordEntry(*row)
        data[obj.team_id] = obj

    return data
