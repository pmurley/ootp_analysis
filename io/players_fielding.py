import pandas


class PlayersFieldingEntry:
    def __init__(self, player_id, team_id, league_id, position, role, fielding_ratings_infield_range, fielding_ratings_infield_arm, fielding_ratings_turn_doubleplay, fielding_ratings_outfield_range, fielding_ratings_outfield_arm, fielding_ratings_catcher_arm, fielding_ratings_catcher_ability, fielding_ratings_infield_error, fielding_ratings_outfield_error, fielding_experience0, fielding_experience1, fielding_experience2, fielding_experience3, fielding_experience4, fielding_experience5, fielding_experience6, fielding_experience7, fielding_experience8, fielding_experience9, fielding_rating_pos1, fielding_rating_pos2, fielding_rating_pos3, fielding_rating_pos4, fielding_rating_pos5, fielding_rating_pos6, fielding_rating_pos7, fielding_rating_pos8, fielding_rating_pos9):
        self.player_id = player_id
        self.team_id = team_id
        self.league_id = league_id
        self.position = position
        self.role = role
        self.fielding_ratings_infield_range = fielding_ratings_infield_range
        self.fielding_ratings_infield_arm = fielding_ratings_infield_arm
        self.fielding_ratings_turn_doubleplay = fielding_ratings_turn_doubleplay
        self.fielding_ratings_outfield_range = fielding_ratings_outfield_range
        self.fielding_ratings_outfield_arm = fielding_ratings_outfield_arm
        self.fielding_ratings_catcher_arm = fielding_ratings_catcher_arm
        self.fielding_ratings_catcher_ability = fielding_ratings_catcher_ability
        self.fielding_ratings_infield_error = fielding_ratings_infield_error
        self.fielding_ratings_outfield_error = fielding_ratings_outfield_error
        self.fielding_experience0 = fielding_experience0
        self.fielding_experience1 = fielding_experience1
        self.fielding_experience2 = fielding_experience2
        self.fielding_experience3 = fielding_experience3
        self.fielding_experience4 = fielding_experience4
        self.fielding_experience5 = fielding_experience5
        self.fielding_experience6 = fielding_experience6
        self.fielding_experience7 = fielding_experience7
        self.fielding_experience8 = fielding_experience8
        self.fielding_experience9 = fielding_experience9
        self.fielding_rating_pos1 = fielding_rating_pos1
        self.fielding_rating_pos2 = fielding_rating_pos2
        self.fielding_rating_pos3 = fielding_rating_pos3
        self.fielding_rating_pos4 = fielding_rating_pos4
        self.fielding_rating_pos5 = fielding_rating_pos5
        self.fielding_rating_pos6 = fielding_rating_pos6
        self.fielding_rating_pos7 = fielding_rating_pos7
        self.fielding_rating_pos8 = fielding_rating_pos8
        self.fielding_rating_pos9 = fielding_rating_pos9
    
    def __str__(self):
        return "\n".join([
            f'player_id: {self.player_id}',
            f'team_id: {self.team_id}',
            f'league_id: {self.league_id}',
            f'position: {self.position}',
            f'role: {self.role}',
            f'fielding_ratings_infield_range: {self.fielding_ratings_infield_range}',
            f'fielding_ratings_infield_arm: {self.fielding_ratings_infield_arm}',
            f'fielding_ratings_turn_doubleplay: {self.fielding_ratings_turn_doubleplay}',
            f'fielding_ratings_outfield_range: {self.fielding_ratings_outfield_range}',
            f'fielding_ratings_outfield_arm: {self.fielding_ratings_outfield_arm}',
            f'fielding_ratings_catcher_arm: {self.fielding_ratings_catcher_arm}',
            f'fielding_ratings_catcher_ability: {self.fielding_ratings_catcher_ability}',
            f'fielding_ratings_infield_error: {self.fielding_ratings_infield_error}',
            f'fielding_ratings_outfield_error: {self.fielding_ratings_outfield_error}',
            f'fielding_experience0: {self.fielding_experience0}',
            f'fielding_experience1: {self.fielding_experience1}',
            f'fielding_experience2: {self.fielding_experience2}',
            f'fielding_experience3: {self.fielding_experience3}',
            f'fielding_experience4: {self.fielding_experience4}',
            f'fielding_experience5: {self.fielding_experience5}',
            f'fielding_experience6: {self.fielding_experience6}',
            f'fielding_experience7: {self.fielding_experience7}',
            f'fielding_experience8: {self.fielding_experience8}',
            f'fielding_experience9: {self.fielding_experience9}',
            f'fielding_rating_pos1: {self.fielding_rating_pos1}',
            f'fielding_rating_pos2: {self.fielding_rating_pos2}',
            f'fielding_rating_pos3: {self.fielding_rating_pos3}',
            f'fielding_rating_pos4: {self.fielding_rating_pos4}',
            f'fielding_rating_pos5: {self.fielding_rating_pos5}',
            f'fielding_rating_pos6: {self.fielding_rating_pos6}',
            f'fielding_rating_pos7: {self.fielding_rating_pos7}',
            f'fielding_rating_pos8: {self.fielding_rating_pos8}',
            f'fielding_rating_pos9: {self.fielding_rating_pos9}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = PlayersFieldingEntry(*row)
        data[obj.player_id] = obj

    return data
