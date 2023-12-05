import star3


TESTINPUT = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

PARSED_GAMES = [[{"blue": 3, "green": 0, "red": 4},
                 {"blue": 6, "green": 2, "red": 1},
                 {"blue": 0, "green": 2, "red": 0}],
                [{"blue": 1, "green": 2, "red": 0},
                 {"blue": 4, "green": 3, "red": 1},
                 {"blue": 1, "green": 1, "red": 0}],
                [{"blue": 6, "green": 8, "red": 20},
                 {"blue": 5, "green": 13, "red": 4},
                 {"blue": 0, "green": 5, "red": 1}],
                [{"blue": 6, "green": 1, "red": 3},
                 {"blue": 0, "green": 3, "red": 6},
                 {"blue": 15, "green": 3, "red": 14}],
                [{"blue": 1, "green": 3, "red": 6},
                 {"blue": 2, "green": 2, "red": 1}]
                ]

TEST_BAG_CONTENTS = {"blue": 14, "green": 13, "red": 12}

def test_parse_games():
    assert star3.parse_games(TESTINPUT) == PARSED_GAMES


def test_game_possible():
    assert star3.game_possible(PARSED_GAMES[0], TEST_BAG_CONTENTS) == True
    assert star3.game_possible(PARSED_GAMES[2], TEST_BAG_CONTENTS) == False


def test_sum_ids():
    assert star3.sum_ids_of_possible_games(PARSED_GAMES, TEST_BAG_CONTENTS) == 8
