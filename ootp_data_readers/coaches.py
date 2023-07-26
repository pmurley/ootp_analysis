import pandas


class Coach:
    def __init__(self, coach_id, first_name, last_name, nick_name, age, date_of_birth, city_of_birth_id, nation_id, weight, height, position, experience, occupation, team_id, former_player_id, quick_left, contract_salary, contract_years, contract_extension_salary, contract_extension_years, scout_major, scout_minor, scout_international, scout_amateur, scout_amateur_preference, teach_hitting, teach_pitching, teach_c, teach_if, teach_of, handle_veterans, handle_rookies, handle_players, heal_legs, heal_arms, heal_back, heal_other, heal_rest, management_style, personality, hitting_focus, pitching_focus, training_focus, teach_running, prevent_legs, prevent_arms, prevent_back, prevent_other, stealing, running, pinchrun, pinchhit_pos, pinchhit_pitch, hook_start, hook_relief, closer, lr_matchup, bunt_hit, bunt, hit_run, run_hit, squeeze, pitch_around, intentional_walk, hold_runner, guard_lines, infield_in, outfield_in, corners_in, shift_if, shift_of, opener, num_pitchers, num_hitters, favor_speed_to_power, favor_avg_to_obp, favor_defense_to_offense, favor_pitching_to_hitting, favor_veterans_to_prospects, trade_aggressiveness, player_loyalty, trade_frequency, trade_preference, value_stats, value_this_year, value_last_year, value_two_years, draft_value, intl_fa_value, develop_value, ratings_value, manager_value, pitching_coach_value, hitting_coach_value, scout_value, doctor_value, basecoach_value, positive_relation, negative_relation):
        self.coach_id = coach_id
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.city_of_birth_id = city_of_birth_id
        self.nation_id = nation_id
        self.weight = weight
        self.height = height
        self.position = position
        self.experience = experience
        self.occupation = occupation
        self.team_id = team_id
        self.former_player_id = former_player_id
        self.quick_left = quick_left
        self.contract_salary = contract_salary
        self.contract_years = contract_years
        self.contract_extension_salary = contract_extension_salary
        self.contract_extension_years = contract_extension_years
        self.scout_major = scout_major
        self.scout_minor = scout_minor
        self.scout_international = scout_international
        self.scout_amateur = scout_amateur
        self.scout_amateur_preference = scout_amateur_preference
        self.teach_hitting = teach_hitting
        self.teach_pitching = teach_pitching
        self.teach_c = teach_c
        self.teach_if = teach_if
        self.teach_of = teach_of
        self.handle_veterans = handle_veterans
        self.handle_rookies = handle_rookies
        self.handle_players = handle_players
        self.heal_legs = heal_legs
        self.heal_arms = heal_arms
        self.heal_back = heal_back
        self.heal_other = heal_other
        self.heal_rest = heal_rest
        self.management_style = management_style
        self.personality = personality
        self.hitting_focus = hitting_focus
        self.pitching_focus = pitching_focus
        self.training_focus = training_focus
        self.teach_running = teach_running
        self.prevent_legs = prevent_legs
        self.prevent_arms = prevent_arms
        self.prevent_back = prevent_back
        self.prevent_other = prevent_other
        self.stealing = stealing
        self.running = running
        self.pinchrun = pinchrun
        self.pinchhit_pos = pinchhit_pos
        self.pinchhit_pitch = pinchhit_pitch
        self.hook_start = hook_start
        self.hook_relief = hook_relief
        self.closer = closer
        self.lr_matchup = lr_matchup
        self.bunt_hit = bunt_hit
        self.bunt = bunt
        self.hit_run = hit_run
        self.run_hit = run_hit
        self.squeeze = squeeze
        self.pitch_around = pitch_around
        self.intentional_walk = intentional_walk
        self.hold_runner = hold_runner
        self.guard_lines = guard_lines
        self.infield_in = infield_in
        self.outfield_in = outfield_in
        self.corners_in = corners_in
        self.shift_if = shift_if
        self.shift_of = shift_of
        self.opener = opener
        self.num_pitchers = num_pitchers
        self.num_hitters = num_hitters
        self.favor_speed_to_power = favor_speed_to_power
        self.favor_avg_to_obp = favor_avg_to_obp
        self.favor_defense_to_offense = favor_defense_to_offense
        self.favor_pitching_to_hitting = favor_pitching_to_hitting
        self.favor_veterans_to_prospects = favor_veterans_to_prospects
        self.trade_aggressiveness = trade_aggressiveness
        self.player_loyalty = player_loyalty
        self.trade_frequency = trade_frequency
        self.trade_preference = trade_preference
        self.value_stats = value_stats
        self.value_this_year = value_this_year
        self.value_last_year = value_last_year
        self.value_two_years = value_two_years
        self.draft_value = draft_value
        self.intl_fa_value = intl_fa_value
        self.develop_value = develop_value
        self.ratings_value = ratings_value
        self.manager_value = manager_value
        self.pitching_coach_value = pitching_coach_value
        self.hitting_coach_value = hitting_coach_value
        self.scout_value = scout_value
        self.doctor_value = doctor_value
        self.basecoach_value = basecoach_value
        self.positive_relation = positive_relation
        self.negative_relation = negative_relation
    
    def __str__(self):
        return "\n".join([
            f'coach_id: {self.coach_id}',
            f'first_name: {self.first_name}',
            f'last_name: {self.last_name}',
            f'nick_name: {self.nick_name}',
            f'age: {self.age}',
            f'date_of_birth: {self.date_of_birth}',
            f'city_of_birth_id: {self.city_of_birth_id}',
            f'nation_id: {self.nation_id}',
            f'weight: {self.weight}',
            f'height: {self.height}',
            f'position: {self.position}',
            f'experience: {self.experience}',
            f'occupation: {self.occupation}',
            f'team_id: {self.team_id}',
            f'former_player_id: {self.former_player_id}',
            f'quick_left: {self.quick_left}',
            f'contract_salary: {self.contract_salary}',
            f'contract_years: {self.contract_years}',
            f'contract_extension_salary: {self.contract_extension_salary}',
            f'contract_extension_years: {self.contract_extension_years}',
            f'scout_major: {self.scout_major}',
            f'scout_minor: {self.scout_minor}',
            f'scout_international: {self.scout_international}',
            f'scout_amateur: {self.scout_amateur}',
            f'scout_amateur_preference: {self.scout_amateur_preference}',
            f'teach_hitting: {self.teach_hitting}',
            f'teach_pitching: {self.teach_pitching}',
            f'teach_c: {self.teach_c}',
            f'teach_if: {self.teach_if}',
            f'teach_of: {self.teach_of}',
            f'handle_veterans: {self.handle_veterans}',
            f'handle_rookies: {self.handle_rookies}',
            f'handle_players: {self.handle_players}',
            f'heal_legs: {self.heal_legs}',
            f'heal_arms: {self.heal_arms}',
            f'heal_back: {self.heal_back}',
            f'heal_other: {self.heal_other}',
            f'heal_rest: {self.heal_rest}',
            f'management_style: {self.management_style}',
            f'personality: {self.personality}',
            f'hitting_focus: {self.hitting_focus}',
            f'pitching_focus: {self.pitching_focus}',
            f'training_focus: {self.training_focus}',
            f'teach_running: {self.teach_running}',
            f'prevent_legs: {self.prevent_legs}',
            f'prevent_arms: {self.prevent_arms}',
            f'prevent_back: {self.prevent_back}',
            f'prevent_other: {self.prevent_other}',
            f'stealing: {self.stealing}',
            f'running: {self.running}',
            f'pinchrun: {self.pinchrun}',
            f'pinchhit_pos: {self.pinchhit_pos}',
            f'pinchhit_pitch: {self.pinchhit_pitch}',
            f'hook_start: {self.hook_start}',
            f'hook_relief: {self.hook_relief}',
            f'closer: {self.closer}',
            f'lr_matchup: {self.lr_matchup}',
            f'bunt_hit: {self.bunt_hit}',
            f'bunt: {self.bunt}',
            f'hit_run: {self.hit_run}',
            f'run_hit: {self.run_hit}',
            f'squeeze: {self.squeeze}',
            f'pitch_around: {self.pitch_around}',
            f'intentional_walk: {self.intentional_walk}',
            f'hold_runner: {self.hold_runner}',
            f'guard_lines: {self.guard_lines}',
            f'infield_in: {self.infield_in}',
            f'outfield_in: {self.outfield_in}',
            f'corners_in: {self.corners_in}',
            f'shift_if: {self.shift_if}',
            f'shift_of: {self.shift_of}',
            f'opener: {self.opener}',
            f'num_pitchers: {self.num_pitchers}',
            f'num_hitters: {self.num_hitters}',
            f'favor_speed_to_power: {self.favor_speed_to_power}',
            f'favor_avg_to_obp: {self.favor_avg_to_obp}',
            f'favor_defense_to_offense: {self.favor_defense_to_offense}',
            f'favor_pitching_to_hitting: {self.favor_pitching_to_hitting}',
            f'favor_veterans_to_prospects: {self.favor_veterans_to_prospects}',
            f'trade_aggressiveness: {self.trade_aggressiveness}',
            f'player_loyalty: {self.player_loyalty}',
            f'trade_frequency: {self.trade_frequency}',
            f'trade_preference: {self.trade_preference}',
            f'value_stats: {self.value_stats}',
            f'value_this_year: {self.value_this_year}',
            f'value_last_year: {self.value_last_year}',
            f'value_two_years: {self.value_two_years}',
            f'draft_value: {self.draft_value}',
            f'intl_fa_value: {self.intl_fa_value}',
            f'develop_value: {self.develop_value}',
            f'ratings_value: {self.ratings_value}',
            f'manager_value: {self.manager_value}',
            f'pitching_coach_value: {self.pitching_coach_value}',
            f'hitting_coach_value: {self.hitting_coach_value}',
            f'scout_value: {self.scout_value}',
            f'doctor_value: {self.doctor_value}',
            f'basecoach_value: {self.basecoach_value}',
            f'positive_relation: {self.positive_relation}',
            f'negative_relation: {self.negative_relation}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Coach(*row)
        data[obj.coach_id] = obj

    return data
