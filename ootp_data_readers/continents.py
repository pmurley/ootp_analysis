import pandas


class Continent:
    def __init__(self, continent_id, name, abbreviation, demonym, population, main_language_id):
        self.continent_id = continent_id
        self.name = name
        self.abbreviation = abbreviation
        self.demonym = demonym
        self.population = population
        self.main_language_id = main_language_id
    
    def __str__(self):
        return "\n".join([
            f'continent_id: {self.continent_id}',
            f'name: {self.name}',
            f'abbreviation: {self.abbreviation}',
            f'demonym: {self.demonym}',
            f'population: {self.population}',
            f'main_language_id: {self.main_language_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Continent(*row)
        data[obj.continent_id] = obj

    return data
