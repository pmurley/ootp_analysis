import pandas


class TeamRosterStaffEntry:
    def __init__(self, team_id, head_scout, manager, general_manager, pitching_coach, hitting_coach, bench_coach, owner, doctor, first_base_coach, third_base_coach):
        self.team_id = team_id
        self.head_scout = head_scout
        self.manager = manager
        self.general_manager = general_manager
        self.pitching_coach = pitching_coach
        self.hitting_coach = hitting_coach
        self.bench_coach = bench_coach
        self.owner = owner
        self.doctor = doctor
        self.first_base_coach = first_base_coach
        self.third_base_coach = third_base_coach
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'head_scout: {self.head_scout}',
            f'manager: {self.manager}',
            f'general_manager: {self.general_manager}',
            f'pitching_coach: {self.pitching_coach}',
            f'hitting_coach: {self.hitting_coach}',
            f'bench_coach: {self.bench_coach}',
            f'owner: {self.owner}',
            f'doctor: {self.doctor}',
            f'first_base_coach: {self.first_base_coach}',
            f'third_base_coach: {self.third_base_coach}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = TeamRosterStaffEntry(*row)
        data[obj.team_id] = obj

    return data
