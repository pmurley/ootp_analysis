import pandas


class Message:
    def __init__(self, message_id, subject, player_id_0, player_id_1, player_id_2, player_id_3, player_id_4, player_id_5, player_id_6, player_id_7, player_id_8, player_id_9, team_id_0, team_id_1, team_id_2, team_id_3, team_id_4, league_id_0, league_id_1, importance, message_type, hype, sender_type, sender_id, recipient_id, trade_id, date, deleted, notify, ongoing_story_id, text_is_modified):
        self.message_id = message_id
        self.subject = subject
        self.player_id_0 = player_id_0
        self.player_id_1 = player_id_1
        self.player_id_2 = player_id_2
        self.player_id_3 = player_id_3
        self.player_id_4 = player_id_4
        self.player_id_5 = player_id_5
        self.player_id_6 = player_id_6
        self.player_id_7 = player_id_7
        self.player_id_8 = player_id_8
        self.player_id_9 = player_id_9
        self.team_id_0 = team_id_0
        self.team_id_1 = team_id_1
        self.team_id_2 = team_id_2
        self.team_id_3 = team_id_3
        self.team_id_4 = team_id_4
        self.league_id_0 = league_id_0
        self.league_id_1 = league_id_1
        self.importance = importance
        self.message_type = message_type
        self.hype = hype
        self.sender_type = sender_type
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.trade_id = trade_id
        self.date = date
        self.deleted = deleted
        self.notify = notify
        self.ongoing_story_id = ongoing_story_id
        self.text_is_modified = text_is_modified
    
    def __str__(self):
        return "\n".join([
            f'message_id: {self.message_id}',
            f'subject: {self.subject}',
            f'player_id_0: {self.player_id_0}',
            f'player_id_1: {self.player_id_1}',
            f'player_id_2: {self.player_id_2}',
            f'player_id_3: {self.player_id_3}',
            f'player_id_4: {self.player_id_4}',
            f'player_id_5: {self.player_id_5}',
            f'player_id_6: {self.player_id_6}',
            f'player_id_7: {self.player_id_7}',
            f'player_id_8: {self.player_id_8}',
            f'player_id_9: {self.player_id_9}',
            f'team_id_0: {self.team_id_0}',
            f'team_id_1: {self.team_id_1}',
            f'team_id_2: {self.team_id_2}',
            f'team_id_3: {self.team_id_3}',
            f'team_id_4: {self.team_id_4}',
            f'league_id_0: {self.league_id_0}',
            f'league_id_1: {self.league_id_1}',
            f'importance: {self.importance}',
            f'message_type: {self.message_type}',
            f'hype: {self.hype}',
            f'sender_type: {self.sender_type}',
            f'sender_id: {self.sender_id}',
            f'recipient_id: {self.recipient_id}',
            f'trade_id: {self.trade_id}',
            f'date: {self.date}',
            f'deleted: {self.deleted}',
            f'notify: {self.notify}',
            f'ongoing_story_id: {self.ongoing_story_id}',
            f'text_is_modified: {self.text_is_modified}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Message(*row)
        data[obj.message_id] = obj

    return data
