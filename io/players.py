import pandas


class Player:
    def __init__(self, player_id, team_id, league_id, position, role, first_name, last_name, nick_name, age, date_of_birth, city_of_birth_id, nation_id, second_nation_id, weight, height, retired, free_agent, last_league_id, last_team_id, organization_id, last_organization_id, language_ids0, language_ids1, uniform_number, experience, person_type, bats, throws, personality_greed, personality_loyalty, personality_play_for_winner, personality_work_ethic, personality_intelligence, personality_leader, historical_id, historical_team_id, best_contract_offer_id, injury_is_injured, injury_dtd_injury, injury_career_ending, injury_dl_left, injury_dl_playoff_round, injury_left, dtd_injury_effect, dtd_injury_effect_hit, dtd_injury_effect_throw, dtd_injury_effect_run, injury_id, injury_id2, injury_dtd_injury2, injury_left2, dtd_injury_effect2, dtd_injury_effect_hit2, dtd_injury_effect_throw2, dtd_injury_effect_run2, prone_overall, prone_leg, prone_back, prone_arm, fatigue_pitches0, fatigue_pitches1, fatigue_pitches2, fatigue_pitches3, fatigue_pitches4, fatigue_pitches5, fatigue_points, fatigue_played_today, running_ratings_speed, running_ratings_stealing, running_ratings_baserunning, college, acquired, acquired_date, draft_year, draft_round, draft_supplemental, draft_pick, draft_overall_pick, draft_eligible, hsc_status, redshirt, picked_in_draft, school, commit_school, hidden, draft_league_id, draft_team_id, turned_coach, hall_of_fame, rust, inducted, strategy_override_team, strategy_stealing, strategy_running, strategy_bunt_for_hit, strategy_sac_bunt, strategy_hit_run, strategy_hook_start, strategy_hook_relief, strategy_pitch_count, strategy_pitch_around, strategy_never_pinch_hit, strategy_defensive_sub, strategy_dtd_sit_min, strategy_dtd_allow_ph, local_pop, national_pop, draft_protected, morale, morale_player_performance, morale_team_performance, morale_team_transactions, expectation, morale_player_role, on_loan, loan_league_id, loan_team_id):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.city_of_birth_id = city_of_birth_id
        self.nation_id = nation_id
        self.second_nation_id = second_nation_id
        self.weight = weight
        self.height = height
        self.retired = retired
        self.free_agent = free_agent
        self.last_league_id = last_league_id
        self.last_team_id = last_team_id
        self.organization_id = organization_id
        self.last_organization_id = last_organization_id
        self.language_ids0 = language_ids0
        self.language_ids1 = language_ids1
        self.uniform_number = uniform_number
        self.experience = experience
        self.person_type = person_type
        self.bats = bats
        self.throws = throws
        self.personality_greed = personality_greed
        self.personality_loyalty = personality_loyalty
        self.personality_play_for_winner = personality_play_for_winner
        self.personality_work_ethic = personality_work_ethic
        self.personality_intelligence = personality_intelligence
        self.personality_leader = personality_leader
        self.historical_id = historical_id
        self.historical_team_id = historical_team_id
        self.best_contract_offer_id = best_contract_offer_id
        self.injury_is_injured = injury_is_injured
        self.injury_dtd_injury = injury_dtd_injury
        self.injury_career_ending = injury_career_ending
        self.injury_dl_left = injury_dl_left
        self.injury_dl_playoff_round = injury_dl_playoff_round
        self.injury_left = injury_left
        self.dtd_injury_effect = dtd_injury_effect
        self.dtd_injury_effect_hit = dtd_injury_effect_hit
        self.dtd_injury_effect_throw = dtd_injury_effect_throw
        self.dtd_injury_effect_run = dtd_injury_effect_run
        self.injury_id = injury_id
        self.injury_id2 = injury_id2
        self.injury_dtd_injury2 = injury_dtd_injury2
        self.injury_left2 = injury_left2
        self.dtd_injury_effect2 = dtd_injury_effect2
        self.dtd_injury_effect_hit2 = dtd_injury_effect_hit2
        self.dtd_injury_effect_throw2 = dtd_injury_effect_throw2
        self.dtd_injury_effect_run2 = dtd_injury_effect_run2
        self.prone_overall = prone_overall
        self.prone_leg = prone_leg
        self.prone_back = prone_back
        self.prone_arm = prone_arm
        self.fatigue_pitches0 = fatigue_pitches0
        self.fatigue_pitches1 = fatigue_pitches1
        self.fatigue_pitches2 = fatigue_pitches2
        self.fatigue_pitches3 = fatigue_pitches3
        self.fatigue_pitches4 = fatigue_pitches4
        self.fatigue_pitches5 = fatigue_pitches5
        self.fatigue_points = fatigue_points
        self.fatigue_played_today = fatigue_played_today
        self.running_ratings_speed = running_ratings_speed
        self.running_ratings_stealing = running_ratings_stealing
        self.running_ratings_baserunning = running_ratings_baserunning
        self.college = college
        self.acquired = acquired
        self.acquired_date = acquired_date
        self.draft_year = draft_year
        self.draft_round = draft_round
        self.draft_supplemental = draft_supplemental
        self.draft_pick = draft_pick
        self.draft_overall_pick = draft_overall_pick
        self.draft_eligible = draft_eligible
        self.hsc_status = hsc_status
        self.redshirt = redshirt
        self.picked_in_draft = picked_in_draft
        self.school = school
        self.commit_school = commit_school
        self.hidden = hidden
        self.draft_league_id = draft_league_id
        self.draft_team_id = draft_team_id
        self.turned_coach = turned_coach
        self.hall_of_fame = hall_of_fame
        self.rust = rust
        self.inducted = inducted
        self.strategy_override_team = strategy_override_team
        self.strategy_stealing = strategy_stealing
        self.strategy_running = strategy_running
        self.strategy_bunt_for_hit = strategy_bunt_for_hit
        self.strategy_sac_bunt = strategy_sac_bunt
        self.strategy_hit_run = strategy_hit_run
        self.strategy_hook_start = strategy_hook_start
        self.strategy_hook_relief = strategy_hook_relief
        self.strategy_pitch_count = strategy_pitch_count
        self.strategy_pitch_around = strategy_pitch_around
        self.strategy_never_pinch_hit = strategy_never_pinch_hit
        self.strategy_defensive_sub = strategy_defensive_sub
        self.strategy_dtd_sit_min = strategy_dtd_sit_min
        self.strategy_dtd_allow_ph = strategy_dtd_allow_ph
        self.local_pop = local_pop
        self.national_pop = national_pop
        self.draft_protected = draft_protected
        self.morale = morale
        self.morale_player_performance = morale_player_performance
        self.morale_team_performance = morale_team_performance
        self.morale_team_transactions = morale_team_transactions
        self.expectation = expectation
        self.morale_player_role = morale_player_role
        self.on_loan = on_loan
        self.loan_league_id = loan_league_id
        self.loan_team_id = loan_team_id
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'first_name: {self.first_name}',
            f'last_name: {self.last_name}',
            f'nick_name: {self.nick_name}',
            f'age: {self.age}',
            f'date_of_birth: {self.date_of_birth}',
            f'city_of_birth_id: {self.city_of_birth_id}',
            f'nation_id: {self.nation_id}',
            f'second_nation_id: {self.second_nation_id}',
            f'weight: {self.weight}',
            f'height: {self.height}',
            f'retired: {self.retired}',
            f'free_agent: {self.free_agent}',
            f'last_league_id: {self.last_league_id}',
            f'last_team_id: {self.last_team_id}',
            f'organization_id: {self.organization_id}',
            f'last_organization_id: {self.last_organization_id}',
            f'language_ids0: {self.language_ids0}',
            f'language_ids1: {self.language_ids1}',
            f'uniform_number: {self.uniform_number}',
            f'experience: {self.experience}',
            f'person_type: {self.person_type}',
            f'bats: {self.bats}',
            f'throws: {self.throws}',
            f'personality_greed: {self.personality_greed}',
            f'personality_loyalty: {self.personality_loyalty}',
            f'personality_play_for_winner: {self.personality_play_for_winner}',
            f'personality_work_ethic: {self.personality_work_ethic}',
            f'personality_intelligence: {self.personality_intelligence}',
            f'personality_leader: {self.personality_leader}',
            f'historical_id: {self.historical_id}',
            f'historical_team_id: {self.historical_team_id}',
            f'best_contract_offer_id: {self.best_contract_offer_id}',
            f'injury_is_injured: {self.injury_is_injured}',
            f'injury_dtd_injury: {self.injury_dtd_injury}',
            f'injury_career_ending: {self.injury_career_ending}',
            f'injury_dl_left: {self.injury_dl_left}',
            f'injury_dl_playoff_round: {self.injury_dl_playoff_round}',
            f'injury_left: {self.injury_left}',
            f'dtd_injury_effect: {self.dtd_injury_effect}',
            f'dtd_injury_effect_hit: {self.dtd_injury_effect_hit}',
            f'dtd_injury_effect_throw: {self.dtd_injury_effect_throw}',
            f'dtd_injury_effect_run: {self.dtd_injury_effect_run}',
            f'injury_id: {self.injury_id}',
            f'injury_id2: {self.injury_id2}',
            f'injury_dtd_injury2: {self.injury_dtd_injury2}',
            f'injury_left2: {self.injury_left2}',
            f'dtd_injury_effect2: {self.dtd_injury_effect2}',
            f'dtd_injury_effect_hit2: {self.dtd_injury_effect_hit2}',
            f'dtd_injury_effect_throw2: {self.dtd_injury_effect_throw2}',
            f'dtd_injury_effect_run2: {self.dtd_injury_effect_run2}',
            f'prone_overall: {self.prone_overall}',
            f'prone_leg: {self.prone_leg}',
            f'prone_back: {self.prone_back}',
            f'prone_arm: {self.prone_arm}',
            f'fatigue_pitches0: {self.fatigue_pitches0}',
            f'fatigue_pitches1: {self.fatigue_pitches1}',
            f'fatigue_pitches2: {self.fatigue_pitches2}',
            f'fatigue_pitches3: {self.fatigue_pitches3}',
            f'fatigue_pitches4: {self.fatigue_pitches4}',
            f'fatigue_pitches5: {self.fatigue_pitches5}',
            f'fatigue_points: {self.fatigue_points}',
            f'fatigue_played_today: {self.fatigue_played_today}',
            f'running_ratings_speed: {self.running_ratings_speed}',
            f'running_ratings_stealing: {self.running_ratings_stealing}',
            f'running_ratings_baserunning: {self.running_ratings_baserunning}',
            f'college: {self.college}',
            f'acquired: {self.acquired}',
            f'acquired_date: {self.acquired_date}',
            f'draft_year: {self.draft_year}',
            f'draft_round: {self.draft_round}',
            f'draft_supplemental: {self.draft_supplemental}',
            f'draft_pick: {self.draft_pick}',
            f'draft_overall_pick: {self.draft_overall_pick}',
            f'draft_eligible: {self.draft_eligible}',
            f'hsc_status: {self.hsc_status}',
            f'redshirt: {self.redshirt}',
            f'picked_in_draft: {self.picked_in_draft}',
            f'school: {self.school}',
            f'commit_school: {self.commit_school}',
            f'hidden: {self.hidden}',
            f'draft_league_id: {self.draft_league_id}',
            f'draft_team_id: {self.draft_team_id}',
            f'turned_coach: {self.turned_coach}',
            f'hall_of_fame: {self.hall_of_fame}',
            f'rust: {self.rust}',
            f'inducted: {self.inducted}',
            f'strategy_override_team: {self.strategy_override_team}',
            f'strategy_stealing: {self.strategy_stealing}',
            f'strategy_running: {self.strategy_running}',
            f'strategy_bunt_for_hit: {self.strategy_bunt_for_hit}',
            f'strategy_sac_bunt: {self.strategy_sac_bunt}',
            f'strategy_hit_run: {self.strategy_hit_run}',
            f'strategy_hook_start: {self.strategy_hook_start}',
            f'strategy_hook_relief: {self.strategy_hook_relief}',
            f'strategy_pitch_count: {self.strategy_pitch_count}',
            f'strategy_pitch_around: {self.strategy_pitch_around}',
            f'strategy_never_pinch_hit: {self.strategy_never_pinch_hit}',
            f'strategy_defensive_sub: {self.strategy_defensive_sub}',
            f'strategy_dtd_sit_min: {self.strategy_dtd_sit_min}',
            f'strategy_dtd_allow_ph: {self.strategy_dtd_allow_ph}',
            f'local_pop: {self.local_pop}',
            f'national_pop: {self.national_pop}',
            f'draft_protected: {self.draft_protected}',
            f'morale: {self.morale}',
            f'morale_player_performance: {self.morale_player_performance}',
            f'morale_team_performance: {self.morale_team_performance}',
            f'morale_team_transactions: {self.morale_team_transactions}',
            f'expectation: {self.expectation}',
            f'morale_player_role: {self.morale_player_role}',
            f'on_loan: {self.on_loan}',
            f'loan_league_id: {self.loan_league_id}',
            f'loan_team_id: {self.loan_team_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Player(*row)
        data[obj.player_id] = obj

    return data
