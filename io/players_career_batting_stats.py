import pandas


class PlayersCareerBattingStatsEntry:
    def __init__(self, player_id, year, team_id, game_id, league_id, level_id, split_id, position, ab, h, k, pa, pitches_seen, g, gs, d, t, hr, r, rbi, sb, cs, bb, ibb, gdp, sh, sf, hp, ci, wpa, stint, ubr, war):
        self.player_id = player_id
        self.year = year
        self.team_id = team_id
        self.game_id = game_id
        self.league_id = league_id
        self.level_id = level_id
        self.split_id = split_id
        self.position = position
        self.ab = ab
        self.h = h
        self.k = k
        self.pa = pa
        self.pitches_seen = pitches_seen
        self.g = g
        self.gs = gs
        self.d = d
        self.t = t
        self.hr = hr
        self.r = r
        self.rbi = rbi
        self.sb = sb
        self.cs = cs
        self.bb = bb
        self.ibb = ibb
        self.gdp = gdp
        self.sh = sh
        self.sf = sf
        self.hp = hp
        self.ci = ci
        self.wpa = wpa
        self.stint = stint
        self.ubr = ubr
        self.war = war
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'game_id: {self.game_id}',
            f'league_id: {self.league_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'position: {self.position}',
            f'ab: {self.ab}',
            f'h: {self.h}',
            f'k: {self.k}',
            f'pa: {self.pa}',
            f'pitches_seen: {self.pitches_seen}',
            f'g: {self.g}',
            f'gs: {self.gs}',
            f'd: {self.d}',
            f't: {self.t}',
            f'hr: {self.hr}',
            f'r: {self.r}',
            f'rbi: {self.rbi}',
            f'sb: {self.sb}',
            f'cs: {self.cs}',
            f'bb: {self.bb}',
            f'ibb: {self.ibb}',
            f'gdp: {self.gdp}',
            f'sh: {self.sh}',
            f'sf: {self.sf}',
            f'hp: {self.hp}',
            f'ci: {self.ci}',
            f'wpa: {self.wpa}',
            f'stint: {self.stint}',
            f'ubr: {self.ubr}',
            f'war: {self.war}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersCareerBattingStatsEntry(*row)
        data.append(obj)

    return data
