import numpy as np

# The heart of the federation...

def get_calibration_value(line):
    numbers = [int(character) for character in line
               if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    return numbers[0] * 10 + numbers[-1]

def get_sum_of_calibration_values(text):
    lines = text.splitlines()
    calibration_values = np.ones(len(lines))
    for line_number, line in enumerate(lines):
        calibration_values[line_number] = get_calibration_value(line)
    return np.sum(calibration_values)


if __name__ == "__main__":
    with open("day01/input.txt") as file:
        text = file.read()
    solution = get_sum_of_calibration_values(text)
    print(int(solution))
