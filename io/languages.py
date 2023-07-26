import pandas


class Language:
    def __init__(self, language_id, name):
        self.language_id = language_id
        self.name = name
    
    def __str__(self):
        return "\n".join([
            f'language_id: {self.language_id}',
            f'name: {self.name}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Language(*row)
        data[obj.language_id] = obj.name

    return data
