import pandas


class LeagueHistoryBattingStatsEntry:
    def __init__(self, year, team_id, game_id, league_id, level_id, split_id, pa, ab, h, k, tb, s, d, t, hr, sb, cs, rbi, r, bb, ibb, hp, sh, sf, ci, gdp, g, gs, ebh, pitches_seen, avg, obp, slg, rc, rc27, iso, woba, ops, sbp, kp, bbp, wpa, babip):
        self.year = year
        self.team_id = team_id
        self.game_id = game_id
        self.league_id = league_id
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
        self.woba = woba
        self.ops = ops
        self.sbp = sbp
        self.kp = kp
        self.bbp = bbp
        self.wpa = wpa
        self.babip = babip
    
    def __str__(self):
        return "\n".join([
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'game_id: {self.game_id}',
            f'league_id: {self.league_id}',
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
            f'woba: {self.woba}',
            f'ops: {self.ops}',
            f'sbp: {self.sbp}',
            f'kp: {self.kp}',
            f'bbp: {self.bbp}',
            f'wpa: {self.wpa}',
            f'babip: {self.babip}',
        ])



def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueHistoryBattingStatsEntry(*row)
        data.append(obj)

    return data
