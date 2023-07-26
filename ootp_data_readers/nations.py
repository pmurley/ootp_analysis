import pandas


class Nation:
    def __init__(self, nation_id, name, short_name, abbreviation, demonym, population, gender, baseball_quality, continent_id, main_language_id, quality_total, capital_id, use_hardcoded_ml_player_origins, this_is_the_usa):
        self.nation_id = nation_id
        self.name = name
        self.short_name = short_name
        self.abbreviation = abbreviation
        self.demonym = demonym
        self.population = population
        self.gender = gender
        self.baseball_quality = baseball_quality
        self.continent_id = continent_id
        self.main_language_id = main_language_id
        self.quality_total = quality_total
        self.capital_id = capital_id
        self.use_hardcoded_ml_player_origins = use_hardcoded_ml_player_origins
        self.this_is_the_usa = this_is_the_usa
    
    def __str__(self):
        return "\n".join([
            f'nation_id: {self.nation_id}',
            f'name: {self.name}',
            f'short_name: {self.short_name}',
            f'abbreviation: {self.abbreviation}',
            f'demonym: {self.demonym}',
            f'population: {self.population}',
            f'gender: {self.gender}',
            f'baseball_quality: {self.baseball_quality}',
            f'continent_id: {self.continent_id}',
            f'main_language_id: {self.main_language_id}',
            f'quality_total: {self.quality_total}',
            f'capital_id: {self.capital_id}',
            f'use_hardcoded_ml_player_origins: {self.use_hardcoded_ml_player_origins}',
            f'this_is_the_usa: {self.this_is_the_usa}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Nation(*row)
        data[obj.nation_id] = obj

    return data
