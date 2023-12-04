from day01 import star1

TESTDATA = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

def test_get_calibration_value1():
    assert star1.get_calibration_value("1abc2") == 12


def test_get_calibration_value2():
    assert star1.get_calibration_value("a1b2c3d4e5f") == 15


def test_get_calibration_value3():
    assert star1.get_calibration_value("treb7uchet") == 77


def test_get_sum_of_calibration_values():
    assert star1.get_sum_of_calibration_values(TESTDATA) == 142
