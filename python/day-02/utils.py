from collections import namedtuple


Draw = namedtuple("Draw", "red green blue", defaults=[0, 0, 0])

Game = namedtuple("Game", "id draws", defaults=[[]])


def parse_draw(draw_str):
    color_entries = draw_str.split(",")
    red, green, blue = 0, 0, 0
    for entry in color_entries:
        if not entry.strip():
            continue
        count, color = entry.strip().split()
        if "red" == color:
            red = int(count)
        elif "green" == color:
            green = int(count)
        elif "blue" == color:
            blue = int(count)
    return Draw(red=red, green=green, blue=blue)


def parse_game(game_str):
    id_str, all_draws_str = game_str.split(":")
    game_id = id_str.replace("Game ", "").strip()

    draws = []
    for draw_str in all_draws_str.strip().split(";"):
        draws.append(parse_draw(draw_str))

    return Game(id=game_id, draws=draws)


def validate_game(game, max_red=0, max_green=0, max_blue=0):
    valid = False
    for draw in game.draws:
        if max_red and draw.red > max_red:
            break
        if max_green and draw.green > max_green:
            break
        if max_blue and draw.blue > max_blue:
            break
    else:
        valid = True
    return valid
