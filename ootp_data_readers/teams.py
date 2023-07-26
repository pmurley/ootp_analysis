import pandas


class Team:
    def __init__(self, team_id, name, abbr, nickname, logo_file_name, city_id, park_id, league_id, sub_league_id, division_id, nation_id, parent_team_id, level, prevent_any_moves, human_team, human_id, gender, background_color_id, text_color_id, ballcaps_main_color_id, ballcaps_visor_color_id, jersey_main_color_id, jersey_away_color_id, jersey_secondary_color_id, jersey_pin_stripes_color_id, allstar_team, historical_id):
        self.team_id = team_id
        self.name = name
        self.abbr = abbr
        self.nickname = nickname
        self.logo_file_name = logo_file_name
        self.city_id = city_id
        self.park_id = park_id
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.nation_id = nation_id
        self.parent_team_id = parent_team_id
        self.level = level
        self.prevent_any_moves = prevent_any_moves
        self.human_team = human_team
        self.human_id = human_id
        self.gender = gender
        self.background_color_id = background_color_id
        self.text_color_id = text_color_id
        self.ballcaps_main_color_id = ballcaps_main_color_id
        self.ballcaps_visor_color_id = ballcaps_visor_color_id
        self.jersey_main_color_id = jersey_main_color_id
        self.jersey_away_color_id = jersey_away_color_id
        self.jersey_secondary_color_id = jersey_secondary_color_id
        self.jersey_pin_stripes_color_id = jersey_pin_stripes_color_id
        self.allstar_team = allstar_team
        self.historical_id = historical_id
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'name: {self.name}',
            f'abbr: {self.abbr}',
            f'nickname: {self.nickname}',
            f'logo_file_name: {self.logo_file_name}',
            f'city_id: {self.city_id}',
            f'park_id: {self.park_id}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'nation_id: {self.nation_id}',
            f'parent_team_id: {self.parent_team_id}',
            f'level: {self.level}',
            f'prevent_any_moves: {self.prevent_any_moves}',
            f'human_team: {self.human_team}',
            f'human_id: {self.human_id}',
            f'gender: {self.gender}',
            f'background_color_id: {self.background_color_id}',
            f'text_color_id: {self.text_color_id}',
            f'ballcaps_main_color_id: {self.ballcaps_main_color_id}',
            f'ballcaps_visor_color_id: {self.ballcaps_visor_color_id}',
            f'jersey_main_color_id: {self.jersey_main_color_id}',
            f'jersey_away_color_id: {self.jersey_away_color_id}',
            f'jersey_secondary_color_id: {self.jersey_secondary_color_id}',
            f'jersey_pin_stripes_color_id: {self.jersey_pin_stripes_color_id}',
            f'allstar_team: {self.allstar_team}',
            f'historical_id: {self.historical_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Team(*row)
        data[obj.team_id] = obj

    return data
