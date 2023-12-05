import re


def parse_games(input):
    unparsed_games = input.splitlines()
    parsed_games = []
    for game in unparsed_games:
        parsed_games.append([])
        # Remove game x preamble
        sets = (game.split(": ")[1]).split("; ")
        for set in sets:
            parsed_games[-1].append(dict(blue=0, green=0, red=0))
            cubes_in_set = re.findall(r'(\d+) (\w+)', set)
            for cube_colour_in_set in cubes_in_set:
                amount, colour = cube_colour_in_set
                parsed_games[-1][-1][colour] = int(amount)
    return parsed_games


def game_possible(game_results, bag_contents):
    for set in game_results:
        for colour in set.keys():
            if set[colour] > bag_contents[colour]:
                return False
    return True


def sum_ids_of_possible_games(parsed_games, bag_contents):
    id_sum = 0
    for index, game in enumerate(parsed_games):
        if game_possible(game, bag_contents):
            id = index + 1
            id_sum += id
    return id_sum


if __name__ == "__main__":
    with open("day02/input.txt") as file:
        input = file.read()
    parsed_games = parse_games(input)
    bag_contents = {"red": 12, "green": 13, "blue": 14}
    id_sum = sum_ids_of_possible_games(parsed_games, bag_contents)
    print(id_sum)
