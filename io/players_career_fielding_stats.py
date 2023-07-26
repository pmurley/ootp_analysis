import pandas


class PlayersCareerFieldingStatsEntry:
    def __init__(self, player_id, year, team_id, league_id, level_id, split_id, position, tc, a, po, er, ip, g, gs, e, dp, tp, pb, sba, rto, ipf, plays, plays_base, roe, opps_0, opps_made_0, opps_1, opps_made_1, opps_2, opps_made_2, opps_3, opps_made_3, opps_4, opps_made_4, opps_5, opps_made_5, framing, arm, zr):
        self.player_id = player_id
        self.year = year
        self.team_id = team_id
        self.league_id = league_id
        self.level_id = level_id
        self.split_id = split_id
        self.position = position
        self.tc = tc
        self.a = a
        self.po = po
        self.er = er
        self.ip = ip
        self.g = g
        self.gs = gs
        self.e = e
        self.dp = dp
        self.tp = tp
        self.pb = pb
        self.sba = sba
        self.rto = rto
        self.ipf = ipf
        self.plays = plays
        self.plays_base = plays_base
        self.roe = roe
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
        self.zr = zr
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'position: {self.position}',
            f'tc: {self.tc}',
            f'a: {self.a}',
            f'po: {self.po}',
            f'er: {self.er}',
            f'ip: {self.ip}',
            f'g: {self.g}',
            f'gs: {self.gs}',
            f'e: {self.e}',
            f'dp: {self.dp}',
            f'tp: {self.tp}',
            f'pb: {self.pb}',
            f'sba: {self.sba}',
            f'rto: {self.rto}',
            f'ipf: {self.ipf}',
            f'plays: {self.plays}',
            f'plays_base: {self.plays_base}',
            f'roe: {self.roe}',
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
            f'zr: {self.zr}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersCareerFieldingStatsEntry(*row)
        data.append(obj)

    return data
