import pandas


class Park:
    def __init__(self, park_id, dimensions_x, dimensions_y, batter_left_x, batter_left_y, batter_right_x, batter_right_y, bases_x0, bases_x1, bases_x2, bases_y0, bases_y1, bases_y2, positions_x0, positions_x1, positions_x2, positions_x3, positions_x4, positions_x5, positions_x6, positions_x7, positions_x8, positions_x9, positions_y0, positions_y1, positions_y2, positions_y3, positions_y4, positions_y5, positions_y6, positions_y7, positions_y8, positions_y9, avg, avg_l, avg_r, d, t, hr, hr_r, hr_l, temperature0, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7, temperature8, temperature9, temperature10, temperature11, rain0, rain1, rain2, rain3, rain4, rain5, rain6, rain7, rain8, rain9, rain10, rain11, wind, wind_direction, distances0, distances1, distances2, distances3, distances4, distances5, distances6, wall_heights0, wall_heights1, wall_heights2, wall_heights3, wall_heights4, wall_heights5, wall_heights6, name, picture, picture_night, nation_id, capacity, type, foul_ground, turf, gender, model_folder, file_name_3d_model, home_team_dugout_is_at_first_base):
        self.park_id = park_id
        self.dimensions_x = dimensions_x
        self.dimensions_y = dimensions_y
        self.batter_left_x = batter_left_x
        self.batter_left_y = batter_left_y
        self.batter_right_x = batter_right_x
        self.batter_right_y = batter_right_y
        self.bases_x0 = bases_x0
        self.bases_x1 = bases_x1
        self.bases_x2 = bases_x2
        self.bases_y0 = bases_y0
        self.bases_y1 = bases_y1
        self.bases_y2 = bases_y2
        self.positions_x0 = positions_x0
        self.positions_x1 = positions_x1
        self.positions_x2 = positions_x2
        self.positions_x3 = positions_x3
        self.positions_x4 = positions_x4
        self.positions_x5 = positions_x5
        self.positions_x6 = positions_x6
        self.positions_x7 = positions_x7
        self.positions_x8 = positions_x8
        self.positions_x9 = positions_x9
        self.positions_y0 = positions_y0
        self.positions_y1 = positions_y1
        self.positions_y2 = positions_y2
        self.positions_y3 = positions_y3
        self.positions_y4 = positions_y4
        self.positions_y5 = positions_y5
        self.positions_y6 = positions_y6
        self.positions_y7 = positions_y7
        self.positions_y8 = positions_y8
        self.positions_y9 = positions_y9
        self.avg = avg
        self.avg_l = avg_l
        self.avg_r = avg_r
        self.d = d
        self.t = t
        self.hr = hr
        self.hr_r = hr_r
        self.hr_l = hr_l
        self.temperature0 = temperature0
        self.temperature1 = temperature1
        self.temperature2 = temperature2
        self.temperature3 = temperature3
        self.temperature4 = temperature4
        self.temperature5 = temperature5
        self.temperature6 = temperature6
        self.temperature7 = temperature7
        self.temperature8 = temperature8
        self.temperature9 = temperature9
        self.temperature10 = temperature10
        self.temperature11 = temperature11
        self.rain0 = rain0
        self.rain1 = rain1
        self.rain2 = rain2
        self.rain3 = rain3
        self.rain4 = rain4
        self.rain5 = rain5
        self.rain6 = rain6
        self.rain7 = rain7
        self.rain8 = rain8
        self.rain9 = rain9
        self.rain10 = rain10
        self.rain11 = rain11
        self.wind = wind
        self.wind_direction = wind_direction
        self.distances0 = distances0
        self.distances1 = distances1
        self.distances2 = distances2
        self.distances3 = distances3
        self.distances4 = distances4
        self.distances5 = distances5
        self.distances6 = distances6
        self.wall_heights0 = wall_heights0
        self.wall_heights1 = wall_heights1
        self.wall_heights2 = wall_heights2
        self.wall_heights3 = wall_heights3
        self.wall_heights4 = wall_heights4
        self.wall_heights5 = wall_heights5
        self.wall_heights6 = wall_heights6
        self.name = name
        self.picture = picture
        self.picture_night = picture_night
        self.nation_id = nation_id
        self.capacity = capacity
        self.type = type
        self.foul_ground = foul_ground
        self.turf = turf
        self.gender = gender
        self.model_folder = model_folder
        self.file_name_3d_model = file_name_3d_model
        self.home_team_dugout_is_at_first_base = home_team_dugout_is_at_first_base
    
    def __str__(self):
        return "\n".join([
            f'park_id: {self.park_id}',
            f'dimensions_x: {self.dimensions_x}',
            f'dimensions_y: {self.dimensions_y}',
            f'batter_left_x: {self.batter_left_x}',
            f'batter_left_y: {self.batter_left_y}',
            f'batter_right_x: {self.batter_right_x}',
            f'batter_right_y: {self.batter_right_y}',
            f'bases_x0: {self.bases_x0}',
            f'bases_x1: {self.bases_x1}',
            f'bases_x2: {self.bases_x2}',
            f'bases_y0: {self.bases_y0}',
            f'bases_y1: {self.bases_y1}',
            f'bases_y2: {self.bases_y2}',
            f'positions_x0: {self.positions_x0}',
            f'positions_x1: {self.positions_x1}',
            f'positions_x2: {self.positions_x2}',
            f'positions_x3: {self.positions_x3}',
            f'positions_x4: {self.positions_x4}',
            f'positions_x5: {self.positions_x5}',
            f'positions_x6: {self.positions_x6}',
            f'positions_x7: {self.positions_x7}',
            f'positions_x8: {self.positions_x8}',
            f'positions_x9: {self.positions_x9}',
            f'positions_y0: {self.positions_y0}',
            f'positions_y1: {self.positions_y1}',
            f'positions_y2: {self.positions_y2}',
            f'positions_y3: {self.positions_y3}',
            f'positions_y4: {self.positions_y4}',
            f'positions_y5: {self.positions_y5}',
            f'positions_y6: {self.positions_y6}',
            f'positions_y7: {self.positions_y7}',
            f'positions_y8: {self.positions_y8}',
            f'positions_y9: {self.positions_y9}',
            f'avg: {self.avg}',
            f'avg_l: {self.avg_l}',
            f'avg_r: {self.avg_r}',
            f'd: {self.d}',
            f't: {self.t}',
            f'hr: {self.hr}',
            f'hr_r: {self.hr_r}',
            f'hr_l: {self.hr_l}',
            f'temperature0: {self.temperature0}',
            f'temperature1: {self.temperature1}',
            f'temperature2: {self.temperature2}',
            f'temperature3: {self.temperature3}',
            f'temperature4: {self.temperature4}',
            f'temperature5: {self.temperature5}',
            f'temperature6: {self.temperature6}',
            f'temperature7: {self.temperature7}',
            f'temperature8: {self.temperature8}',
            f'temperature9: {self.temperature9}',
            f'temperature10: {self.temperature10}',
            f'temperature11: {self.temperature11}',
            f'rain0: {self.rain0}',
            f'rain1: {self.rain1}',
            f'rain2: {self.rain2}',
            f'rain3: {self.rain3}',
            f'rain4: {self.rain4}',
            f'rain5: {self.rain5}',
            f'rain6: {self.rain6}',
            f'rain7: {self.rain7}',
            f'rain8: {self.rain8}',
            f'rain9: {self.rain9}',
            f'rain10: {self.rain10}',
            f'rain11: {self.rain11}',
            f'wind: {self.wind}',
            f'wind_direction: {self.wind_direction}',
            f'distances0: {self.distances0}',
            f'distances1: {self.distances1}',
            f'distances2: {self.distances2}',
            f'distances3: {self.distances3}',
            f'distances4: {self.distances4}',
            f'distances5: {self.distances5}',
            f'distances6: {self.distances6}',
            f'wall_heights0: {self.wall_heights0}',
            f'wall_heights1: {self.wall_heights1}',
            f'wall_heights2: {self.wall_heights2}',
            f'wall_heights3: {self.wall_heights3}',
            f'wall_heights4: {self.wall_heights4}',
            f'wall_heights5: {self.wall_heights5}',
            f'wall_heights6: {self.wall_heights6}',
            f'name: {self.name}',
            f'picture: {self.picture}',
            f'picture_night: {self.picture_night}',
            f'nation_id: {self.nation_id}',
            f'capacity: {self.capacity}',
            f'type: {self.type}',
            f'foul_ground: {self.foul_ground}',
            f'turf: {self.turf}',
            f'gender: {self.gender}',
            f'model_folder: {self.model_folder}',
            f'file_name_3d_model: {self.file_name_3d_model}',
            f'home_team_dugout_is_at_first_base: {self.home_team_dugout_is_at_first_base}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = {}

    for index, row in df.iterrows():
        obj = Park(*row)
        data[obj.park_id] = obj

    return data
