import pandas


class LeagueHistoryEntry:
    def __init__(self, league_id, sub_league_id, year, best_hitter_id, best_pitcher_id, best_rookie_id, best_manager_id, best_fielder_id0, best_fielder_id1, best_fielder_id2, best_fielder_id3, best_fielder_id4, best_fielder_id5, best_fielder_id6, best_fielder_id7, best_fielder_id8, best_fielder_id9):
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.year = year
        self.best_hitter_id = best_hitter_id
        self.best_pitcher_id = best_pitcher_id
        self.best_rookie_id = best_rookie_id
        self.best_manager_id = best_manager_id
        self.best_fielder_id0 = best_fielder_id0
        self.best_fielder_id1 = best_fielder_id1
        self.best_fielder_id2 = best_fielder_id2
        self.best_fielder_id3 = best_fielder_id3
        self.best_fielder_id4 = best_fielder_id4
        self.best_fielder_id5 = best_fielder_id5
        self.best_fielder_id6 = best_fielder_id6
        self.best_fielder_id7 = best_fielder_id7
        self.best_fielder_id8 = best_fielder_id8
        self.best_fielder_id9 = best_fielder_id9
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'year: {self.year}',
            f'best_hitter_id: {self.best_hitter_id}',
            f'best_pitcher_id: {self.best_pitcher_id}',
            f'best_rookie_id: {self.best_rookie_id}',
            f'best_manager_id: {self.best_manager_id}',
            f'best_fielder_id0: {self.best_fielder_id0}',
            f'best_fielder_id1: {self.best_fielder_id1}',
            f'best_fielder_id2: {self.best_fielder_id2}',
            f'best_fielder_id3: {self.best_fielder_id3}',
            f'best_fielder_id4: {self.best_fielder_id4}',
            f'best_fielder_id5: {self.best_fielder_id5}',
            f'best_fielder_id6: {self.best_fielder_id6}',
            f'best_fielder_id7: {self.best_fielder_id7}',
            f'best_fielder_id8: {self.best_fielder_id8}',
            f'best_fielder_id9: {self.best_fielder_id9}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueHistoryEntry(*row)
        data.append(obj)

    return data
