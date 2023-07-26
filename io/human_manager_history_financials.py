import pandas


class HumanManagerHistoryFinancials:
    def __init__(self, human_manager_id, team_id, year, league_id, sub_league_id, division_id, gate_revenue, media_revenue, merchandising_revenue, other_revenue, revenue_sharing, luxury_sharing, playoff_revenue, cash, player_expenses, staff_expenses, stadium_expenses, attendance, fan_interest, fan_loyalty, fan_modifier, ticket_price, budget, market, owner_expectation):
        self.human_manager_id = human_manager_id
        self.team_id = team_id
        self.year = year
        self.league_id = league_id
        self.sub_league_id = sub_league_id
        self.division_id = division_id
        self.gate_revenue = gate_revenue
        self.media_revenue = media_revenue
        self.merchandising_revenue = merchandising_revenue
        self.other_revenue = other_revenue
        self.revenue_sharing = revenue_sharing
        self.luxury_sharing = luxury_sharing
        self.playoff_revenue = playoff_revenue
        self.cash = cash
        self.player_expenses = player_expenses
        self.staff_expenses = staff_expenses
        self.stadium_expenses = stadium_expenses
        self.attendance = attendance
        self.fan_interest = fan_interest
        self.fan_loyalty = fan_loyalty
        self.fan_modifier = fan_modifier
        self.ticket_price = ticket_price
        self.budget = budget
        self.market = market
        self.owner_expectation = owner_expectation
    
    def __str__(self):
        return "\n".join([
            f'human_manager_id: {self.human_manager_id}',
            f'team_id: {self.team_id}',
            f'year: {self.year}',
            f'league_id: {self.league_id}',
            f'sub_league_id: {self.sub_league_id}',
            f'division_id: {self.division_id}',
            f'gate_revenue: {self.gate_revenue}',
            f'media_revenue: {self.media_revenue}',
            f'merchandising_revenue: {self.merchandising_revenue}',
            f'other_revenue: {self.other_revenue}',
            f'revenue_sharing: {self.revenue_sharing}',
            f'luxury_sharing: {self.luxury_sharing}',
            f'playoff_revenue: {self.playoff_revenue}',
            f'cash: {self.cash}',
            f'player_expenses: {self.player_expenses}',
            f'staff_expenses: {self.staff_expenses}',
            f'stadium_expenses: {self.stadium_expenses}',
            f'attendance: {self.attendance}',
            f'fan_interest: {self.fan_interest}',
            f'fan_loyalty: {self.fan_loyalty}',
            f'fan_modifier: {self.fan_modifier}',
            f'ticket_price: {self.ticket_price}',
            f'budget: {self.budget}',
            f'market: {self.market}',
            f'owner_expectation: {self.owner_expectation}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = HumanManagerHistoryFinancials(*row)
        data.append(obj)

    return data
