from analysis import mappings as m


class CoachDataPoint:
    def __init__(self, row):
        self.nick_name = row[3]
        self.age = row[4]
        self.weight = row[8]
        self.height = row[9]
        self.position = row[10]
        self.experience = row[11]
        self.occupation = row[12]
        self.team_id = row[13]
        self.contract_salary = row[16]
        self.contract_years = row[17]
        self.contract_extension_salary = row[18]
        self.contract_extension_years = row[19]
        self.scout_major = row[20]
        self.scout_minor = row[21]
        self.scout_international = row[22]
        self.scout_amateur = row[23]
        self.scout_amateur_preference = row[24]
        self.teach_hitting = row[25]
        self.teach_pitching = row[26]
        self.teach_c = row[27]
        self.teach_if = row[28]
        self.teach_of = row[29]
        self.handle_veterans = row[30]
        self.handle_rookies = row[31]
        self.handle_players = row[32]
        self.heal_legs = row[33]
        self.heal_arms = row[34]
        self.heal_back = row[35]
        self.heal_other = row[36]
        self.heal_rest = row[37]
        self.management_style = row[38]
        self.personality = row[39]
        self.hitting_focus = row[5]
        self.pitching_focus = row[5]
        self.training_focus = row[5]
        self.teach_running = row[43]
        self.prevent_legs = row[44]
        self.prevent_arms = row[45]
        self.prevent_back = row[46]
        self.prevent_other = row[47]
        self.draft_value = row[87]
        self.intl_fa_value = row[88]
        self.develop_value = row[89]
        self.ratings_value = row[90]
        self.manager_value = row[91]
        self.pitching_coach_value = row[92]
        self.hitting_coach_value = row[93]
        self.scout_value = row[94]
        self.doctor_value = row[95]
        self.basecoach_value = row[96]
        self.positive_relation = row[97]
        self.negative_relation = row[98]


class Coach:
    def __init__(self, coach_id,first_name,last_name, date_of_birth):
        self.coach_id = coach_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.data_points = {}

    def __str__(self):
        s = self.first_name + ' ' + self.last_name
        return s

    def add_data_point(self, row):
        self.data_points[row[4]] = CoachDataPoint(row)
