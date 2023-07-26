#!/usr/bin/env python3

import ootp_data_readers



def test_read_file():
    cities_data = ootp_data_readers.cities.parse('data/2025/cities.csv')
    for city_id, city in cities_data.items():
        print(city)


def main():
    test_read_file()
    return


if __name__ == '__main__':
    main()

