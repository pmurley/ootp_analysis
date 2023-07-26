import pandas


class PlayersContractEntry:
    def __init__(self, player_id, team_id, league_id, position, role, is_major, no_trade, last_year_team_option, last_year_player_option, last_year_vesting_option, next_last_year_team_option, next_last_year_player_option, next_last_year_vesting_option, contract_team_id, contract_league_id, season_year, salary0, salary1, salary2, salary3, salary4, salary5, salary6, salary7, salary8, salary9, salary10, salary11, salary12, salary13, salary14, years, current_year, minimum_pa, minimum_pa_bonus, minimum_ip, minimum_ip_bonus, mvp_bonus, cyyoung_bonus, allstar_bonus, next_last_year_option_buyout, last_year_option_buyout, opt_out, opt_out_relegation, retained):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.is_major = is_major
        self.no_trade = no_trade
        self.last_year_team_option = last_year_team_option
        self.last_year_player_option = last_year_player_option
        self.last_year_vesting_option = last_year_vesting_option
        self.next_last_year_team_option = next_last_year_team_option
        self.next_last_year_player_option = next_last_year_player_option
        self.next_last_year_vesting_option = next_last_year_vesting_option
        self.contract_team_id = contract_team_id
        self.contract_league_id = contract_league_id
        self.season_year = season_year
        self.salary0 = salary0
        self.salary1 = salary1
        self.salary2 = salary2
        self.salary3 = salary3
        self.salary4 = salary4
        self.salary5 = salary5
        self.salary6 = salary6
        self.salary7 = salary7
        self.salary8 = salary8
        self.salary9 = salary9
        self.salary10 = salary10
        self.salary11 = salary11
        self.salary12 = salary12
        self.salary13 = salary13
        self.salary14 = salary14
        self.years = years
        self.current_year = current_year
        self.minimum_pa = minimum_pa
        self.minimum_pa_bonus = minimum_pa_bonus
        self.minimum_ip = minimum_ip
        self.minimum_ip_bonus = minimum_ip_bonus
        self.mvp_bonus = mvp_bonus
        self.cyyoung_bonus = cyyoung_bonus
        self.allstar_bonus = allstar_bonus
        self.next_last_year_option_buyout = next_last_year_option_buyout
        self.last_year_option_buyout = last_year_option_buyout
        self.opt_out = opt_out
        self.opt_out_relegation = opt_out_relegation
        self.retained = retained
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'is_major: {self.is_major}',
            f'no_trade: {self.no_trade}',
            f'last_year_team_option: {self.last_year_team_option}',
            f'last_year_player_option: {self.last_year_player_option}',
            f'last_year_vesting_option: {self.last_year_vesting_option}',
            f'next_last_year_team_option: {self.next_last_year_team_option}',
            f'next_last_year_player_option: {self.next_last_year_player_option}',
            f'next_last_year_vesting_option: {self.next_last_year_vesting_option}',
            f'contract_team_id: {self.contract_team_id}',
            f'contract_league_id: {self.contract_league_id}',
            f'season_year: {self.season_year}',
            f'salary0: {self.salary0}',
            f'salary1: {self.salary1}',
            f'salary2: {self.salary2}',
            f'salary3: {self.salary3}',
            f'salary4: {self.salary4}',
            f'salary5: {self.salary5}',
            f'salary6: {self.salary6}',
            f'salary7: {self.salary7}',
            f'salary8: {self.salary8}',
            f'salary9: {self.salary9}',
            f'salary10: {self.salary10}',
            f'salary11: {self.salary11}',
            f'salary12: {self.salary12}',
            f'salary13: {self.salary13}',
            f'salary14: {self.salary14}',
            f'years: {self.years}',
            f'current_year: {self.current_year}',
            f'minimum_pa: {self.minimum_pa}',
            f'minimum_pa_bonus: {self.minimum_pa_bonus}',
            f'minimum_ip: {self.minimum_ip}',
            f'minimum_ip_bonus: {self.minimum_ip_bonus}',
            f'mvp_bonus: {self.mvp_bonus}',
            f'cyyoung_bonus: {self.cyyoung_bonus}',
            f'allstar_bonus: {self.allstar_bonus}',
            f'next_last_year_option_buyout: {self.next_last_year_option_buyout}',
            f'last_year_option_buyout: {self.last_year_option_buyout}',
            f'opt_out: {self.opt_out}',
            f'opt_out_relegation: {self.opt_out_relegation}',
            f'retained: {self.retained}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersContractEntry(*row)
        data.append(obj)

    return data
