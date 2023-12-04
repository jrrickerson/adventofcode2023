import utils


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    nodes = utils.parse_schematic(input_data)
    part_cells = utils.find_adjacent_digits(nodes)

    part_numbers = utils.collect_numbers(nodes, part_cells)

    return sum(part_numbers)


def part_2(input_data):
    nodes = utils.parse_schematic(input_data)
    gear_ratios = utils.find_gear_ratios(nodes)

    return sum(gear_ratios)


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
        "Solving Puzzle for Day 3:", "https://adventofcode.com/2022/day/3"
    )
    print(main("../puzzles/day-03.input"))
