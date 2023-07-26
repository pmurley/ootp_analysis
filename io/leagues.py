import pandas


class League:
    def __init__(self, league_id, name, abbr, nation_id, language_id, gender, historical_league, logo_file_name, players_path, start_date, preferred_start_date, pitcher_award_name, mvp_award_name, rookie_award_name, defense_award_name, fictional_players, start_fantasy_draft, trading_deadline, winter_meetings, arbitration_offering, show_draft_pool, rosters_expanded, draft_date, rule_5_draft_date, international_fa_date, roster_expand_date, trade_deadline_date, allstar_date, days_until_deadline, next_draft_type, parent_league_id, league_state, season_year, historical_year, league_level, stats_detail, historical_import_path, foreigner_percentage, was_ootp6, was_65, allstar_game, auto_schedule_allstar, allstar_team_id0, allstar_team_id1, schedule_file_1, schedule_file_2, rules_rule_5, rules_minor_league_options, rules_trading, rules_trading_deadline_events, rules_draft_pick_trading, rules_financials, rules_amateur_draft, rules_fa_compensation, rules_schedule_balanced, rules_schedule_inter_league, rules_schedule_force_start_day, rules_trades_other_leagues, rules_free_agents_from_other_leagues, rules_free_agents_leave_other_leagues, rules_allstar_game, rules_spring_training, rules_active_roster_limit, rules_secondary_roster_limit, rules_expanded_roster_limit, rules_min_service_days, rules_waiver_period_length, rules_dfa_period_length, rules_fa_minimum_years, rules_salary_arbitration_minimum_years, rules_minor_league_fa_minimum_years, rules_foreigner_limit, rules_foreigner_pitcher_limit, rules_foreigner_hitter_limit, rules_schedule_games_per_team, rules_schedule_typical_series, rules_schedule_game_times, rules_schedule_preferred_start_day, rules_amateur_draft_rounds, rules_minimum_salary, rules_salary_cap, rules_player_salary0, rules_player_salary1, rules_player_salary2, rules_player_salary3, rules_player_salary4, rules_player_salary5, rules_player_salary6, rules_player_salary7, rules_average_coach_salary, rules_average_attendance, rules_average_national_media_contract, rules_cash_maximum, rules_average_ticket_price, rules_luxury_sharing, rules_revenue_sharing, rules_revenue_sharing_tax, rules_luxury_sharing_cap, rules_luxury_tax, rules_national_media_contract_fixed, rules_owner_decides_budget, rules_schedule_auto_adjust_dates, rules_historical_import_rookies, avg_rating_contact, avg_rating_gap, avg_rating_power, avg_rating_eye, avg_rating_strikeouts, avg_rating_stuff, avg_rating_movement, avg_rating_control, avg_rating_fielding0, avg_rating_fielding1, avg_rating_fielding2, avg_rating_fielding3, avg_rating_fielding4, avg_rating_fielding5, avg_rating_fielding6, avg_rating_fielding7, avg_rating_fielding8, avg_rating_fielding9, avg_rating_overall, avg_rating_age, league_totals_ab, league_totals_h, league_totals_d, league_totals_t, league_totals_hr, league_totals_bb, league_totals_hp, league_totals_k, league_totals_pa, league_totals_babip, league_totals_mod_h, league_totals_mod_d, league_totals_mod_t, league_totals_mod_hr, league_totals_mod_bb, league_totals_mod_hp, league_totals_mod_k, league_totals_mod_babip, ml_equivalencies_avg, ml_equivalencies_hr, ml_equivalencies_eb, ml_equivalencies_bb, ml_equivalencies_k, ml_equivalencies_hp, player_creation_modifier_contact, player_creation_modifier_gap, player_creation_modifier_power, player_creation_modifier_eye, player_creation_modifier_strikeouts, player_creation_modifier_stuff, player_creation_modifier_movement, player_creation_modifier_control, player_creation_modifier_speed, player_creation_modifier_fielding, financial_coefficient, world_start_year, current_date, background_color_id, text_color_id, scouting_coach_id):
        self.league_id = league_id
        self.name = name
        self.abbr = abbr
        self.nation_id = nation_id
        self.language_id = language_id
        self.gender = gender
        self.historical_league = historical_league
        self.logo_file_name = logo_file_name
        self.players_path = players_path
        self.start_date = start_date
        self.preferred_start_date = preferred_start_date
        self.pitcher_award_name = pitcher_award_name
        self.mvp_award_name = mvp_award_name
        self.rookie_award_name = rookie_award_name
        self.defense_award_name = defense_award_name
        self.fictional_players = fictional_players
        self.start_fantasy_draft = start_fantasy_draft
        self.trading_deadline = trading_deadline
        self.winter_meetings = winter_meetings
        self.arbitration_offering = arbitration_offering
        self.show_draft_pool = show_draft_pool
        self.rosters_expanded = rosters_expanded
        self.draft_date = draft_date
        self.rule_5_draft_date = rule_5_draft_date
        self.international_fa_date = international_fa_date
        self.roster_expand_date = roster_expand_date
        self.trade_deadline_date = trade_deadline_date
        self.allstar_date = allstar_date
        self.days_until_deadline = days_until_deadline
        self.next_draft_type = next_draft_type
        self.parent_league_id = parent_league_id
        self.league_state = league_state
        self.season_year = season_year
        self.historical_year = historical_year
        self.league_level = league_level
        self.stats_detail = stats_detail
        self.historical_import_path = historical_import_path
        self.foreigner_percentage = foreigner_percentage
        self.was_ootp6 = was_ootp6
        self.was_65 = was_65
        self.allstar_game = allstar_game
        self.auto_schedule_allstar = auto_schedule_allstar
        self.allstar_team_id0 = allstar_team_id0
        self.allstar_team_id1 = allstar_team_id1
        self.schedule_file_1 = schedule_file_1
        self.schedule_file_2 = schedule_file_2
        self.rules_rule_5 = rules_rule_5
        self.rules_minor_league_options = rules_minor_league_options
        self.rules_trading = rules_trading
        self.rules_trading_deadline_events = rules_trading_deadline_events
        self.rules_draft_pick_trading = rules_draft_pick_trading
        self.rules_financials = rules_financials
        self.rules_amateur_draft = rules_amateur_draft
        self.rules_fa_compensation = rules_fa_compensation
        self.rules_schedule_balanced = rules_schedule_balanced
        self.rules_schedule_inter_league = rules_schedule_inter_league
        self.rules_schedule_force_start_day = rules_schedule_force_start_day
        self.rules_trades_other_leagues = rules_trades_other_leagues
        self.rules_free_agents_from_other_leagues = rules_free_agents_from_other_leagues
        self.rules_free_agents_leave_other_leagues = rules_free_agents_leave_other_leagues
        self.rules_allstar_game = rules_allstar_game
        self.rules_spring_training = rules_spring_training
        self.rules_active_roster_limit = rules_active_roster_limit
        self.rules_secondary_roster_limit = rules_secondary_roster_limit
        self.rules_expanded_roster_limit = rules_expanded_roster_limit
        self.rules_min_service_days = rules_min_service_days
        self.rules_waiver_period_length = rules_waiver_period_length
        self.rules_dfa_period_length = rules_dfa_period_length
        self.rules_fa_minimum_years = rules_fa_minimum_years
        self.rules_salary_arbitration_minimum_years = rules_salary_arbitration_minimum_years
        self.rules_minor_league_fa_minimum_years = rules_minor_league_fa_minimum_years
        self.rules_foreigner_limit = rules_foreigner_limit
        self.rules_foreigner_pitcher_limit = rules_foreigner_pitcher_limit
        self.rules_foreigner_hitter_limit = rules_foreigner_hitter_limit
        self.rules_schedule_games_per_team = rules_schedule_games_per_team
        self.rules_schedule_typical_series = rules_schedule_typical_series
        self.rules_schedule_game_times = rules_schedule_game_times
        self.rules_schedule_preferred_start_day = rules_schedule_preferred_start_day
        self.rules_amateur_draft_rounds = rules_amateur_draft_rounds
        self.rules_minimum_salary = rules_minimum_salary
        self.rules_salary_cap = rules_salary_cap
        self.rules_player_salary0 = rules_player_salary0
        self.rules_player_salary1 = rules_player_salary1
        self.rules_player_salary2 = rules_player_salary2
        self.rules_player_salary3 = rules_player_salary3
        self.rules_player_salary4 = rules_player_salary4
        self.rules_player_salary5 = rules_player_salary5
        self.rules_player_salary6 = rules_player_salary6
        self.rules_player_salary7 = rules_player_salary7
        self.rules_average_coach_salary = rules_average_coach_salary
        self.rules_average_attendance = rules_average_attendance
        self.rules_average_national_media_contract = rules_average_national_media_contract
        self.rules_cash_maximum = rules_cash_maximum
        self.rules_average_ticket_price = rules_average_ticket_price
        self.rules_luxury_sharing = rules_luxury_sharing
        self.rules_revenue_sharing = rules_revenue_sharing
        self.rules_revenue_sharing_tax = rules_revenue_sharing_tax
        self.rules_luxury_sharing_cap = rules_luxury_sharing_cap
        self.rules_luxury_tax = rules_luxury_tax
        self.rules_national_media_contract_fixed = rules_national_media_contract_fixed
        self.rules_owner_decides_budget = rules_owner_decides_budget
        self.rules_schedule_auto_adjust_dates = rules_schedule_auto_adjust_dates
        self.rules_historical_import_rookies = rules_historical_import_rookies
        self.avg_rating_contact = avg_rating_contact
        self.avg_rating_gap = avg_rating_gap
        self.avg_rating_power = avg_rating_power
        self.avg_rating_eye = avg_rating_eye
        self.avg_rating_strikeouts = avg_rating_strikeouts
        self.avg_rating_stuff = avg_rating_stuff
        self.avg_rating_movement = avg_rating_movement
        self.avg_rating_control = avg_rating_control
        self.avg_rating_fielding0 = avg_rating_fielding0
        self.avg_rating_fielding1 = avg_rating_fielding1
        self.avg_rating_fielding2 = avg_rating_fielding2
        self.avg_rating_fielding3 = avg_rating_fielding3
        self.avg_rating_fielding4 = avg_rating_fielding4
        self.avg_rating_fielding5 = avg_rating_fielding5
        self.avg_rating_fielding6 = avg_rating_fielding6
        self.avg_rating_fielding7 = avg_rating_fielding7
        self.avg_rating_fielding8 = avg_rating_fielding8
        self.avg_rating_fielding9 = avg_rating_fielding9
        self.avg_rating_overall = avg_rating_overall
        self.avg_rating_age = avg_rating_age
        self.league_totals_ab = league_totals_ab
        self.league_totals_h = league_totals_h
        self.league_totals_d = league_totals_d
        self.league_totals_t = league_totals_t
        self.league_totals_hr = league_totals_hr
        self.league_totals_bb = league_totals_bb
        self.league_totals_hp = league_totals_hp
        self.league_totals_k = league_totals_k
        self.league_totals_pa = league_totals_pa
        self.league_totals_babip = league_totals_babip
        self.league_totals_mod_h = league_totals_mod_h
        self.league_totals_mod_d = league_totals_mod_d
        self.league_totals_mod_t = league_totals_mod_t
        self.league_totals_mod_hr = league_totals_mod_hr
        self.league_totals_mod_bb = league_totals_mod_bb
        self.league_totals_mod_hp = league_totals_mod_hp
        self.league_totals_mod_k = league_totals_mod_k
        self.league_totals_mod_babip = league_totals_mod_babip
        self.ml_equivalencies_avg = ml_equivalencies_avg
        self.ml_equivalencies_hr = ml_equivalencies_hr
        self.ml_equivalencies_eb = ml_equivalencies_eb
        self.ml_equivalencies_bb = ml_equivalencies_bb
        self.ml_equivalencies_k = ml_equivalencies_k
        self.ml_equivalencies_hp = ml_equivalencies_hp
        self.player_creation_modifier_contact = player_creation_modifier_contact
        self.player_creation_modifier_gap = player_creation_modifier_gap
        self.player_creation_modifier_power = player_creation_modifier_power
        self.player_creation_modifier_eye = player_creation_modifier_eye
        self.player_creation_modifier_strikeouts = player_creation_modifier_strikeouts
        self.player_creation_modifier_stuff = player_creation_modifier_stuff
        self.player_creation_modifier_movement = player_creation_modifier_movement
        self.player_creation_modifier_control = player_creation_modifier_control
        self.player_creation_modifier_speed = player_creation_modifier_speed
        self.player_creation_modifier_fielding = player_creation_modifier_fielding
        self.financial_coefficient = financial_coefficient
        self.world_start_year = world_start_year
        self.current_date = current_date
        self.background_color_id = background_color_id
        self.text_color_id = text_color_id
        self.scouting_coach_id = scouting_coach_id
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'name: {self.name}',
            f'abbr: {self.abbr}',
            f'nation_id: {self.nation_id}',
            f'language_id: {self.language_id}',
            f'gender: {self.gender}',
            f'historical_league: {self.historical_league}',
            f'logo_file_name: {self.logo_file_name}',
            f'players_path: {self.players_path}',
            f'start_date: {self.start_date}',
            f'preferred_start_date: {self.preferred_start_date}',
            f'pitcher_award_name: {self.pitcher_award_name}',
            f'mvp_award_name: {self.mvp_award_name}',
            f'rookie_award_name: {self.rookie_award_name}',
            f'defense_award_name: {self.defense_award_name}',
            f'fictional_players: {self.fictional_players}',
            f'start_fantasy_draft: {self.start_fantasy_draft}',
            f'trading_deadline: {self.trading_deadline}',
            f'winter_meetings: {self.winter_meetings}',
            f'arbitration_offering: {self.arbitration_offering}',
            f'show_draft_pool: {self.show_draft_pool}',
            f'rosters_expanded: {self.rosters_expanded}',
            f'draft_date: {self.draft_date}',
            f'rule_5_draft_date: {self.rule_5_draft_date}',
            f'international_fa_date: {self.international_fa_date}',
            f'roster_expand_date: {self.roster_expand_date}',
            f'trade_deadline_date: {self.trade_deadline_date}',
            f'allstar_date: {self.allstar_date}',
            f'days_until_deadline: {self.days_until_deadline}',
            f'next_draft_type: {self.next_draft_type}',
            f'parent_league_id: {self.parent_league_id}',
            f'league_state: {self.league_state}',
            f'season_year: {self.season_year}',
            f'historical_year: {self.historical_year}',
            f'league_level: {self.league_level}',
            f'stats_detail: {self.stats_detail}',
            f'historical_import_path: {self.historical_import_path}',
            f'foreigner_percentage: {self.foreigner_percentage}',
            f'was_ootp6: {self.was_ootp6}',
            f'was_65: {self.was_65}',
            f'allstar_game: {self.allstar_game}',
            f'auto_schedule_allstar: {self.auto_schedule_allstar}',
            f'allstar_team_id0: {self.allstar_team_id0}',
            f'allstar_team_id1: {self.allstar_team_id1}',
            f'schedule_file_1: {self.schedule_file_1}',
            f'schedule_file_2: {self.schedule_file_2}',
            f'rules_rule_5: {self.rules_rule_5}',
            f'rules_minor_league_options: {self.rules_minor_league_options}',
            f'rules_trading: {self.rules_trading}',
            f'rules_trading_deadline_events: {self.rules_trading_deadline_events}',
            f'rules_draft_pick_trading: {self.rules_draft_pick_trading}',
            f'rules_financials: {self.rules_financials}',
            f'rules_amateur_draft: {self.rules_amateur_draft}',
            f'rules_fa_compensation: {self.rules_fa_compensation}',
            f'rules_schedule_balanced: {self.rules_schedule_balanced}',
            f'rules_schedule_inter_league: {self.rules_schedule_inter_league}',
            f'rules_schedule_force_start_day: {self.rules_schedule_force_start_day}',
            f'rules_trades_other_leagues: {self.rules_trades_other_leagues}',
            f'rules_free_agents_from_other_leagues: {self.rules_free_agents_from_other_leagues}',
            f'rules_free_agents_leave_other_leagues: {self.rules_free_agents_leave_other_leagues}',
            f'rules_allstar_game: {self.rules_allstar_game}',
            f'rules_spring_training: {self.rules_spring_training}',
            f'rules_active_roster_limit: {self.rules_active_roster_limit}',
            f'rules_secondary_roster_limit: {self.rules_secondary_roster_limit}',
            f'rules_expanded_roster_limit: {self.rules_expanded_roster_limit}',
            f'rules_min_service_days: {self.rules_min_service_days}',
            f'rules_waiver_period_length: {self.rules_waiver_period_length}',
            f'rules_dfa_period_length: {self.rules_dfa_period_length}',
            f'rules_fa_minimum_years: {self.rules_fa_minimum_years}',
            f'rules_salary_arbitration_minimum_years: {self.rules_salary_arbitration_minimum_years}',
            f'rules_minor_league_fa_minimum_years: {self.rules_minor_league_fa_minimum_years}',
            f'rules_foreigner_limit: {self.rules_foreigner_limit}',
            f'rules_foreigner_pitcher_limit: {self.rules_foreigner_pitcher_limit}',
            f'rules_foreigner_hitter_limit: {self.rules_foreigner_hitter_limit}',
            f'rules_schedule_games_per_team: {self.rules_schedule_games_per_team}',
            f'rules_schedule_typical_series: {self.rules_schedule_typical_series}',
            f'rules_schedule_game_times: {self.rules_schedule_game_times}',
            f'rules_schedule_preferred_start_day: {self.rules_schedule_preferred_start_day}',
            f'rules_amateur_draft_rounds: {self.rules_amateur_draft_rounds}',
            f'rules_minimum_salary: {self.rules_minimum_salary}',
            f'rules_salary_cap: {self.rules_salary_cap}',
            f'rules_player_salary0: {self.rules_player_salary0}',
            f'rules_player_salary1: {self.rules_player_salary1}',
            f'rules_player_salary2: {self.rules_player_salary2}',
            f'rules_player_salary3: {self.rules_player_salary3}',
            f'rules_player_salary4: {self.rules_player_salary4}',
            f'rules_player_salary5: {self.rules_player_salary5}',
            f'rules_player_salary6: {self.rules_player_salary6}',
            f'rules_player_salary7: {self.rules_player_salary7}',
            f'rules_average_coach_salary: {self.rules_average_coach_salary}',
            f'rules_average_attendance: {self.rules_average_attendance}',
            f'rules_average_national_media_contract: {self.rules_average_national_media_contract}',
            f'rules_cash_maximum: {self.rules_cash_maximum}',
            f'rules_average_ticket_price: {self.rules_average_ticket_price}',
            f'rules_luxury_sharing: {self.rules_luxury_sharing}',
            f'rules_revenue_sharing: {self.rules_revenue_sharing}',
            f'rules_revenue_sharing_tax: {self.rules_revenue_sharing_tax}',
            f'rules_luxury_sharing_cap: {self.rules_luxury_sharing_cap}',
            f'rules_luxury_tax: {self.rules_luxury_tax}',
            f'rules_national_media_contract_fixed: {self.rules_national_media_contract_fixed}',
            f'rules_owner_decides_budget: {self.rules_owner_decides_budget}',
            f'rules_schedule_auto_adjust_dates: {self.rules_schedule_auto_adjust_dates}',
            f'rules_historical_import_rookies: {self.rules_historical_import_rookies}',
            f'avg_rating_contact: {self.avg_rating_contact}',
            f'avg_rating_gap: {self.avg_rating_gap}',
            f'avg_rating_power: {self.avg_rating_power}',
            f'avg_rating_eye: {self.avg_rating_eye}',
            f'avg_rating_strikeouts: {self.avg_rating_strikeouts}',
            f'avg_rating_stuff: {self.avg_rating_stuff}',
            f'avg_rating_movement: {self.avg_rating_movement}',
            f'avg_rating_control: {self.avg_rating_control}',
            f'avg_rating_fielding0: {self.avg_rating_fielding0}',
            f'avg_rating_fielding1: {self.avg_rating_fielding1}',
            f'avg_rating_fielding2: {self.avg_rating_fielding2}',
            f'avg_rating_fielding3: {self.avg_rating_fielding3}',
            f'avg_rating_fielding4: {self.avg_rating_fielding4}',
            f'avg_rating_fielding5: {self.avg_rating_fielding5}',
            f'avg_rating_fielding6: {self.avg_rating_fielding6}',
            f'avg_rating_fielding7: {self.avg_rating_fielding7}',
            f'avg_rating_fielding8: {self.avg_rating_fielding8}',
            f'avg_rating_fielding9: {self.avg_rating_fielding9}',
            f'avg_rating_overall: {self.avg_rating_overall}',
            f'avg_rating_age: {self.avg_rating_age}',
            f'league_totals_ab: {self.league_totals_ab}',
            f'league_totals_h: {self.league_totals_h}',
            f'league_totals_d: {self.league_totals_d}',
            f'league_totals_t: {self.league_totals_t}',
            f'league_totals_hr: {self.league_totals_hr}',
            f'league_totals_bb: {self.league_totals_bb}',
            f'league_totals_hp: {self.league_totals_hp}',
            f'league_totals_k: {self.league_totals_k}',
            f'league_totals_pa: {self.league_totals_pa}',
            f'league_totals_babip: {self.league_totals_babip}',
            f'league_totals_mod_h: {self.league_totals_mod_h}',
            f'league_totals_mod_d: {self.league_totals_mod_d}',
            f'league_totals_mod_t: {self.league_totals_mod_t}',
            f'league_totals_mod_hr: {self.league_totals_mod_hr}',
            f'league_totals_mod_bb: {self.league_totals_mod_bb}',
            f'league_totals_mod_hp: {self.league_totals_mod_hp}',
            f'league_totals_mod_k: {self.league_totals_mod_k}',
            f'league_totals_mod_babip: {self.league_totals_mod_babip}',
            f'ml_equivalencies_avg: {self.ml_equivalencies_avg}',
            f'ml_equivalencies_hr: {self.ml_equivalencies_hr}',
            f'ml_equivalencies_eb: {self.ml_equivalencies_eb}',
            f'ml_equivalencies_bb: {self.ml_equivalencies_bb}',
            f'ml_equivalencies_k: {self.ml_equivalencies_k}',
            f'ml_equivalencies_hp: {self.ml_equivalencies_hp}',
            f'player_creation_modifier_contact: {self.player_creation_modifier_contact}',
            f'player_creation_modifier_gap: {self.player_creation_modifier_gap}',
            f'player_creation_modifier_power: {self.player_creation_modifier_power}',
            f'player_creation_modifier_eye: {self.player_creation_modifier_eye}',
            f'player_creation_modifier_strikeouts: {self.player_creation_modifier_strikeouts}',
            f'player_creation_modifier_stuff: {self.player_creation_modifier_stuff}',
            f'player_creation_modifier_movement: {self.player_creation_modifier_movement}',
            f'player_creation_modifier_control: {self.player_creation_modifier_control}',
            f'player_creation_modifier_speed: {self.player_creation_modifier_speed}',
            f'player_creation_modifier_fielding: {self.player_creation_modifier_fielding}',
            f'financial_coefficient: {self.financial_coefficient}',
            f'world_start_year: {self.world_start_year}',
            f'current_date: {self.current_date}',
            f'background_color_id: {self.background_color_id}',
            f'text_color_id: {self.text_color_id}',
            f'scouting_coach_id: {self.scouting_coach_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = League(*row)
        data[obj.league_id] = obj

    return data
