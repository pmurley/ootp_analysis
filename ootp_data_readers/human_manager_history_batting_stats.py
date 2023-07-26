import pandas


class HumanManagerHistoryBattingStats:
    def __init__(self, human_manager_id, team_id, year, league_id, sub_league_id, division_id, level_id, split_id, pa, ab, h, k, tb, s, d, t, hr, sb, cs, rbi, r, bb, ibb, hp, sh, sf, ci, gdp, g, gs, ebh, pitches_seen, avg, obp, slg, rc, rc27, iso, tavg, woba, ops, sbp):
        self.human_manager_id = human_manager_id
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.level_id = level_id
        self.split_id = split_id
        self.pa = pa
        self.ab = ab
        self.h = h
        self.k = k
        self.tb = tb
        self.s = s
        self.d = d
        self.t = t
        self.hr = hr
        self.sb = sb
        self.cs = cs
        self.rbi = rbi
        self.r = r
        self.bb = bb
        self.ibb = ibb
        self.hp = hp
        self.sh = sh
        self.sf = sf
        self.ci = ci
        self.gdp = gdp
        self.g = g
        self.gs = gs
        self.ebh = ebh
        self.pitches_seen = pitches_seen
        self.avg = avg
        self.obp = obp
        self.slg = slg
        self.rc = rc
        self.rc27 = rc27
        self.iso = iso
        self.tavg = tavg
        self.woba = woba
        self.ops = ops
        self.sbp = sbp
    
    def __str__(self):
        return "\n".join([
            f'human_manager_id: {self.human_manager_id}',
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'pa: {self.pa}',
            f'ab: {self.ab}',
            f'h: {self.h}',
            f'k: {self.k}',
            f'tb: {self.tb}',
            f's: {self.s}',
            f'd: {self.d}',
            f't: {self.t}',
            f'hr: {self.hr}',
            f'sb: {self.sb}',
            f'cs: {self.cs}',
            f'rbi: {self.rbi}',
            f'r: {self.r}',
            f'bb: {self.bb}',
            f'ibb: {self.ibb}',
            f'hp: {self.hp}',
            f'sh: {self.sh}',
            f'sf: {self.sf}',
            f'ci: {self.ci}',
            f'gdp: {self.gdp}',
            f'g: {self.g}',
            f'gs: {self.gs}',
            f'ebh: {self.ebh}',
            f'pitches_seen: {self.pitches_seen}',
            f'avg: {self.avg}',
            f'obp: {self.obp}',
            f'slg: {self.slg}',
            f'rc: {self.rc}',
            f'rc27: {self.rc27}',
            f'iso: {self.iso}',
            f'tavg: {self.tavg}',
            f'woba: {self.woba}',
            f'ops: {self.ops}',
            f'sbp: {self.sbp}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = HumanManagerHistoryBattingStats(*row)
        data.append(obj)

    return data
