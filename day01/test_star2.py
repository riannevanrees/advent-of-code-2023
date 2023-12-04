from day01 import star2

TESTDATA = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

test_lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2",
              "zoneight234", "7pqrstsixteen"]

solution_lines = [29, 83, 13, 24, 42, 14, 76]

solution_total = 281


def test_first_number():
    assert star2.get_first_number(test_lines[0]) == 2
    assert star2.get_first_number(test_lines[1]) == 8
    assert star2.get_first_number(test_lines[2]) == 1
    assert star2.get_first_number(test_lines[3]) == 2
    assert star2.get_first_number(test_lines[4]) == 4
    assert star2.get_first_number(test_lines[5]) == 1
    assert star2.get_first_number(test_lines[6]) == 7


def test_last_number():
    assert star2.get_last_number(test_lines[0]) == 9
    assert star2.get_last_number(test_lines[1]) == 3
    assert star2.get_last_number(test_lines[2]) == 3
    assert star2.get_last_number(test_lines[3]) == 4
    assert star2.get_last_number(test_lines[4]) == 2
    assert star2.get_last_number(test_lines[5]) == 4
    assert star2.get_last_number(test_lines[6]) == 6


def test_get_solution_line():
    for line_count, line in enumerate(test_lines):
        assert star2.get_solution_line(line)  == solution_lines[line_count]


def test_get_solution_line1():
    assert star2.get_solution_line("sevenine") == 79


def test_get_solution_line2():
    assert star2.get_solution_line("five") == 55


def test_get_solution_line3():
    assert star2.get_solution_line("twone") == 21


def test_get_solution_total():
    assert star2.get_solution_total(TESTDATA) == 281

