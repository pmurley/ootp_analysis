import pandas


class Game:
    def __init__(self, game_id, league_id, home_team, away_team, attendance, date, time, game_type, played, innings, runs0, runs1, hits0, hits1, errors0, errors1, winning_pitcher, losing_pitcher, save_pitcher, starter0, starter1):
        self.game_id = game_id
        self.league_id = league_id
        self.home_team = home_team
        self.away_team = away_team
        self.attendance = attendance
        self.date = date
        self.time = time
        self.game_type = game_type
        self.played = played
        self.innings = innings
        self.runs0 = runs0
        self.runs1 = runs1
        self.hits0 = hits0
        self.hits1 = hits1
        self.errors0 = errors0
        self.errors1 = errors1
        self.winning_pitcher = winning_pitcher
        self.losing_pitcher = losing_pitcher
        self.save_pitcher = save_pitcher
        self.starter0 = starter0
        self.starter1 = starter1
    
    def __str__(self):
        return "\n".join([
            f'game_id: {self.game_id}',
            f'league_id: {self.league_id}',
            f'home_team: {self.home_team}',
            f'away_team: {self.away_team}',
            f'attendance: {self.attendance}',
            f'date: {self.date}',
            f'time: {self.time}',
            f'game_type: {self.game_type}',
            f'played: {self.played}',
            f'innings: {self.innings}',
            f'runs0: {self.runs0}',
            f'runs1: {self.runs1}',
            f'hits0: {self.hits0}',
            f'hits1: {self.hits1}',
            f'errors0: {self.errors0}',
            f'errors1: {self.errors1}',
            f'winning_pitcher: {self.winning_pitcher}',
            f'losing_pitcher: {self.losing_pitcher}',
            f'save_pitcher: {self.save_pitcher}',
            f'starter0: {self.starter0}',
            f'starter1: {self.starter1}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Game(*row)
        data[obj.game_id] = obj

    return data
