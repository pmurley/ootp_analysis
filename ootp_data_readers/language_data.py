import pandas


class LanguageData:
    def __init__(self, parent_table, parent_id, language_id, percentage):
        self.parent_table = parent_table
        self.parent_id = parent_id
        self.language_id = language_id
        self.percentage = percentage
    
    def __str__(self):
        return "\n".join([
            f'parent_table: {self.parent_table}',
            f'parent_id: {self.parent_id}',
            f'language_id: {self.language_id}',
            f'percentage: {self.percentage}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LanguageData(*row)
        data.append(obj)

    return data
