import pandas


class PlayersRosterStatusEntry:
    def __init__(self, player_id, team_id, league_id, position, role, playing_level, is_active, is_on_secondary, is_on_dl, is_on_dl60, must_be_active, just_signed, was_on_active, was_on_secondary, was_on_dl, mlb_service_years, secondary_service_years, pro_service_years, mlb_service_days, secondary_service_days, pro_service_days, mlb_service_days_this_year, secondary_service_days_this_year, pro_service_days_this_year, dl_days_this_year, years_protected_from_rule_5, is_on_waivers, designated_for_assignment, irrevocable_waivers, days_on_waivers, days_on_waivers_left, days_on_dfa_left, claimed_team_id, options_used, options_used_this_year, has_received_arbitration, was_traded, trade_status):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.playing_level = playing_level
        self.is_active = is_active
        self.is_on_secondary = is_on_secondary
        self.is_on_dl = is_on_dl
        self.is_on_dl60 = is_on_dl60
        self.must_be_active = must_be_active
        self.just_signed = just_signed
        self.was_on_active = was_on_active
        self.was_on_secondary = was_on_secondary
        self.was_on_dl = was_on_dl
        self.mlb_service_years = mlb_service_years
        self.secondary_service_years = secondary_service_years
        self.pro_service_years = pro_service_years
        self.mlb_service_days = mlb_service_days
        self.secondary_service_days = secondary_service_days
        self.pro_service_days = pro_service_days
        self.mlb_service_days_this_year = mlb_service_days_this_year
        self.secondary_service_days_this_year = secondary_service_days_this_year
        self.pro_service_days_this_year = pro_service_days_this_year
        self.dl_days_this_year = dl_days_this_year
        self.years_protected_from_rule_5 = years_protected_from_rule_5
        self.is_on_waivers = is_on_waivers
        self.designated_for_assignment = designated_for_assignment
        self.irrevocable_waivers = irrevocable_waivers
        self.days_on_waivers = days_on_waivers
        self.days_on_waivers_left = days_on_waivers_left
        self.days_on_dfa_left = days_on_dfa_left
        self.claimed_team_id = claimed_team_id
        self.options_used = options_used
        self.options_used_this_year = options_used_this_year
        self.has_received_arbitration = has_received_arbitration
        self.was_traded = was_traded
        self.trade_status = trade_status
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'playing_level: {self.playing_level}',
            f'is_active: {self.is_active}',
            f'is_on_secondary: {self.is_on_secondary}',
            f'is_on_dl: {self.is_on_dl}',
            f'is_on_dl60: {self.is_on_dl60}',
            f'must_be_active: {self.must_be_active}',
            f'just_signed: {self.just_signed}',
            f'was_on_active: {self.was_on_active}',
            f'was_on_secondary: {self.was_on_secondary}',
            f'was_on_dl: {self.was_on_dl}',
            f'mlb_service_years: {self.mlb_service_years}',
            f'secondary_service_years: {self.secondary_service_years}',
            f'pro_service_years: {self.pro_service_years}',
            f'mlb_service_days: {self.mlb_service_days}',
            f'secondary_service_days: {self.secondary_service_days}',
            f'pro_service_days: {self.pro_service_days}',
            f'mlb_service_days_this_year: {self.mlb_service_days_this_year}',
            f'secondary_service_days_this_year: {self.secondary_service_days_this_year}',
            f'pro_service_days_this_year: {self.pro_service_days_this_year}',
            f'dl_days_this_year: {self.dl_days_this_year}',
            f'years_protected_from_rule_5: {self.years_protected_from_rule_5}',
            f'is_on_waivers: {self.is_on_waivers}',
            f'designated_for_assignment: {self.designated_for_assignment}',
            f'irrevocable_waivers: {self.irrevocable_waivers}',
            f'days_on_waivers: {self.days_on_waivers}',
            f'days_on_waivers_left: {self.days_on_waivers_left}',
            f'days_on_dfa_left: {self.days_on_dfa_left}',
            f'claimed_team_id: {self.claimed_team_id}',
            f'options_used: {self.options_used}',
            f'options_used_this_year: {self.options_used_this_year}',
            f'has_received_arbitration: {self.has_received_arbitration}',
            f'was_traded: {self.was_traded}',
            f'trade_status: {self.trade_status}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = PlayersRosterStatusEntry(*row)
        data[obj.player_id] = obj

    return data
