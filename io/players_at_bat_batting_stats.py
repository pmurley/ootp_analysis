import pandas


class PlayersAtBatBattingStatsEntry:
    def __init__(self, player_id, game_id, opponent_player_id, team_id, sac, balls, strikes, result, base1, base2, base3, Close, pinch, inning, run_diff, outs, sb, cs, rbi, r, spot, hit_loc, hit_xy, exit_velo, launch_angle):
        self.player_id = player_id
        self.game_id = game_id
        self.opponent_player_id = opponent_player_id
        self.team_id = team_id
        self.sac = sac
        self.balls = balls
        self.strikes = strikes
        self.result = result
        self.base1 = base1
        self.base2 = base2
        self.base3 = base3
        self.Close = Close
        self.pinch = pinch
        self.inning = inning
        self.run_diff = run_diff
        self.outs = outs
        self.sb = sb
        self.cs = cs
        self.rbi = rbi
        self.r = r
        self.spot = spot
        self.hit_loc = hit_loc
        self.hit_xy = hit_xy
        self.exit_velo = exit_velo
        self.launch_angle = launch_angle
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'game_id: {self.game_id}',
            f'opponent_player_id: {self.opponent_player_id}',
            f'team_id: {self.team_id}',
            f'sac: {self.sac}',
            f'balls: {self.balls}',
            f'strikes: {self.strikes}',
            f'result: {self.result}',
            f'base1: {self.base1}',
            f'base2: {self.base2}',
            f'base3: {self.base3}',
            f'Close: {self.Close}',
            f'pinch: {self.pinch}',
            f'inning: {self.inning}',
            f'run_diff: {self.run_diff}',
            f'outs: {self.outs}',
            f'sb: {self.sb}',
            f'cs: {self.cs}',
            f'rbi: {self.rbi}',
            f'r: {self.r}',
            f'spot: {self.spot}',
            f'hit_loc: {self.hit_loc}',
            f'hit_xy: {self.hit_xy}',
            f'exit_velo: {self.exit_velo}',
            f'launch_angle: {self.launch_angle}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersAtBatBattingStatsEntry(*row)
        data.append(obj)

    return data
