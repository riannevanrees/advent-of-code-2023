import math
import numpy as np

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
NUMBERS_AS_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
STRING_TO_NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def get_first_number(line):
    # Iterate over all possible numbers and return the number with the lowest index
    best_index = math.inf
    best_number = None
    for number in NUMBERS:
        result = line.find(str(number))
        if result != -1 and result < best_index:
            best_index = result
            best_number = number
    for number in NUMBERS_AS_STRINGS:
        result = line.find(number)
        if result != -1 and result < best_index:
            best_index = result
            best_number = STRING_TO_NUMBERS[number]
    return best_number


def get_last_number(line):
    best_index = -math.inf
    best_number = None
    for number in NUMBERS:
        result = line.rfind(str(number))
        if result != -1 and result > best_index:
            best_index = result
            best_number = number
    for number in NUMBERS_AS_STRINGS:
        result = line.rfind(number)
        if result != -1 and result > best_index:
            best_index = result
            best_number = STRING_TO_NUMBERS[number]
    return best_number


def get_solution_line(line):
    first_number = get_first_number(line)
    last_number = get_last_number(line)
    return first_number * 10 + last_number


def get_solution_total(text):
    lines = text.splitlines()
    calibration_values = np.ones(len(lines))
    for line_number, line in enumerate(lines):
        calibration_values[line_number] = get_solution_line(line)
    return int(np.sum(calibration_values))


if __name__ == "__main__":
    with open("day01/input.txt") as file:
        text = file.read()
    solution = get_solution_total(text)
    print(solution)
