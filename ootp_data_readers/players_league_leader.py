import pandas


class PlayersLeagueLeaderEntry:
    def __init__(self, player_id, league_id, sub_league_id, year, category, place, amount):
        self.player_id = player_id
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.year = year
        self.category = category
        self.place = place
        self.amount = amount
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'year: {self.year}',
            f'category: {self.category}',
            f'place: {self.place}',
            f'amount: {self.amount}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersLeagueLeaderEntry(*row)
        data.append(obj)

    return data
