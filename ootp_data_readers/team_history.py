import pandas


class TeamHistoryEntry:
    def __init__(self, team_id, year, league_id, sub_league_id, division_id, name, abbr, nickname, best_hitter_id, best_pitcher_id, best_rookie_id, manager_id, made_playoffs, won_playoffs, fired, position_in_division):
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.name = name
        self.abbr = abbr
        self.nickname = nickname
        self.best_hitter_id = best_hitter_id
        self.best_pitcher_id = best_pitcher_id
        self.best_rookie_id = best_rookie_id
        self.manager_id = manager_id
        self.made_playoffs = made_playoffs
        self.won_playoffs = won_playoffs
        self.fired = fired
        self.position_in_division = position_in_division
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'name: {self.name}',
            f'abbr: {self.abbr}',
            f'nickname: {self.nickname}',
            f'best_hitter_id: {self.best_hitter_id}',
            f'best_pitcher_id: {self.best_pitcher_id}',
            f'best_rookie_id: {self.best_rookie_id}',
            f'manager_id: {self.manager_id}',
            f'made_playoffs: {self.made_playoffs}',
            f'won_playoffs: {self.won_playoffs}',
            f'fired: {self.fired}',
            f'position_in_division: {self.position_in_division}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TeamHistoryEntry(*row)
        data.append(obj)

    return data
