import pandas


class PlayersGamePitchingStatsEntry:
    def __init__(self, player_id, year, team_id, game_id, league_id, level_id, split_id, ip, ab, tb, ha, k, bf, rs, bb, r, er, gb, fb, pi, ipf, g, gs, w, l, s, sa, da, sh, sf, ta, hra, bk, ci, iw, wp, hp, gf, dp, qs, svo, bs, ra, cg, sho, sb, cs, hld, ir, irs, wpa, li, stint, outs, sd, md):
        self.player_id = player_id
        self.year = year
        self.team_id = team_id
        self.game_id = game_id
        self.league_id = league_id
        self.level_id = level_id
        self.split_id = split_id
        self.ip = ip
        self.ab = ab
        self.tb = tb
        self.ha = ha
        self.k = k
        self.bf = bf
        self.rs = rs
        self.bb = bb
        self.r = r
        self.er = er
        self.gb = gb
        self.fb = fb
        self.pi = pi
        self.ipf = ipf
        self.g = g
        self.gs = gs
        self.w = w
        self.l = l
        self.s = s
        self.sa = sa
        self.da = da
        self.sh = sh
        self.sf = sf
        self.ta = ta
        self.hra = hra
        self.bk = bk
        self.ci = ci
        self.iw = iw
        self.wp = wp
        self.hp = hp
        self.gf = gf
        self.dp = dp
        self.qs = qs
        self.svo = svo
        self.bs = bs
        self.ra = ra
        self.cg = cg
        self.sho = sho
        self.sb = sb
        self.cs = cs
        self.hld = hld
        self.ir = ir
        self.irs = irs
        self.wpa = wpa
        self.li = li
        self.stint = stint
        self.outs = outs
        self.sd = sd
        self.md = md
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'game_id: {self.game_id}',
            f'league_id: {self.league_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'ip: {self.ip}',
            f'ab: {self.ab}',
            f'tb: {self.tb}',
            f'ha: {self.ha}',
            f'k: {self.k}',
            f'bf: {self.bf}',
            f'rs: {self.rs}',
            f'bb: {self.bb}',
            f'r: {self.r}',
            f'er: {self.er}',
            f'gb: {self.gb}',
            f'fb: {self.fb}',
            f'pi: {self.pi}',
            f'ipf: {self.ipf}',
            f'g: {self.g}',
            f'gs: {self.gs}',
            f'w: {self.w}',
            f'l: {self.l}',
            f's: {self.s}',
            f'sa: {self.sa}',
            f'da: {self.da}',
            f'sh: {self.sh}',
            f'sf: {self.sf}',
            f'ta: {self.ta}',
            f'hra: {self.hra}',
            f'bk: {self.bk}',
            f'ci: {self.ci}',
            f'iw: {self.iw}',
            f'wp: {self.wp}',
            f'hp: {self.hp}',
            f'gf: {self.gf}',
            f'dp: {self.dp}',
            f'qs: {self.qs}',
            f'svo: {self.svo}',
            f'bs: {self.bs}',
            f'ra: {self.ra}',
            f'cg: {self.cg}',
            f'sho: {self.sho}',
            f'sb: {self.sb}',
            f'cs: {self.cs}',
            f'hld: {self.hld}',
            f'ir: {self.ir}',
            f'irs: {self.irs}',
            f'wpa: {self.wpa}',
            f'li: {self.li}',
            f'stint: {self.stint}',
            f'outs: {self.outs}',
            f'sd: {self.sd}',
            f'md: {self.md}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersGamePitchingStatsEntry(*row)
        data.append(obj)

    return data
