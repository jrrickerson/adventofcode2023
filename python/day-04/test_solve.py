import solve
import utils


def test_parse_card_get_id():
    line = "Card 123: 1 2 3 | 4 5 6"
    card = utils.parse_card(line)

    assert type(card) is utils.Card
    assert card.id == "123"


def test_parse_card_no_numbers():
    line = "Card 123: "
    card = utils.parse_card(line)

    assert type(card) is utils.Card
    assert card.id == "123"
    assert card.winning_nums == set()
    assert card.play_nums == set()


def test_parse_card_empty_numbers():
    line = "Card 123: |"
    card = utils.parse_card(line)

    assert type(card) is utils.Card
    assert card.id == "123"
    assert card.winning_nums == set()
    assert card.play_nums == set()


def test_parse_card_no_play_numbers():
    line = "Card 123: 7 15 23|"
    card = utils.parse_card(line)

    assert type(card) is utils.Card
    assert card.id == "123"
    assert card.winning_nums == {7, 15, 23}
    assert card.play_nums == set()


def test_parse_card_number_lists():
    line = "Card 123: 1 2 3 | 4 5 6"
    card = utils.parse_card(line)

    assert type(card) is utils.Card
    assert card.id == "123"
    assert card.winning_nums == {1, 2, 3}
    assert card.play_nums == {4, 5, 6}


def test_score_matches_no_matches():
    card = utils.Card(
        id="123",
        winning_nums={1, 2, 3},
        play_nums={4, 5, 6},
    )
    score = utils.score_matches(card)

    assert score == 0


def test_score_matches_single_match():
    card = utils.Card(
        id="123",
        winning_nums={1, 2, 3, 8},
        play_nums={8, 4, 5, 6},
    )
    score = utils.score_matches(card)

    assert score == 1


def test_score_matches_multi_matches():
    card = utils.Card(
        id="123",
        winning_nums={1, 2, 3, 8, 9, 10, 11},
        play_nums={4, 5, 6, 8, 9, 10, 11},
    )
    score = utils.score_matches(card)

    assert score ==  2 ** (4 - 1)


def test_part_1_input_data():
    input_data = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    result = solve.part_1(input_data)

    assert result == 13
