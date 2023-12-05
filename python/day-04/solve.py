import utils

from collections import defaultdict


def get_input_data(filename):  # pragma: no cover
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    cards = [utils.parse_card(line) for line in input_data]
    scores = [utils.score_matches(card) for card in cards]

    return sum(scores)


def part_2(input_data):
    cards = [utils.parse_card(line) for line in input_data]
    card_counts = {card.id: 1 for card in cards}
    for card in cards:
        card_counts = utils.process_matches(card_counts, card)

    return sum(card_counts.values())


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
        "Solving Puzzle for Day 4:", "https://adventofcode.com/2022/day/4"
    )
    print(main("../puzzles/day-04.input"))
