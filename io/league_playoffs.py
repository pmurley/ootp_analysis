import pandas


class LeaguePlayoffsEntry:
    def __init__(self, league_id, play_off_mode, round, max_round, num_wild_cards, best_of0, best_of1, best_of2, best_of3, best_of4, best_of5, best_of6, best_of7, best_of8, best_of9, best_of10, best_of11, best_of12, best_of13, best_of14, best_of15, best_of16, best_of17, best_of18, best_of19, best_of20, best_of21, best_of22, best_of23, best_of24, best_of25, best_of26, best_of27, best_of28, best_of29, best_of30, best_of31, best_of32, best_of33, best_of34, best_of35, best_of36, best_of37, best_of38, best_of39, best_of40, best_of41, best_of42, best_of43, best_of44, best_of45, best_of46, best_of47, best_of48, best_of49, round_names0, round_names1, round_names2, round_names3, round_names4, round_names5, round_names6, round_names7, round_names8, round_names9, round_names10, round_names11, round_names12, round_names13, round_names14, round_names15, round_names16, round_names17, round_names18, round_names19, round_names20, round_names21, round_names22, round_names23, round_names24, round_names25, round_names26, round_names27, round_names28, round_names29, round_names30, round_names31, round_names32, round_names33, round_names34, round_names35, round_names36, round_names37, round_names38, round_names39, round_names40, round_names41, round_names42, round_names43, round_names44, round_names45, round_names46, round_names47, round_names48, round_names49, split_season, allstar_winner_homefield, allstar_winner, winner):
        self.league_id = league_id
        self.play_off_mode = play_off_mode
        self.round = round
        self.max_round = max_round
        self.num_wild_cards = num_wild_cards
        self.best_of0 = best_of0
        self.best_of1 = best_of1
        self.best_of2 = best_of2
        self.best_of3 = best_of3
        self.best_of4 = best_of4
        self.best_of5 = best_of5
        self.best_of6 = best_of6
        self.best_of7 = best_of7
        self.best_of8 = best_of8
        self.best_of9 = best_of9
        self.best_of10 = best_of10
        self.best_of11 = best_of11
        self.best_of12 = best_of12
        self.best_of13 = best_of13
        self.best_of14 = best_of14
        self.best_of15 = best_of15
        self.best_of16 = best_of16
        self.best_of17 = best_of17
        self.best_of18 = best_of18
        self.best_of19 = best_of19
        self.best_of20 = best_of20
        self.best_of21 = best_of21
        self.best_of22 = best_of22
        self.best_of23 = best_of23
        self.best_of24 = best_of24
        self.best_of25 = best_of25
        self.best_of26 = best_of26
        self.best_of27 = best_of27
        self.best_of28 = best_of28
        self.best_of29 = best_of29
        self.best_of30 = best_of30
        self.best_of31 = best_of31
        self.best_of32 = best_of32
        self.best_of33 = best_of33
        self.best_of34 = best_of34
        self.best_of35 = best_of35
        self.best_of36 = best_of36
        self.best_of37 = best_of37
        self.best_of38 = best_of38
        self.best_of39 = best_of39
        self.best_of40 = best_of40
        self.best_of41 = best_of41
        self.best_of42 = best_of42
        self.best_of43 = best_of43
        self.best_of44 = best_of44
        self.best_of45 = best_of45
        self.best_of46 = best_of46
        self.best_of47 = best_of47
        self.best_of48 = best_of48
        self.best_of49 = best_of49
        self.round_names0 = round_names0
        self.round_names1 = round_names1
        self.round_names2 = round_names2
        self.round_names3 = round_names3
        self.round_names4 = round_names4
        self.round_names5 = round_names5
        self.round_names6 = round_names6
        self.round_names7 = round_names7
        self.round_names8 = round_names8
        self.round_names9 = round_names9
        self.round_names10 = round_names10
        self.round_names11 = round_names11
        self.round_names12 = round_names12
        self.round_names13 = round_names13
        self.round_names14 = round_names14
        self.round_names15 = round_names15
        self.round_names16 = round_names16
        self.round_names17 = round_names17
        self.round_names18 = round_names18
        self.round_names19 = round_names19
        self.round_names20 = round_names20
        self.round_names21 = round_names21
        self.round_names22 = round_names22
        self.round_names23 = round_names23
        self.round_names24 = round_names24
        self.round_names25 = round_names25
        self.round_names26 = round_names26
        self.round_names27 = round_names27
        self.round_names28 = round_names28
        self.round_names29 = round_names29
        self.round_names30 = round_names30
        self.round_names31 = round_names31
        self.round_names32 = round_names32
        self.round_names33 = round_names33
        self.round_names34 = round_names34
        self.round_names35 = round_names35
        self.round_names36 = round_names36
        self.round_names37 = round_names37
        self.round_names38 = round_names38
        self.round_names39 = round_names39
        self.round_names40 = round_names40
        self.round_names41 = round_names41
        self.round_names42 = round_names42
        self.round_names43 = round_names43
        self.round_names44 = round_names44
        self.round_names45 = round_names45
        self.round_names46 = round_names46
        self.round_names47 = round_names47
        self.round_names48 = round_names48
        self.round_names49 = round_names49
        self.split_season = split_season
        self.allstar_winner_homefield = allstar_winner_homefield
        self.allstar_winner = allstar_winner
        self.winner = winner
    
    def __str__(self):
        return "\n".join([
            f'league_id: {self.league_id}',
            f'play_off_mode: {self.play_off_mode}',
            f'round: {self.round}',
            f'max_round: {self.max_round}',
            f'num_wild_cards: {self.num_wild_cards}',
            f'best_of0: {self.best_of0}',
            f'best_of1: {self.best_of1}',
            f'best_of2: {self.best_of2}',
            f'best_of3: {self.best_of3}',
            f'best_of4: {self.best_of4}',
            f'best_of5: {self.best_of5}',
            f'best_of6: {self.best_of6}',
            f'best_of7: {self.best_of7}',
            f'best_of8: {self.best_of8}',
            f'best_of9: {self.best_of9}',
            f'best_of10: {self.best_of10}',
            f'best_of11: {self.best_of11}',
            f'best_of12: {self.best_of12}',
            f'best_of13: {self.best_of13}',
            f'best_of14: {self.best_of14}',
            f'best_of15: {self.best_of15}',
            f'best_of16: {self.best_of16}',
            f'best_of17: {self.best_of17}',
            f'best_of18: {self.best_of18}',
            f'best_of19: {self.best_of19}',
            f'best_of20: {self.best_of20}',
            f'best_of21: {self.best_of21}',
            f'best_of22: {self.best_of22}',
            f'best_of23: {self.best_of23}',
            f'best_of24: {self.best_of24}',
            f'best_of25: {self.best_of25}',
            f'best_of26: {self.best_of26}',
            f'best_of27: {self.best_of27}',
            f'best_of28: {self.best_of28}',
            f'best_of29: {self.best_of29}',
            f'best_of30: {self.best_of30}',
            f'best_of31: {self.best_of31}',
            f'best_of32: {self.best_of32}',
            f'best_of33: {self.best_of33}',
            f'best_of34: {self.best_of34}',
            f'best_of35: {self.best_of35}',
            f'best_of36: {self.best_of36}',
            f'best_of37: {self.best_of37}',
            f'best_of38: {self.best_of38}',
            f'best_of39: {self.best_of39}',
            f'best_of40: {self.best_of40}',
            f'best_of41: {self.best_of41}',
            f'best_of42: {self.best_of42}',
            f'best_of43: {self.best_of43}',
            f'best_of44: {self.best_of44}',
            f'best_of45: {self.best_of45}',
            f'best_of46: {self.best_of46}',
            f'best_of47: {self.best_of47}',
            f'best_of48: {self.best_of48}',
            f'best_of49: {self.best_of49}',
            f'round_names0: {self.round_names0}',
            f'round_names1: {self.round_names1}',
            f'round_names2: {self.round_names2}',
            f'round_names3: {self.round_names3}',
            f'round_names4: {self.round_names4}',
            f'round_names5: {self.round_names5}',
            f'round_names6: {self.round_names6}',
            f'round_names7: {self.round_names7}',
            f'round_names8: {self.round_names8}',
            f'round_names9: {self.round_names9}',
            f'round_names10: {self.round_names10}',
            f'round_names11: {self.round_names11}',
            f'round_names12: {self.round_names12}',
            f'round_names13: {self.round_names13}',
            f'round_names14: {self.round_names14}',
            f'round_names15: {self.round_names15}',
            f'round_names16: {self.round_names16}',
            f'round_names17: {self.round_names17}',
            f'round_names18: {self.round_names18}',
            f'round_names19: {self.round_names19}',
            f'round_names20: {self.round_names20}',
            f'round_names21: {self.round_names21}',
            f'round_names22: {self.round_names22}',
            f'round_names23: {self.round_names23}',
            f'round_names24: {self.round_names24}',
            f'round_names25: {self.round_names25}',
            f'round_names26: {self.round_names26}',
            f'round_names27: {self.round_names27}',
            f'round_names28: {self.round_names28}',
            f'round_names29: {self.round_names29}',
            f'round_names30: {self.round_names30}',
            f'round_names31: {self.round_names31}',
            f'round_names32: {self.round_names32}',
            f'round_names33: {self.round_names33}',
            f'round_names34: {self.round_names34}',
            f'round_names35: {self.round_names35}',
            f'round_names36: {self.round_names36}',
            f'round_names37: {self.round_names37}',
            f'round_names38: {self.round_names38}',
            f'round_names39: {self.round_names39}',
            f'round_names40: {self.round_names40}',
            f'round_names41: {self.round_names41}',
            f'round_names42: {self.round_names42}',
            f'round_names43: {self.round_names43}',
            f'round_names44: {self.round_names44}',
            f'round_names45: {self.round_names45}',
            f'round_names46: {self.round_names46}',
            f'round_names47: {self.round_names47}',
            f'round_names48: {self.round_names48}',
            f'round_names49: {self.round_names49}',
            f'split_season: {self.split_season}',
            f'allstar_winner_homefield: {self.allstar_winner_homefield}',
            f'allstar_winner: {self.allstar_winner}',
            f'winner: {self.winner}',
        ])


def parse(path):
    df = pandas.read_csv(path)
    data = []

    for index, row in df.iterrows():
        obj = LeaguePlayoffsEntry(*row)
        data.append(obj)

    return data
