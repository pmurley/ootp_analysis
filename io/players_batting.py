import pandas


class PlayersBattingEntry:
    def __init__(self, player_id, team_id, league_id, position, role, batting_ratings_overall_contact, batting_ratings_overall_gap, batting_ratings_overall_eye, batting_ratings_overall_strikeouts, batting_ratings_overall_hp, batting_ratings_overall_power, batting_ratings_overall_babip, batting_ratings_vsr_contact, batting_ratings_vsr_gap, batting_ratings_vsr_eye, batting_ratings_vsr_strikeouts, batting_ratings_vsr_hp, batting_ratings_vsr_power, batting_ratings_vsr_babip, batting_ratings_vsl_contact, batting_ratings_vsl_gap, batting_ratings_vsl_eye, batting_ratings_vsl_strikeouts, batting_ratings_vsl_hp, batting_ratings_vsl_power, batting_ratings_vsl_babip, batting_ratings_talent_contact, batting_ratings_talent_gap, batting_ratings_talent_eye, batting_ratings_talent_strikeouts, batting_ratings_talent_hp, batting_ratings_talent_power, batting_ratings_talent_babip, batting_ratings_misc_bunt, batting_ratings_misc_bunt_for_hit, batting_ratings_misc_gb_hitter_type, batting_ratings_misc_fb_hitter_type):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.batting_ratings_overall_contact = batting_ratings_overall_contact
        self.batting_ratings_overall_gap = batting_ratings_overall_gap
        self.batting_ratings_overall_eye = batting_ratings_overall_eye
        self.batting_ratings_overall_strikeouts = batting_ratings_overall_strikeouts
        self.batting_ratings_overall_hp = batting_ratings_overall_hp
        self.batting_ratings_overall_power = batting_ratings_overall_power
        self.batting_ratings_overall_babip = batting_ratings_overall_babip
        self.batting_ratings_vsr_contact = batting_ratings_vsr_contact
        self.batting_ratings_vsr_gap = batting_ratings_vsr_gap
        self.batting_ratings_vsr_eye = batting_ratings_vsr_eye
        self.batting_ratings_vsr_strikeouts = batting_ratings_vsr_strikeouts
        self.batting_ratings_vsr_hp = batting_ratings_vsr_hp
        self.batting_ratings_vsr_power = batting_ratings_vsr_power
        self.batting_ratings_vsr_babip = batting_ratings_vsr_babip
        self.batting_ratings_vsl_contact = batting_ratings_vsl_contact
        self.batting_ratings_vsl_gap = batting_ratings_vsl_gap
        self.batting_ratings_vsl_eye = batting_ratings_vsl_eye
        self.batting_ratings_vsl_strikeouts = batting_ratings_vsl_strikeouts
        self.batting_ratings_vsl_hp = batting_ratings_vsl_hp
        self.batting_ratings_vsl_power = batting_ratings_vsl_power
        self.batting_ratings_vsl_babip = batting_ratings_vsl_babip
        self.batting_ratings_talent_contact = batting_ratings_talent_contact
        self.batting_ratings_talent_gap = batting_ratings_talent_gap
        self.batting_ratings_talent_eye = batting_ratings_talent_eye
        self.batting_ratings_talent_strikeouts = batting_ratings_talent_strikeouts
        self.batting_ratings_talent_hp = batting_ratings_talent_hp
        self.batting_ratings_talent_power = batting_ratings_talent_power
        self.batting_ratings_talent_babip = batting_ratings_talent_babip
        self.batting_ratings_misc_bunt = batting_ratings_misc_bunt
        self.batting_ratings_misc_bunt_for_hit = batting_ratings_misc_bunt_for_hit
        self.batting_ratings_misc_gb_hitter_type = batting_ratings_misc_gb_hitter_type
        self.batting_ratings_misc_fb_hitter_type = batting_ratings_misc_fb_hitter_type
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'batting_ratings_overall_contact: {self.batting_ratings_overall_contact}',
            f'batting_ratings_overall_gap: {self.batting_ratings_overall_gap}',
            f'batting_ratings_overall_eye: {self.batting_ratings_overall_eye}',
            f'batting_ratings_overall_strikeouts: {self.batting_ratings_overall_strikeouts}',
            f'batting_ratings_overall_hp: {self.batting_ratings_overall_hp}',
            f'batting_ratings_overall_power: {self.batting_ratings_overall_power}',
            f'batting_ratings_overall_babip: {self.batting_ratings_overall_babip}',
            f'batting_ratings_vsr_contact: {self.batting_ratings_vsr_contact}',
            f'batting_ratings_vsr_gap: {self.batting_ratings_vsr_gap}',
            f'batting_ratings_vsr_eye: {self.batting_ratings_vsr_eye}',
            f'batting_ratings_vsr_strikeouts: {self.batting_ratings_vsr_strikeouts}',
            f'batting_ratings_vsr_hp: {self.batting_ratings_vsr_hp}',
            f'batting_ratings_vsr_power: {self.batting_ratings_vsr_power}',
            f'batting_ratings_vsr_babip: {self.batting_ratings_vsr_babip}',
            f'batting_ratings_vsl_contact: {self.batting_ratings_vsl_contact}',
            f'batting_ratings_vsl_gap: {self.batting_ratings_vsl_gap}',
            f'batting_ratings_vsl_eye: {self.batting_ratings_vsl_eye}',
            f'batting_ratings_vsl_strikeouts: {self.batting_ratings_vsl_strikeouts}',
            f'batting_ratings_vsl_hp: {self.batting_ratings_vsl_hp}',
            f'batting_ratings_vsl_power: {self.batting_ratings_vsl_power}',
            f'batting_ratings_vsl_babip: {self.batting_ratings_vsl_babip}',
            f'batting_ratings_talent_contact: {self.batting_ratings_talent_contact}',
            f'batting_ratings_talent_gap: {self.batting_ratings_talent_gap}',
            f'batting_ratings_talent_eye: {self.batting_ratings_talent_eye}',
            f'batting_ratings_talent_strikeouts: {self.batting_ratings_talent_strikeouts}',
            f'batting_ratings_talent_hp: {self.batting_ratings_talent_hp}',
            f'batting_ratings_talent_power: {self.batting_ratings_talent_power}',
            f'batting_ratings_talent_babip: {self.batting_ratings_talent_babip}',
            f'batting_ratings_misc_bunt: {self.batting_ratings_misc_bunt}',
            f'batting_ratings_misc_bunt_for_hit: {self.batting_ratings_misc_bunt_for_hit}',
            f'batting_ratings_misc_gb_hitter_type: {self.batting_ratings_misc_gb_hitter_type}',
            f'batting_ratings_misc_fb_hitter_type: {self.batting_ratings_misc_fb_hitter_type}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = PlayersBattingEntry(*row)
        data[obj.player_id] = obj

    return data
