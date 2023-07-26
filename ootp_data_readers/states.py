import pandas


class State:
    def __init__(self, state_id, nation_id, name, abbreviation, population, main_language_id):
        self.state_id = state_id
        self.nation_id = nation_id
        self.name = name
        self.abbreviation = abbreviation
        self.population = population
        self.main_language_id = main_language_id
    
    def __str__(self):
        return "\n".join([
            f'state_id: {self.state_id}',
            f'nation_id: {self.nation_id}',
            f'name: {self.name}',
            f'abbreviation: {self.abbreviation}',
            f'population: {self.population}',
            f'main_language_id: {self.main_language_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = State(*row)
        data[obj.state_id] = obj

    return data
