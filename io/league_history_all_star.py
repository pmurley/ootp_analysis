import pandas


class LeagueHistoryAllStarEntry:
    def __init__(self, league_id, sub_league_id, year, all_star_pos, all_star):
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.year = year
        self.all_star_pos = all_star_pos
        self.all_star = all_star
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'year: {self.year}',
            f'all_star_pos: {self.all_star_pos}',
            f'all_star: {self.all_star}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueHistoryAllStarEntry(*row)
        data.append(obj)

    return data
