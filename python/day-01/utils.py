import re
import string


WORD_DIGITS = {
    "zero":  "0",
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

words = "|".join(WORD_DIGITS.keys())
numerals = string.digits

word_digit_re = re.compile(f"{words}|[{numerals}]" + "{1}")


def get_digits(line):
    digits = [c for c in line if c in string.digits]
    print(f"Got digits {digits}")
    return digits


def get_calibration_value(digit_list):
    return int(f"{digit_list[0]}{digit_list[-1]}")


def get_digits_words(line):
    digits = []
    index = 0
    match_obj = word_digit_re.search(line)
    while match_obj:
        digits.append(WORD_DIGITS.get(match_obj.group(0), match_obj.group(0)))
        index = match_obj.start(0) + 1
        match_obj = word_digit_re.search(line, pos=index)

    print(f"Got {digits} from {line}")
    return digits
