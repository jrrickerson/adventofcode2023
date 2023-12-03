import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    max_red = 12
    max_green = 13
    max_blue = 14
    games = [utils.parse_game(line) for line in input_data]
    possible_games = [g for g in games if utils.validate_game(
        g,
        max_red=max_red,
        max_green=max_green,
        max_blue=max_blue)
    ]
    result = sum([int(g.id) for g in possible_games])

    return result


def part_2(input_data):
    pass


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
    print(
        "Solving Puzzle for Day 2:", "https://adventofcode.com/2022/day/2"
    )
    print(main("../puzzles/day-02.input"))
