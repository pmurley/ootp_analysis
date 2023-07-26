import pandas


class PlayersAwardsEntry:
    def __init__(self, player_id, league_id, team_id, sub_league_id, award_id, year, season, position, day, month, finish):
        self.player_id = player_id
        self.league_id = league_id
        self.team_id = team_id
        self.sub_league_id = sub_league_id
        self.award_id = award_id
        self.year = year
        self.season = season
        self.position = position
        self.day = day
        self.month = month
        self.finish = finish
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'league_id: {self.league_id}',
            f'team_id: {self.team_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'award_id: {self.award_id}',
            f'year: {self.year}',
            f'season: {self.season}',
            f'position: {self.position}',
            f'day: {self.day}',
            f'month: {self.month}',
            f'finish: {self.finish}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersAwardsEntry(*row)
        data.append(obj)

    return data
