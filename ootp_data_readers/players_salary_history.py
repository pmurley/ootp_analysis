import pandas


class PlayersSalaryHistoryEntry:
    def __init__(self, player_id, team_id, year, salary, uniform):
        self.player_id = player_id
        self.team_id = team_id
        self.year = year
        self.salary = salary
        self.uniform = uniform
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'salary: {self.salary}',
            f'uniform: {self.uniform}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = PlayersSalaryHistoryEntry(*row)
        data.append(obj)

    return data
