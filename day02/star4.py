import star3

def find_minimum_cube_set(game):
    minimum_cube_set = {"blue": 0, "green": 0, "red": 0}
    for set in game:
        for colour in minimum_cube_set.keys():
            minimum_cube_set[colour] = max(minimum_cube_set[colour], set[colour])
    return minimum_cube_set


def power(cube_set):
    power = 1
    for colour in cube_set.keys():
        power = power * cube_set[colour]
    return power


def power_sum(parsed_games):
    power_sum = 0
    for game in parsed_games:
        minimum_cube_set = find_minimum_cube_set(game)
        power_sum += power(minimum_cube_set)
    return power_sum


if __name__ == "__main__":
    with open("day02/input.txt") as file:
        input = file.read()
    parsed_games = star3.parse_games(input)
    total_power = power_sum(parsed_games)
    print(total_power)
