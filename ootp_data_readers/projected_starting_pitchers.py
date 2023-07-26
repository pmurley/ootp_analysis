import pandas


class ProjectedStartingPitchersEntry:
    def __init__(self, team_id, starter_0, starter_1, starter_2, starter_3, starter_4, starter_5, starter_6, starter_7):
        self.team_id = team_id
        self.starter_0 = starter_0
        self.starter_1 = starter_1
        self.starter_2 = starter_2
        self.starter_3 = starter_3
        self.starter_4 = starter_4
        self.starter_5 = starter_5
        self.starter_6 = starter_6
        self.starter_7 = starter_7
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'starter_0: {self.starter_0}',
            f'starter_1: {self.starter_1}',
            f'starter_2: {self.starter_2}',
            f'starter_3: {self.starter_3}',
            f'starter_4: {self.starter_4}',
            f'starter_5: {self.starter_5}',
            f'starter_6: {self.starter_6}',
            f'starter_7: {self.starter_7}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = ProjectedStartingPitchersEntry(*row)
        data.append(obj)

    return data
