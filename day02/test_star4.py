import star4

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

MINIMUM_CUBE_SETS = [{"blue": 6, "green": 2, "red": 4},
                     {"blue": 4, "green": 3, "red": 1},
                     {"blue": 6, "green": 13, "red": 20},
                     {"blue": 15, "green": 3, "red": 14},
                     {"blue": 2, "green": 3, "red": 6}]

POWERS = [48, 12, 1560, 630, 36]

POWER_TOTAL = 2286


def test_find_minimum_cube_set():
    for i in range(5):
        assert star4.find_minimum_cube_set(PARSED_GAMES[i]) == MINIMUM_CUBE_SETS[i]


def test_power():
    for i in range(5):
        assert star4.power(MINIMUM_CUBE_SETS[i]) == POWERS[i]


def test_power_sum():
    assert star4.power_sum(PARSED_GAMES) == POWER_TOTAL
