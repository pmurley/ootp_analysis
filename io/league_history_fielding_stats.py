import pandas


class LeagueHistoryFieldingStatsEntry:
    def __init__(self, year, team_id, league_id, sub_league_id, level_id, split_id, position, g, gs, tc, a, po, e, dp, tp, pb, sba, rto, er, ip, ipf, pct, range, rtop, cera, zr, plays, plays_base, roe, eff, opps_0, opps_made_0, opps_1, opps_made_1, opps_2, opps_made_2, opps_3, opps_made_3, opps_4, opps_made_4, opps_5, opps_made_5, framing, arm):
        self.year = year
        self.team_id = team_id
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.level_id = level_id
        self.split_id = split_id
        self.position = position
        self.g = g
        self.gs = gs
        self.tc = tc
        self.a = a
        self.po = po
        self.e = e
        self.dp = dp
        self.tp = tp
        self.pb = pb
        self.sba = sba
        self.rto = rto
        self.er = er
        self.ip = ip
        self.ipf = ipf
        self.pct = pct
        self.range = range
        self.rtop = rtop
        self.cera = cera
        self.zr = zr
        self.plays = plays
        self.plays_base = plays_base
        self.roe = roe
        self.eff = eff
        self.opps_0 = opps_0
        self.opps_made_0 = opps_made_0
        self.opps_1 = opps_1
        self.opps_made_1 = opps_made_1
        self.opps_2 = opps_2
        self.opps_made_2 = opps_made_2
        self.opps_3 = opps_3
        self.opps_made_3 = opps_made_3
        self.opps_4 = opps_4
        self.opps_made_4 = opps_made_4
        self.opps_5 = opps_5
        self.opps_made_5 = opps_made_5
        self.framing = framing
        self.arm = arm
    
    def __str__(self):
        return "\n".join([
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'position: {self.position}',
            f'g: {self.g}',
            f'gs: {self.gs}',
            f'tc: {self.tc}',
            f'a: {self.a}',
            f'po: {self.po}',
            f'e: {self.e}',
            f'dp: {self.dp}',
            f'tp: {self.tp}',
            f'pb: {self.pb}',
            f'sba: {self.sba}',
            f'rto: {self.rto}',
            f'er: {self.er}',
            f'ip: {self.ip}',
            f'ipf: {self.ipf}',
            f'pct: {self.pct}',
            f'range: {self.range}',
            f'rtop: {self.rtop}',
            f'cera: {self.cera}',
            f'zr: {self.zr}',
            f'plays: {self.plays}',
            f'plays_base: {self.plays_base}',
            f'roe: {self.roe}',
            f'eff: {self.eff}',
            f'opps_0: {self.opps_0}',
            f'opps_made_0: {self.opps_made_0}',
            f'opps_1: {self.opps_1}',
            f'opps_made_1: {self.opps_made_1}',
            f'opps_2: {self.opps_2}',
            f'opps_made_2: {self.opps_made_2}',
            f'opps_3: {self.opps_3}',
            f'opps_made_3: {self.opps_made_3}',
            f'opps_4: {self.opps_4}',
            f'opps_made_4: {self.opps_made_4}',
            f'opps_5: {self.opps_5}',
            f'opps_made_5: {self.opps_made_5}',
            f'framing: {self.framing}',
            f'arm: {self.arm}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueHistoryFieldingStatsEntry(*row)
        data.append(obj)

    return data
