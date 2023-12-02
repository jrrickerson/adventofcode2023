import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    calibration_values = [
        utils.get_calibration_value(utils.get_digits(line)) for line in input_data
    ]
    return sum(calibration_values)


def part_2(input_data):
    calibration_values = [
        utils.get_calibration_value(
            utils.get_digits_words(line)) for line in input_data
    ]
    return sum(calibration_values)


def main(input_file):  # pragma: no cover
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":  # pragma: no cover
    print("Solving Puzzle for Day 1:", "https://adventofcode.com/2022/day/1")
    print(main("../puzzles/day-01.input"))
