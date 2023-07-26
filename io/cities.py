import pandas


class City:
    def __init__(self, city_id, nation_id, state_id, name, abbreviation, latitude, longitude, population, main_language_id):
        self.city_id = city_id
        self.nation_id = nation_id
        self.state_id = state_id
        self.name = name
        self.abbreviation = abbreviation
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        self.main_language_id = main_language_id
    
    def __str__(self):
        return "\n".join([
            f'city_id: {self.city_id}',
            f'nation_id: {self.nation_id}',
            f'state_id: {self.state_id}',
            f'name: {self.name}',
            f'abbreviation: {self.abbreviation}',
            f'latitude: {self.latitude}',
            f'longitude: {self.longitude}',
            f'population: {self.population}',
            f'main_language_id: {self.main_language_id}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = City(*row)
        data[obj.city_id] = obj

    return data
