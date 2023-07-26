import pandas


class TradeHistoryEntry:
    def __init__(self, date, summary, message_id, team_id_0, player_id_0_0, player_id_0_1, player_id_0_2, player_id_0_3, player_id_0_4, player_id_0_5, player_id_0_6, player_id_0_7, player_id_0_8, player_id_0_9, draft_round_0_0, draft_team_0_0, draft_round_0_1, draft_team_0_1, draft_round_0_2, draft_team_0_2, draft_round_0_3, draft_team_0_3, draft_round_0_4, draft_team_0_4, cash_0, iafa_cap_0, team_id_1, player_id_1_0, player_id_1_1, player_id_1_2, player_id_1_3, player_id_1_4, player_id_1_5, player_id_1_6, player_id_1_7, player_id_1_8, player_id_1_9, draft_round_1_0, draft_team_1_0, draft_round_1_1, draft_team_1_1, draft_round_1_2, draft_team_1_2, draft_round_1_3, draft_team_1_3, draft_round_1_4, draft_team_1_4, cash_1, iafa_cap_1):
        self.date = date
        self.summary = summary
        self.message_id = message_id
        self.team_id_0 = team_id_0
        self.player_id_0_0 = player_id_0_0
        self.player_id_0_1 = player_id_0_1
        self.player_id_0_2 = player_id_0_2
        self.player_id_0_3 = player_id_0_3
        self.player_id_0_4 = player_id_0_4
        self.player_id_0_5 = player_id_0_5
        self.player_id_0_6 = player_id_0_6
        self.player_id_0_7 = player_id_0_7
        self.player_id_0_8 = player_id_0_8
        self.player_id_0_9 = player_id_0_9
        self.draft_round_0_0 = draft_round_0_0
        self.draft_team_0_0 = draft_team_0_0
        self.draft_round_0_1 = draft_round_0_1
        self.draft_team_0_1 = draft_team_0_1
        self.draft_round_0_2 = draft_round_0_2
        self.draft_team_0_2 = draft_team_0_2
        self.draft_round_0_3 = draft_round_0_3
        self.draft_team_0_3 = draft_team_0_3
        self.draft_round_0_4 = draft_round_0_4
        self.draft_team_0_4 = draft_team_0_4
        self.cash_0 = cash_0
        self.iafa_cap_0 = iafa_cap_0
        self.team_id_1 = team_id_1
        self.player_id_1_0 = player_id_1_0
        self.player_id_1_1 = player_id_1_1
        self.player_id_1_2 = player_id_1_2
        self.player_id_1_3 = player_id_1_3
        self.player_id_1_4 = player_id_1_4
        self.player_id_1_5 = player_id_1_5
        self.player_id_1_6 = player_id_1_6
        self.player_id_1_7 = player_id_1_7
        self.player_id_1_8 = player_id_1_8
        self.player_id_1_9 = player_id_1_9
        self.draft_round_1_0 = draft_round_1_0
        self.draft_team_1_0 = draft_team_1_0
        self.draft_round_1_1 = draft_round_1_1
        self.draft_team_1_1 = draft_team_1_1
        self.draft_round_1_2 = draft_round_1_2
        self.draft_team_1_2 = draft_team_1_2
        self.draft_round_1_3 = draft_round_1_3
        self.draft_team_1_3 = draft_team_1_3
        self.draft_round_1_4 = draft_round_1_4
        self.draft_team_1_4 = draft_team_1_4
        self.cash_1 = cash_1
        self.iafa_cap_1 = iafa_cap_1
    
    def __str__(self):
        return "\n".join([
            f'date: {self.date}',
            f'summary: {self.summary}',
            f'message_id: {self.message_id}',
            f'team_id_0: {self.team_id_0}',
            f'player_id_0_0: {self.player_id_0_0}',
            f'player_id_0_1: {self.player_id_0_1}',
            f'player_id_0_2: {self.player_id_0_2}',
            f'player_id_0_3: {self.player_id_0_3}',
            f'player_id_0_4: {self.player_id_0_4}',
            f'player_id_0_5: {self.player_id_0_5}',
            f'player_id_0_6: {self.player_id_0_6}',
            f'player_id_0_7: {self.player_id_0_7}',
            f'player_id_0_8: {self.player_id_0_8}',
            f'player_id_0_9: {self.player_id_0_9}',
            f'draft_round_0_0: {self.draft_round_0_0}',
            f'draft_team_0_0: {self.draft_team_0_0}',
            f'draft_round_0_1: {self.draft_round_0_1}',
            f'draft_team_0_1: {self.draft_team_0_1}',
            f'draft_round_0_2: {self.draft_round_0_2}',
            f'draft_team_0_2: {self.draft_team_0_2}',
            f'draft_round_0_3: {self.draft_round_0_3}',
            f'draft_team_0_3: {self.draft_team_0_3}',
            f'draft_round_0_4: {self.draft_round_0_4}',
            f'draft_team_0_4: {self.draft_team_0_4}',
            f'cash_0: {self.cash_0}',
            f'iafa_cap_0: {self.iafa_cap_0}',
            f'team_id_1: {self.team_id_1}',
            f'player_id_1_0: {self.player_id_1_0}',
            f'player_id_1_1: {self.player_id_1_1}',
            f'player_id_1_2: {self.player_id_1_2}',
            f'player_id_1_3: {self.player_id_1_3}',
            f'player_id_1_4: {self.player_id_1_4}',
            f'player_id_1_5: {self.player_id_1_5}',
            f'player_id_1_6: {self.player_id_1_6}',
            f'player_id_1_7: {self.player_id_1_7}',
            f'player_id_1_8: {self.player_id_1_8}',
            f'player_id_1_9: {self.player_id_1_9}',
            f'draft_round_1_0: {self.draft_round_1_0}',
            f'draft_team_1_0: {self.draft_team_1_0}',
            f'draft_round_1_1: {self.draft_round_1_1}',
            f'draft_team_1_1: {self.draft_team_1_1}',
            f'draft_round_1_2: {self.draft_round_1_2}',
            f'draft_team_1_2: {self.draft_team_1_2}',
            f'draft_round_1_3: {self.draft_round_1_3}',
            f'draft_team_1_3: {self.draft_team_1_3}',
            f'draft_round_1_4: {self.draft_round_1_4}',
            f'draft_team_1_4: {self.draft_team_1_4}',
            f'cash_1: {self.cash_1}',
            f'iafa_cap_1: {self.iafa_cap_1}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = TradeHistoryEntry(*row)
        data.append(obj)

    return data
