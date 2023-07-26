import pandas


class TeamLastFinancialsEntry:
    def __init__(self, team_id, gate_revenue, gate_share_gained, gate_share_lost, season_ticket_revenue, media_revenue, merchandising_revenue, revenue_sharing, luxury_sharing, playoff_revenue, cash, cash_owner, cash_trades, previous_balance, player_expenses, staff_expenses, stadium_expenses, season_tickets, attendance, fan_interest, fan_loyalty, fan_modifier, ticket_price, local_media_contract, local_media_contract_expires, national_media_contract, national_media_contract_expires, scouting_budget, development_budget, draft_budget, draft_expenses, intl_fa_budget, spent_in_intl, budget, market, owner_expectation, total_revenue, total_expenses, financial_balance, budget_balance):
        self.team_id = team_id
        self.gate_revenue = gate_revenue
        self.gate_share_gained = gate_share_gained
        self.gate_share_lost = gate_share_lost
        self.season_ticket_revenue = season_ticket_revenue
        self.media_revenue = media_revenue
        self.merchandising_revenue = merchandising_revenue
        self.revenue_sharing = revenue_sharing
        self.luxury_sharing = luxury_sharing
        self.playoff_revenue = playoff_revenue
        self.cash = cash
        self.cash_owner = cash_owner
        self.cash_trades = cash_trades
        self.previous_balance = previous_balance
        self.player_expenses = player_expenses
        self.staff_expenses = staff_expenses
        self.stadium_expenses = stadium_expenses
        self.season_tickets = season_tickets
        self.attendance = attendance
        self.fan_interest = fan_interest
        self.fan_loyalty = fan_loyalty
        self.fan_modifier = fan_modifier
        self.ticket_price = ticket_price
        self.local_media_contract = local_media_contract
        self.local_media_contract_expires = local_media_contract_expires
        self.national_media_contract = national_media_contract
        self.national_media_contract_expires = national_media_contract_expires
        self.scouting_budget = scouting_budget
        self.development_budget = development_budget
        self.draft_budget = draft_budget
        self.draft_expenses = draft_expenses
        self.intl_fa_budget = intl_fa_budget
        self.spent_in_intl = spent_in_intl
        self.budget = budget
        self.market = market
        self.owner_expectation = owner_expectation
        self.total_revenue = total_revenue
        self.total_expenses = total_expenses
        self.financial_balance = financial_balance
        self.budget_balance = budget_balance
    
    def __str__(self):
        return "\n".join([
            f'team_id: {self.team_id}',
            f'gate_revenue: {self.gate_revenue}',
            f'gate_share_gained: {self.gate_share_gained}',
            f'gate_share_lost: {self.gate_share_lost}',
            f'season_ticket_revenue: {self.season_ticket_revenue}',
            f'media_revenue: {self.media_revenue}',
            f'merchandising_revenue: {self.merchandising_revenue}',
            f'revenue_sharing: {self.revenue_sharing}',
            f'luxury_sharing: {self.luxury_sharing}',
            f'playoff_revenue: {self.playoff_revenue}',
            f'cash: {self.cash}',
            f'cash_owner: {self.cash_owner}',
            f'cash_trades: {self.cash_trades}',
            f'previous_balance: {self.previous_balance}',
            f'player_expenses: {self.player_expenses}',
            f'staff_expenses: {self.staff_expenses}',
            f'stadium_expenses: {self.stadium_expenses}',
            f'season_tickets: {self.season_tickets}',
            f'attendance: {self.attendance}',
            f'fan_interest: {self.fan_interest}',
            f'fan_loyalty: {self.fan_loyalty}',
            f'fan_modifier: {self.fan_modifier}',
            f'ticket_price: {self.ticket_price}',
            f'local_media_contract: {self.local_media_contract}',
            f'local_media_contract_expires: {self.local_media_contract_expires}',
            f'national_media_contract: {self.national_media_contract}',
            f'national_media_contract_expires: {self.national_media_contract_expires}',
            f'scouting_budget: {self.scouting_budget}',
            f'development_budget: {self.development_budget}',
            f'draft_budget: {self.draft_budget}',
            f'draft_expenses: {self.draft_expenses}',
            f'intl_fa_budget: {self.intl_fa_budget}',
            f'spent_in_intl: {self.spent_in_intl}',
            f'budget: {self.budget}',
            f'market: {self.market}',
            f'owner_expectation: {self.owner_expectation}',
            f'total_revenue: {self.total_revenue}',
            f'total_expenses: {self.total_expenses}',
            f'financial_balance: {self.financial_balance}',
            f'budget_balance: {self.budget_balance}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = TeamLastFinancialsEntry(*row)
        data[obj.team_id] = obj

    return data
