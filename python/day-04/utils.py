from collections import namedtuple

Card = namedtuple("Card", "id winning_nums play_nums", defaults=(set(), set()))


def parse_card(card_str):
    id_str, num_lists = card_str.split(":")
    card_id = int(id_str.replace("Card ", "").strip())

    if "|" in num_lists:
        winning, plays = num_lists.split("|")
        winning_nums = set([int(n) for n in winning.split()])
        play_nums = set([int(n) for n in plays.split()])
    else:
        winning_nums = set()
        play_nums = set()

    return Card(
        id=card_id,
        winning_nums=winning_nums,
        play_nums=play_nums
    )


def score_matches(card):
    matches = card.winning_nums & card.play_nums
    if not matches:
        return 0
    match_count = max((len(matches) - 1, 0))

    return 2 ** match_count


def update_card_counts(card_counts, card):
    matches = card.winning_nums & card.play_nums
    next_card = card.id + 1
    for card_id in range(next_card, next_card + len(matches)):
        card_counts[card_id] += 1
    return card_counts


def process_matches(card_counts, card):
    copies = card_counts.get(card.id, 1)
    match_count = len(card.winning_nums & card.play_nums)
    next_card = card.id + 1
    for card_id in range(next_card, next_card + match_count):
        card_counts[card_id] += copies
    return card_counts
