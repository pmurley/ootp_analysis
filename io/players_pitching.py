import pandas


class PlayersPitchingEntry:
    def __init__(self, player_id, team_id, league_id, position, role, pitching_ratings_overall_stuff, pitching_ratings_overall_control, pitching_ratings_overall_movement, pitching_ratings_overall_balk, pitching_ratings_overall_hp, pitching_ratings_overall_wild_pitch, pitching_ratings_vsr_stuff, pitching_ratings_vsr_control, pitching_ratings_vsr_movement, pitching_ratings_vsr_balk, pitching_ratings_vsr_hp, pitching_ratings_vsr_wild_pitch, pitching_ratings_vsl_stuff, pitching_ratings_vsl_control, pitching_ratings_vsl_movement, pitching_ratings_vsl_balk, pitching_ratings_vsl_hp, pitching_ratings_vsl_wild_pitch, pitching_ratings_talent_stuff, pitching_ratings_talent_control, pitching_ratings_talent_movement, pitching_ratings_talent_balk, pitching_ratings_talent_hp, pitching_ratings_talent_wild_pitch, pitching_ratings_pitches_fastball, pitching_ratings_pitches_slider, pitching_ratings_pitches_curveball, pitching_ratings_pitches_screwball, pitching_ratings_pitches_forkball, pitching_ratings_pitches_changeup, pitching_ratings_pitches_sinker, pitching_ratings_pitches_splitter, pitching_ratings_pitches_knuckleball, pitching_ratings_pitches_cutter, pitching_ratings_pitches_circlechange, pitching_ratings_pitches_knucklecurve, pitching_ratings_pitches_talent_fastball, pitching_ratings_pitches_talent_slider, pitching_ratings_pitches_talent_curveball, pitching_ratings_pitches_talent_screwball, pitching_ratings_pitches_talent_forkball, pitching_ratings_pitches_talent_changeup, pitching_ratings_pitches_talent_sinker, pitching_ratings_pitches_talent_splitter, pitching_ratings_pitches_talent_knuckleball, pitching_ratings_pitches_talent_cutter, pitching_ratings_pitches_talent_circlechange, pitching_ratings_pitches_talent_knucklecurve, pitching_ratings_misc_velocity, pitching_ratings_misc_arm_slot, pitching_ratings_misc_stamina, pitching_ratings_misc_ground_fly, pitching_ratings_misc_hold, pitching_ratings_babip):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.pitching_ratings_overall_stuff = pitching_ratings_overall_stuff
        self.pitching_ratings_overall_control = pitching_ratings_overall_control
        self.pitching_ratings_overall_movement = pitching_ratings_overall_movement
        self.pitching_ratings_overall_balk = pitching_ratings_overall_balk
        self.pitching_ratings_overall_hp = pitching_ratings_overall_hp
        self.pitching_ratings_overall_wild_pitch = pitching_ratings_overall_wild_pitch
        self.pitching_ratings_vsr_stuff = pitching_ratings_vsr_stuff
        self.pitching_ratings_vsr_control = pitching_ratings_vsr_control
        self.pitching_ratings_vsr_movement = pitching_ratings_vsr_movement
        self.pitching_ratings_vsr_balk = pitching_ratings_vsr_balk
        self.pitching_ratings_vsr_hp = pitching_ratings_vsr_hp
        self.pitching_ratings_vsr_wild_pitch = pitching_ratings_vsr_wild_pitch
        self.pitching_ratings_vsl_stuff = pitching_ratings_vsl_stuff
        self.pitching_ratings_vsl_control = pitching_ratings_vsl_control
        self.pitching_ratings_vsl_movement = pitching_ratings_vsl_movement
        self.pitching_ratings_vsl_balk = pitching_ratings_vsl_balk
        self.pitching_ratings_vsl_hp = pitching_ratings_vsl_hp
        self.pitching_ratings_vsl_wild_pitch = pitching_ratings_vsl_wild_pitch
        self.pitching_ratings_talent_stuff = pitching_ratings_talent_stuff
        self.pitching_ratings_talent_control = pitching_ratings_talent_control
        self.pitching_ratings_talent_movement = pitching_ratings_talent_movement
        self.pitching_ratings_talent_balk = pitching_ratings_talent_balk
        self.pitching_ratings_talent_hp = pitching_ratings_talent_hp
        self.pitching_ratings_talent_wild_pitch = pitching_ratings_talent_wild_pitch
        self.pitching_ratings_pitches_fastball = pitching_ratings_pitches_fastball
        self.pitching_ratings_pitches_slider = pitching_ratings_pitches_slider
        self.pitching_ratings_pitches_curveball = pitching_ratings_pitches_curveball
        self.pitching_ratings_pitches_screwball = pitching_ratings_pitches_screwball
        self.pitching_ratings_pitches_forkball = pitching_ratings_pitches_forkball
        self.pitching_ratings_pitches_changeup = pitching_ratings_pitches_changeup
        self.pitching_ratings_pitches_sinker = pitching_ratings_pitches_sinker
        self.pitching_ratings_pitches_splitter = pitching_ratings_pitches_splitter
        self.pitching_ratings_pitches_knuckleball = pitching_ratings_pitches_knuckleball
        self.pitching_ratings_pitches_cutter = pitching_ratings_pitches_cutter
        self.pitching_ratings_pitches_circlechange = pitching_ratings_pitches_circlechange
        self.pitching_ratings_pitches_knucklecurve = pitching_ratings_pitches_knucklecurve
        self.pitching_ratings_pitches_talent_fastball = pitching_ratings_pitches_talent_fastball
        self.pitching_ratings_pitches_talent_slider = pitching_ratings_pitches_talent_slider
        self.pitching_ratings_pitches_talent_curveball = pitching_ratings_pitches_talent_curveball
        self.pitching_ratings_pitches_talent_screwball = pitching_ratings_pitches_talent_screwball
        self.pitching_ratings_pitches_talent_forkball = pitching_ratings_pitches_talent_forkball
        self.pitching_ratings_pitches_talent_changeup = pitching_ratings_pitches_talent_changeup
        self.pitching_ratings_pitches_talent_sinker = pitching_ratings_pitches_talent_sinker
        self.pitching_ratings_pitches_talent_splitter = pitching_ratings_pitches_talent_splitter
        self.pitching_ratings_pitches_talent_knuckleball = pitching_ratings_pitches_talent_knuckleball
        self.pitching_ratings_pitches_talent_cutter = pitching_ratings_pitches_talent_cutter
        self.pitching_ratings_pitches_talent_circlechange = pitching_ratings_pitches_talent_circlechange
        self.pitching_ratings_pitches_talent_knucklecurve = pitching_ratings_pitches_talent_knucklecurve
        self.pitching_ratings_misc_velocity = pitching_ratings_misc_velocity
        self.pitching_ratings_misc_arm_slot = pitching_ratings_misc_arm_slot
        self.pitching_ratings_misc_stamina = pitching_ratings_misc_stamina
        self.pitching_ratings_misc_ground_fly = pitching_ratings_misc_ground_fly
        self.pitching_ratings_misc_hold = pitching_ratings_misc_hold
        self.pitching_ratings_babip = pitching_ratings_babip
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'pitching_ratings_overall_stuff: {self.pitching_ratings_overall_stuff}',
            f'pitching_ratings_overall_control: {self.pitching_ratings_overall_control}',
            f'pitching_ratings_overall_movement: {self.pitching_ratings_overall_movement}',
            f'pitching_ratings_overall_balk: {self.pitching_ratings_overall_balk}',
            f'pitching_ratings_overall_hp: {self.pitching_ratings_overall_hp}',
            f'pitching_ratings_overall_wild_pitch: {self.pitching_ratings_overall_wild_pitch}',
            f'pitching_ratings_vsr_stuff: {self.pitching_ratings_vsr_stuff}',
            f'pitching_ratings_vsr_control: {self.pitching_ratings_vsr_control}',
            f'pitching_ratings_vsr_movement: {self.pitching_ratings_vsr_movement}',
            f'pitching_ratings_vsr_balk: {self.pitching_ratings_vsr_balk}',
            f'pitching_ratings_vsr_hp: {self.pitching_ratings_vsr_hp}',
            f'pitching_ratings_vsr_wild_pitch: {self.pitching_ratings_vsr_wild_pitch}',
            f'pitching_ratings_vsl_stuff: {self.pitching_ratings_vsl_stuff}',
            f'pitching_ratings_vsl_control: {self.pitching_ratings_vsl_control}',
            f'pitching_ratings_vsl_movement: {self.pitching_ratings_vsl_movement}',
            f'pitching_ratings_vsl_balk: {self.pitching_ratings_vsl_balk}',
            f'pitching_ratings_vsl_hp: {self.pitching_ratings_vsl_hp}',
            f'pitching_ratings_vsl_wild_pitch: {self.pitching_ratings_vsl_wild_pitch}',
            f'pitching_ratings_talent_stuff: {self.pitching_ratings_talent_stuff}',
            f'pitching_ratings_talent_control: {self.pitching_ratings_talent_control}',
            f'pitching_ratings_talent_movement: {self.pitching_ratings_talent_movement}',
            f'pitching_ratings_talent_balk: {self.pitching_ratings_talent_balk}',
            f'pitching_ratings_talent_hp: {self.pitching_ratings_talent_hp}',
            f'pitching_ratings_talent_wild_pitch: {self.pitching_ratings_talent_wild_pitch}',
            f'pitching_ratings_pitches_fastball: {self.pitching_ratings_pitches_fastball}',
            f'pitching_ratings_pitches_slider: {self.pitching_ratings_pitches_slider}',
            f'pitching_ratings_pitches_curveball: {self.pitching_ratings_pitches_curveball}',
            f'pitching_ratings_pitches_screwball: {self.pitching_ratings_pitches_screwball}',
            f'pitching_ratings_pitches_forkball: {self.pitching_ratings_pitches_forkball}',
            f'pitching_ratings_pitches_changeup: {self.pitching_ratings_pitches_changeup}',
            f'pitching_ratings_pitches_sinker: {self.pitching_ratings_pitches_sinker}',
            f'pitching_ratings_pitches_splitter: {self.pitching_ratings_pitches_splitter}',
            f'pitching_ratings_pitches_knuckleball: {self.pitching_ratings_pitches_knuckleball}',
            f'pitching_ratings_pitches_cutter: {self.pitching_ratings_pitches_cutter}',
            f'pitching_ratings_pitches_circlechange: {self.pitching_ratings_pitches_circlechange}',
            f'pitching_ratings_pitches_knucklecurve: {self.pitching_ratings_pitches_knucklecurve}',
            f'pitching_ratings_pitches_talent_fastball: {self.pitching_ratings_pitches_talent_fastball}',
            f'pitching_ratings_pitches_talent_slider: {self.pitching_ratings_pitches_talent_slider}',
            f'pitching_ratings_pitches_talent_curveball: {self.pitching_ratings_pitches_talent_curveball}',
            f'pitching_ratings_pitches_talent_screwball: {self.pitching_ratings_pitches_talent_screwball}',
            f'pitching_ratings_pitches_talent_forkball: {self.pitching_ratings_pitches_talent_forkball}',
            f'pitching_ratings_pitches_talent_changeup: {self.pitching_ratings_pitches_talent_changeup}',
            f'pitching_ratings_pitches_talent_sinker: {self.pitching_ratings_pitches_talent_sinker}',
            f'pitching_ratings_pitches_talent_splitter: {self.pitching_ratings_pitches_talent_splitter}',
            f'pitching_ratings_pitches_talent_knuckleball: {self.pitching_ratings_pitches_talent_knuckleball}',
            f'pitching_ratings_pitches_talent_cutter: {self.pitching_ratings_pitches_talent_cutter}',
            f'pitching_ratings_pitches_talent_circlechange: {self.pitching_ratings_pitches_talent_circlechange}',
            f'pitching_ratings_pitches_talent_knucklecurve: {self.pitching_ratings_pitches_talent_knucklecurve}',
            f'pitching_ratings_misc_velocity: {self.pitching_ratings_misc_velocity}',
            f'pitching_ratings_misc_arm_slot: {self.pitching_ratings_misc_arm_slot}',
            f'pitching_ratings_misc_stamina: {self.pitching_ratings_misc_stamina}',
            f'pitching_ratings_misc_ground_fly: {self.pitching_ratings_misc_ground_fly}',
            f'pitching_ratings_misc_hold: {self.pitching_ratings_misc_hold}',
            f'pitching_ratings_babip: {self.pitching_ratings_babip}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = PlayersPitchingEntry(*row)
        data[obj.player_id] = obj

    return data
