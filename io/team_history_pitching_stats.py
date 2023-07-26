import pandas


class TeamHistoryPitchingStatsEntry:
    def __init__(self, team_id, year, league_id, sub_league_id, division_id, level_id, split_id, ab, ip, bf, tb, ha, k, rs, bb, r, er, gb, fb, pi, ipf, g, gs, w, l, s, sa, da, sh, sf, ta, hra, bk, ci, iw, wp, hp, gf, dp, qs, svo, bs, ra, cg, sho, sb, cs, hld, r9, avg, obp, slg, ops, h9, k9, hr9, bb9, cgp, fip, qsp, winp, rsg, svp, bsvp, gfp, era, pig, ws, whip, gbfbp, kbb, babip):
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.level_id = level_id
        self.split_id = split_id
        self.ab = ab
        self.ip = ip
        self.bf = bf
        self.tb = tb
        self.ha = ha
        self.k = k
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
        self.r9 = r9
        self.avg = avg
        self.obp = obp
        self.slg = slg
        self.ops = ops
        self.h9 = h9
        self.k9 = k9
        self.hr9 = hr9
        self.bb9 = bb9
        self.cgp = cgp
        self.fip = fip
        self.qsp = qsp
        self.winp = winp
        self.rsg = rsg
        self.svp = svp
        self.bsvp = bsvp
        self.gfp = gfp
        self.era = era
        self.pig = pig
        self.ws = ws
        self.whip = whip
        self.gbfbp = gbfbp
        self.kbb = kbb
        self.babip = babip
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'level_id: {self.level_id}',
            f'split_id: {self.split_id}',
            f'ab: {self.ab}',
            f'ip: {self.ip}',
            f'bf: {self.bf}',
            f'tb: {self.tb}',
            f'ha: {self.ha}',
            f'k: {self.k}',
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
            f'r9: {self.r9}',
            f'avg: {self.avg}',
            f'obp: {self.obp}',
            f'slg: {self.slg}',
            f'ops: {self.ops}',
            f'h9: {self.h9}',
            f'k9: {self.k9}',
            f'hr9: {self.hr9}',
            f'bb9: {self.bb9}',
            f'cgp: {self.cgp}',
            f'fip: {self.fip}',
            f'qsp: {self.qsp}',
            f'winp: {self.winp}',
            f'rsg: {self.rsg}',
            f'svp: {self.svp}',
            f'bsvp: {self.bsvp}',
            f'gfp: {self.gfp}',
            f'era: {self.era}',
            f'pig: {self.pig}',
            f'ws: {self.ws}',
            f'whip: {self.whip}',
            f'gbfbp: {self.gbfbp}',
            f'kbb: {self.kbb}',
            f'babip: {self.babip}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TeamHistoryPitchingStatsEntry(*row)
        data.append(obj)

    return data
