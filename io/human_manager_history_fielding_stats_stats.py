import pandas


class HumanManagerHistoryFieldingStats:
    def __init__(self, human_manager_id, team_id, year, league_id, sub_league_id, division_id, level_id, split_id, position, g, gs, tc, a, po, e, dp, tp, pb, sba, rto, er, ip, ipf, pct, range, rtop, cera):
        self.human_manager_id = human_manager_id
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
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
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = HumanManagerHistoryFieldingStats(*row)
        data.append(obj)

    return data
