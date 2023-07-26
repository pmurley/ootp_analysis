import pandas


class LeagueEvent:
    def __init__(self, league_id, start_date, type, event_over, deleted, name, needs_human_action, real_sim_date):
        self.league_id = league_id
        self.start_date = start_date
        self.type = type
        self.event_over = event_over
        self.deleted = deleted
        self.name = name
        self.needs_human_action = needs_human_action
        self.real_sim_date = real_sim_date
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'start_date: {self.start_date}',
            f'type: {self.type}',
            f'event_over: {self.event_over}',
            f'deleted: {self.deleted}',
            f'name: {self.name}',
            f'needs_human_action: {self.needs_human_action}',
            f'real_sim_date: {self.real_sim_date}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeagueEvent(*row)
        data.append(obj)

    return data
