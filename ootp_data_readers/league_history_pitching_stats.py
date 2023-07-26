import pandas


class LeagueHistoryPitchingStatsEntry:
    def __init__(self, year, team_id, game_id, league_id, level_id, split_id, ab, ip, bf, tb, ha, k, rs, bb, r, er, gb, fb, pi, ipf, g, gs, w, l, s, sa, da, sh, sf, ta, hra, bk, ci, iw, wp, hp, gf, dp, qs, svo, bs, ra, ir, irs, cg, sho, sb, cs, hld, r9, avg, obp, slg, ops, h9, k9, kp, bbp, kbbp, hr9, bb9, cgp, fip, qsp, winp, rsg, svp, bsvp, irsp, gfp, era, pig, ws, whip, gbfbp, kbb, babip, wpa, war, ra9war, sd, md):
        self.year = year
        self.team_id = team_id
        self.game_id = game_id
        self.league_id = league_id
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
        self.ir = ir
        self.irs = irs
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
        self.kp = kp
        self.bbp = bbp
        self.kbbp = kbbp
        self.hr9 = hr9
        self.bb9 = bb9
        self.cgp = cgp
        self.fip = fip
        self.qsp = qsp
        self.winp = winp
        self.rsg = rsg
        self.svp = svp
        self.bsvp = bsvp
        self.irsp = irsp
        self.gfp = gfp
        self.era = era
        self.pig = pig
        self.ws = ws
        self.whip = whip
        self.gbfbp = gbfbp
        self.kbb = kbb
        self.babip = babip
        self.wpa = wpa
        self.war = war
        self.ra9war = ra9war
        self.sd = sd
        self.md = md
    
    def __str__(self):
        return "\n".join([
            f'year: {self.year}',
            f'team_id: {self.team_id}',
            f'game_id: {self.game_id}',
            f'league_id: {self.league_id}',
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
            f'ir: {self.ir}',
            f'irs: {self.irs}',
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
            f'kp: {self.kp}',
            f'bbp: {self.bbp}',
            f'kbbp: {self.kbbp}',
            f'hr9: {self.hr9}',
            f'bb9: {self.bb9}',
            f'cgp: {self.cgp}',
            f'fip: {self.fip}',
            f'qsp: {self.qsp}',
            f'winp: {self.winp}',
            f'rsg: {self.rsg}',
            f'svp: {self.svp}',
            f'bsvp: {self.bsvp}',
            f'irsp: {self.irsp}',
            f'gfp: {self.gfp}',
            f'era: {self.era}',
            f'pig: {self.pig}',
            f'ws: {self.ws}',
            f'whip: {self.whip}',
            f'gbfbp: {self.gbfbp}',
            f'kbb: {self.kbb}',
            f'babip: {self.babip}',
            f'wpa: {self.wpa}',
            f'war: {self.war}',
            f'ra9war: {self.ra9war}',
            f'sd: {self.sd}',
            f'md: {self.md}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueHistoryPitchingStatsEntry(*row)
        data.append(obj)

    return data
