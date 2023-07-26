#!/usr/bin/env python3
import csv

from analysis import coach
import pandas as pd
from analysis import mappings as m
from pprint import pprint
import io


def test_read_file():
    cities_data = parse_cities('data/2025/cities.csv')
    for city_id, city in cities_data.items():
        print(city)


def parse_cities(path):
    # Read the CSV file
    df = pd.read_csv(path)

    # Create a dict to hold the City objects
    city_dict = {}

    # Iterate over the DataFrame rows as (index, Series) pairs
    for index, row in df.iterrows():
        # Convert each row into a City object
        city = City(*row)
        # Store the City object in the dictionary using city_id as the key
        city_dict[city.city_id] = city

    return city_dict


def main():
    test_read_file()
    return


if __name__ == '__main__':
    main()

