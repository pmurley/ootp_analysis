import pandas


class HumanManager:
    def __init__(self, human_manager_id, is_commish, first_name, last_name, nick_name, age, date_of_birth, city_of_birth_id, nation_id, second_nation_id, weight, height, retired, free_agent, league_id, last_league_id, team_id, last_team_id, organization_id, last_organization_id, language_ids0, language_ids1, uniform_number, experience, person_type, bats, throws, personality_greed, personality_loyalty, personality_play_for_winner, personality_work_ethic, personality_intelligence, personality_leader):
        self.human_manager_id = human_manager_id
        self.is_commish = is_commish
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.city_of_birth_id = city_of_birth_id
        self.nation_id = nation_id
        self.second_nation_id = second_nation_id
        self.weight = weight
        self.height = height
        self.retired = retired
        self.free_agent = free_agent
        self.league_id = league_id
        self.last_league_id = last_league_id
        self.team_id = team_id
        self.last_team_id = last_team_id
        self.organization_id = organization_id
        self.last_organization_id = last_organization_id
        self.language_ids0 = language_ids0
        self.language_ids1 = language_ids1
        self.uniform_number = uniform_number
        self.experience = experience
        self.person_type = person_type
        self.bats = bats
        self.throws = throws
        self.personality_greed = personality_greed
        self.personality_loyalty = personality_loyalty
        self.personality_play_for_winner = personality_play_for_winner
        self.personality_work_ethic = personality_work_ethic
        self.personality_intelligence = personality_intelligence
        self.personality_leader = personality_leader
    
    def __str__(self):
        return "\n".join([
            f'human_manager_id: {self.human_manager_id}',
            f'is_commish: {self.is_commish}',
            f'first_name: {self.first_name}',
            f'last_name: {self.last_name}',
            f'nick_name: {self.nick_name}',
            f'age: {self.age}',
            f'date_of_birth: {self.date_of_birth}',
            f'city_of_birth_id: {self.city_of_birth_id}',
            f'nation_id: {self.nation_id}',
            f'second_nation_id: {self.second_nation_id}',
            f'weight: {self.weight}',
            f'height: {self.height}',
            f'retired: {self.retired}',
            f'free_agent: {self.free_agent}',
            f'league_id: {self.league_id}',
            f'last_league_id: {self.last_league_id}',
            f'team_id: {self.team_id}',
            f'last_team_id: {self.last_team_id}',
            f'organization_id: {self.organization_id}',
            f'last_organization_id: {self.last_organization_id}',
            f'language_ids0: {self.language_ids0}',
            f'language_ids1: {self.language_ids1}',
            f'uniform_number: {self.uniform_number}',
            f'experience: {self.experience}',
            f'person_type: {self.person_type}',
            f'bats: {self.bats}',
            f'throws: {self.throws}',
            f'personality_greed: {self.personality_greed}',
            f'personality_loyalty: {self.personality_loyalty}',
            f'personality_play_for_winner: {self.personality_play_for_winner}',
            f'personality_work_ethic: {self.personality_work_ethic}',
            f'personality_intelligence: {self.personality_intelligence}',
            f'personality_leader: {self.personality_leader}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = HumanManager(*row)
        data[obj.human_manager_id] = obj

    return data

