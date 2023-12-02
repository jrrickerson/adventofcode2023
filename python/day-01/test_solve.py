import solve
import utils


def test_get_digits_no_digits():
    line = "abcdefg"
    digits = utils.get_digits(line)

    assert not digits


def test_get_digits_single_digit():
    line = "abc1def"
    digits = utils.get_digits(line)

    assert digits[0] == "1"


def test_get_digits_multi_digit():
    line = "ab1cd2ef3g"
    digits = utils.get_digits(line)

    assert digits == ["1", "2", "3"]


def test_get_calibration_value_endpoints():
    digits = ["1", "2", "3"]
    value = utils.get_calibration_value(digits)

    assert value == 13


def test_get_calibration_value_single_digit():
    digits = ["1"]
    value = utils.get_calibration_value(digits)

    assert value == 11


def test_part_1_sample_input():
    input_data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    calibration = solve.part_1(input_data)

    assert calibration == 142


def test_get_digits_words_no_numbers():
    line = "abcdefg"
    digits = utils.get_digits_words(line)

    assert digits == []


def test_get_digits_words_no_words():
    line = "abc1def2g"
    digits = utils.get_digits_words(line)

    assert digits == ["1", "2"]


def test_convert_word_digits_one_word():
    line = "abc1dzeroef2g"
    digits = utils.get_digits_words(line)

    assert digits == ["1", "0", "2"]


def test_convert_word_digits_multi_word():
    line = "absevenc1dzeroetwof2g"
    digits = utils.get_digits_words(line)

    assert digits == ["7", "1", "0", "2", "2"]


def test_convert_word_digits_overlap():
    line = "eighthree12seven"
    digits = utils.get_digits_words(line)

    assert digits == ["8", "3", "1", "2", "7"]


def test_part_2_sample_input():
    input_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    calibration = solve.part_2(input_data)

    assert calibration == 281
