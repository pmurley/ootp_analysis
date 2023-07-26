import pandas


class PlayersValueEntry:
    def __init__(self, player_id, team_id, league_id, position, role, offensive_value, offensive_value_talent, offensive_value_vsl, offensive_value_vsr, pitching_value, pitching_value_talent, pitching_value_vsl, pitching_value_vsr, overall_value, talent_value, career_value, leadoff_value_vsl, leadoff_value_vsr, running_value, stealing_value, season_performance, stats_value_0, stats_value_1, stats_value_2, stats_mod_0, stats_mod_1, stats_mod_2, ratings_value, overall_sp, overall_rp, overall_c, overall_1b, overall_2b, overall_3b, overall_ss, overall_lf, overall_cf, overall_rf, award_bat, award_pit, award_field, oa, pot):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.offensive_value = offensive_value
        self.offensive_value_talent = offensive_value_talent
        self.offensive_value_vsl = offensive_value_vsl
        self.offensive_value_vsr = offensive_value_vsr
        self.pitching_value = pitching_value
        self.pitching_value_talent = pitching_value_talent
        self.pitching_value_vsl = pitching_value_vsl
        self.pitching_value_vsr = pitching_value_vsr
        self.overall_value = overall_value
        self.talent_value = talent_value
        self.career_value = career_value
        self.leadoff_value_vsl = leadoff_value_vsl
        self.leadoff_value_vsr = leadoff_value_vsr
        self.running_value = running_value
        self.stealing_value = stealing_value
        self.season_performance = season_performance
        self.stats_value_0 = stats_value_0
        self.stats_value_1 = stats_value_1
        self.stats_value_2 = stats_value_2
        self.stats_mod_0 = stats_mod_0
        self.stats_mod_1 = stats_mod_1
        self.stats_mod_2 = stats_mod_2
        self.ratings_value = ratings_value
        self.overall_sp = overall_sp
        self.overall_rp = overall_rp
        self.overall_c = overall_c
        self.overall_1b = overall_1b
        self.overall_2b = overall_2b
        self.overall_3b = overall_3b
        self.overall_ss = overall_ss
        self.overall_lf = overall_lf
        self.overall_cf = overall_cf
        self.overall_rf = overall_rf
        self.award_bat = award_bat
        self.award_pit = award_pit
        self.award_field = award_field
        self.oa = oa
        self.pot = pot
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'offensive_value: {self.offensive_value}',
            f'offensive_value_talent: {self.offensive_value_talent}',
            f'offensive_value_vsl: {self.offensive_value_vsl}',
            f'offensive_value_vsr: {self.offensive_value_vsr}',
            f'pitching_value: {self.pitching_value}',
            f'pitching_value_talent: {self.pitching_value_talent}',
            f'pitching_value_vsl: {self.pitching_value_vsl}',
            f'pitching_value_vsr: {self.pitching_value_vsr}',
            f'overall_value: {self.overall_value}',
            f'talent_value: {self.talent_value}',
            f'career_value: {self.career_value}',
            f'leadoff_value_vsl: {self.leadoff_value_vsl}',
            f'leadoff_value_vsr: {self.leadoff_value_vsr}',
            f'running_value: {self.running_value}',
            f'stealing_value: {self.stealing_value}',
            f'season_performance: {self.season_performance}',
            f'stats_value_0: {self.stats_value_0}',
            f'stats_value_1: {self.stats_value_1}',
            f'stats_value_2: {self.stats_value_2}',
            f'stats_mod_0: {self.stats_mod_0}',
            f'stats_mod_1: {self.stats_mod_1}',
            f'stats_mod_2: {self.stats_mod_2}',
            f'ratings_value: {self.ratings_value}',
            f'overall_sp: {self.overall_sp}',
            f'overall_rp: {self.overall_rp}',
            f'overall_c: {self.overall_c}',
            f'overall_1b: {self.overall_1b}',
            f'overall_2b: {self.overall_2b}',
            f'overall_3b: {self.overall_3b}',
            f'overall_ss: {self.overall_ss}',
            f'overall_lf: {self.overall_lf}',
            f'overall_cf: {self.overall_cf}',
            f'overall_rf: {self.overall_rf}',
            f'award_bat: {self.award_bat}',
            f'award_pit: {self.award_pit}',
            f'award_field: {self.award_field}',
            f'oa: {self.oa}',
            f'pot: {self.pot}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = PlayersValueEntry(*row)
        data[obj.player_id] = obj

    return data
