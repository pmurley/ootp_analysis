import os
import pandas as pd

CLASS_NAMES = {
    'cities': 'City',
    'coaches': 'Coach',
    'continents': 'Continent',
    'divisions': 'Division',
    'games': 'Game',
    'games_score': 'GameScore',
    'human_managers': 'HumanManager',
    'human_manager_history': 'HumanManagerHistory',
    'human_manager_history_batting_stats': 'HumanManagerHistoryBattingStats',
    'human_manager_history_fielding_stats_stats': 'HumanManagerHistoryFieldingStatsStats',
    'human_manager_history_financials': 'HumanManagerHistoryFinancials',
    'human_manager_history_pitching_stats': 'HumanManagerHistoryPitchingStats',
    'human_manager_history_record': 'HumanManagerHistoryRecord',
    'languages': 'Language',
    'language_data': 'LanguageData',
    'leagues': 'League',
    'league_events': 'LeagueEvent',
    'league_history': 'LeagueHistoryEntry',
    'league_history_all_star': 'LeagueHistoryAllStarEntry',
    'league_history_batting_stats': 'LeagueHistoryBattingStatsEntry',
    'league_history_fielding_stats': 'LeagueHistoryFieldingStatsEntry',
    'league_history_pitching_stats': 'LeagueHistoryPitchingStatsEntry',
    'league_playoffs': 'LeaguePlayoffsEntry',
    'league_playoff_fixtures': 'LeaguePlayoffFixture',
    'messages': 'Message',
    'nations': 'Nation',
    'parks': 'Park',
    'players': 'Player',
    'players_at_bat_batting_stats': 'PlayersAtBatBattingStatsEntry',
    'players_awards': 'PlayersAwardsEntry',
    'players_batting': 'PlayersBattingEntry',
    'players_career_batting_stats': 'PlayersCareerBattingStatsEntry',
    'players_career_fielding_stats': 'PlayersCareerFieldingStatsEntry',
    'players_career_pitching_stats': 'PlayersCareerPitchingStatsEntry',
    'players_contract': 'PlayersContractEntry',
    'players_contract_extension': 'PlayersContractExtensionEntry',
    'players_fielding': 'PlayersFieldingEntry',
    'players_game_batting': 'PlayersGameBattingEntry',
    'players_game_pitching_stats': 'PlayersGamePitchingStatsEntry',
    'players_individual_batting_stats': 'PlayersIndividualBattingStatsEntry',
    'players_injury_history': 'PlayersInjuryHistoryEntry',
    'players_league_leader': 'PlayersLeagueLeaderEntry',
    'players_pitching': 'PlayersPitchingEntry',
    'players_roster_status': 'PlayersRosterStatusEntry',
    'players_salary_history': 'PlayersSalaryHistoryEntry',
    'players_streak': 'PlayersStreakEntry',
    'players_value': 'PlayersValueEntry',
    'projected_starting_pitchers': 'ProjectedStartingPitchersEntry',
    'states': 'State',
    'sub_leagues': 'SubLeague',
    'teams': 'Team',
    'team_affiliations': 'TeamAffiliationEntry',
    'team_batting_stats': 'TeamBattingStatsEntry',
    'team_bullpen_pitching_stats': 'TeamBullpenPitchingStatsEntry',
    'team_fielding_stats_stats': 'TeamFieldingStatsStatsEntry',
    'team_financials': 'TeamFinancialsEntry',
    'team_history': 'TeamHistoryEntry',
    'team_history_batting_stats': 'TeamHistoryBattingStatsEntry',
    'team_history_fielding_stats_stats': 'TeamHistoryFieldingStatsStatsEntry',
    'team_history_financials': 'TeamHistoryFinancialsEntry',
    'team_history_pitching_stats': 'TeamHistoryPitchingStatsEntry',
    'team_history_record': 'TeamHistoryRecordEntry',
    'team_last_financials': 'TeamLastFinancialsEntry',
    'team_pitching_stats': 'TeamPitchingStatsEntry',
    'team_record': 'TeamRecordEntry',
    'team_relations': 'TeamRelationsEntry',
    'team_roster': 'TeamRosterEntry',
    'team_roster_staff': 'TeamRosterStaffEntry',
    'team_starting_pitching_stats': 'TeamStartingPitchingStatsEntry',
    'trade_history': 'TradeHistoryEntry'
}

def generate_class_string(csv_file, name):
    # Read the first row of the CSV file
    df = pd.read_csv(csv_file, nrows=1)

    # Get the column headers
    headers = df.columns.tolist()

    # Create the class definition
    class_name = name
    init_body = "\n        ".join(f"self.{header} = {header}" for header in headers)
    str_body  = "\n            ".join(f"f'{header}: {{self.{header}}}'," for header in headers)

    class_definition = f"""class {class_name}:
    def __init__(self, {', '.join(headers)}):
        {init_body}
    
    def __str__(self):
        return "\\n".join([
            {str_body}
        ])
"""

    return class_definition


def main():
    files = os.listdir('../data/2025')
    for f in files:
        thing = f.split('.')[0]
        class_name = CLASS_NAMES[thing]
        class_data = generate_class_string('../data/2025/' + f, class_name)
        of = open('../ootp_data_readers/%s' % thing + '.py', 'w')
        of.write(class_data)
        of.close()


if __name__ == '__main__':
    main()