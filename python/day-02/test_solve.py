import solve
import utils


def test_parse_draw_empty():
    draw_str = ""
    draw = utils.parse_draw(draw_str)

    assert type(draw) == utils.Draw
    assert draw.red == 0
    assert draw.green == 0
    assert draw.blue == 0


def test_parse_draw_single_color():
    draw_str = "1 red"
    draw = utils.parse_draw(draw_str)

    assert type(draw) == utils.Draw
    assert draw.red == 1
    assert draw.green == 0
    assert draw.blue == 0


def test_parse_draw_all_color():
    draw_str = "3 red, 2 green, 1 blue"
    draw = utils.parse_draw(draw_str)

    assert type(draw) == utils.Draw
    assert draw.red == 3
    assert draw.green == 2
    assert draw.blue == 1


def test_parse_game_populates_id():
    game_str = "Game 123: "
    game = utils.parse_game(game_str)

    assert type(game) == utils.Game
    assert game.id == "123"


def test_parse_game_single_draw():
    game_str = "Game 1: 1 red, 2 blue"
    game = utils.parse_game(game_str)

    assert type(game) == utils.Game
    assert game.id == "1"
    assert len(game.draws) == 1
    assert game.draws[0].red == 1
    assert game.draws[0].blue == 2


def test_parse_game_multi_draw():
    game_str = "Game 1: 1 red, 2 blue; 2 green, 1 blue; 3 red"
    game = utils.parse_game(game_str)

    assert type(game) == utils.Game
    assert game.id == "1"
    assert len(game.draws) == 3

    assert game.draws[0].red == 1
    assert game.draws[0].blue == 2

    assert game.draws[1].green == 2
    assert game.draws[1].blue == 1

    assert game.draws[2].red == 3


def test_validate_game_no_max():
    game = utils.Game(
        id="123",
        draws=[
            utils.Draw(red=1, green=2, blue=3),
            utils.Draw(red=5, green=1, blue=1),
            utils.Draw(red=15, green=10, blue=5),
            utils.Draw(green=12, blue=2),
            utils.Draw(red=4, blue=1),
        ]
    )

    valid = utils.validate_game(game)

    assert valid is True


def test_validate_game_max_single_color():
    game = utils.Game(
        id="123",
        draws=[
            utils.Draw(red=1, green=2, blue=3),
            utils.Draw(red=5, green=1, blue=1),
            utils.Draw(red=15, green=10, blue=5),
            utils.Draw(green=12, blue=2),
            utils.Draw(red=4, blue=1),
        ]
    )

    valid = utils.validate_game(game, max_red=10)

    assert valid is False


def test_validate_game_all_colors_valid():
    game = utils.Game(
        id="123",
        draws=[
            utils.Draw(red=1, green=2, blue=3),
            utils.Draw(red=5, green=1, blue=1),
            utils.Draw(red=15, green=10, blue=5),
            utils.Draw(green=12, blue=2),
            utils.Draw(red=4, blue=1),
        ]
    )

    valid = utils.validate_game(
        game, max_red=20, max_green=15, max_blue=5)

    assert valid is True


def test_validate_game_all_colors_invalid():
    game = utils.Game(
        id="123",
        draws=[
            utils.Draw(red=1, green=2, blue=3),
            utils.Draw(red=5, green=1, blue=1),
            utils.Draw(red=15, green=10, blue=5),
            utils.Draw(green=12, blue=2),
            utils.Draw(red=4, blue=1),
        ]
    )

    valid = utils.validate_game(
        game, max_red=14, max_green=10, max_blue=3)

    assert valid is False


def test_part_1_input_data():
    input_data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    result = solve.part_1(input_data)
    assert result == 8
