import solve
import utils


def test_parse_schematic_empty_cells():
    lines = [
        ".....",
        ".....",
        ".....",
    ]
    nodes = utils.parse_schematic(lines)

    assert nodes == {}


def test_parse_schematic_store_symbols():
    lines = [
        "..@..",
        "....#",
        ".....",
    ]
    nodes = utils.parse_schematic(lines)

    assert len(nodes) == 2
    assert nodes[(2, 0)] == "@"
    assert nodes[(4, 1)] == "#"


def test_parse_schematic_store_numbers():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    assert len(nodes) == 5
    assert nodes[(2, 0)] == "1"
    assert nodes[(3, 0)] == "2"
    assert nodes[(4, 0)] == "3"
    assert nodes[(1, 2)] == "4"
    assert nodes[(2, 2)] == "5"


def test_parse_schematic_store_mixed():
    lines = [
        "..123",
        ".#...",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    assert len(nodes) == 6
    assert nodes[(2, 0)] == "1"
    assert nodes[(3, 0)] == "2"
    assert nodes[(4, 0)] == "3"
    assert nodes[(1, 1)] == "#"
    assert nodes[(1, 2)] == "4"
    assert nodes[(2, 2)] == "5"


def test_surrounding_cells():
    center_cell = (1, 2)

    cells = utils.surrounding_cells(*center_cell)

    assert len(cells) == 8
    assert (0, 1) in cells
    assert (1, 1) in cells
    assert (2, 1) in cells
    assert (0, 2) in cells
    assert (2, 2) in cells
    assert (0, 3) in cells
    assert (1, 3) in cells
    assert (2, 3) in cells


def test_find_adjacent_digits_no_digits():
    lines = [
        "..@..",
        "....#",
        ".....",
    ]
    nodes = utils.parse_schematic(lines)
    adj_digits = utils.find_adjacent_digits(nodes)

    assert len(adj_digits) == 0


def test_find_adjacent_digits_no_symbols():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)
    adj_digits = utils.find_adjacent_digits(nodes)

    assert len(adj_digits) == 0


def test_find_adjacent_digits_none_adjacent():
    lines = [
        "@.123",
        ".....",
        ".45.#",
    ]
    nodes = utils.parse_schematic(lines)
    adj_digits = utils.find_adjacent_digits(nodes)

    assert len(adj_digits) == 0


def test_find_adjacent_digits_one_adjacent():
    lines = [
        ".@123",
        ".....",
        ".45.#",
    ]
    nodes = utils.parse_schematic(lines)
    adj_digits = utils.find_adjacent_digits(nodes)

    assert len(adj_digits) == 1
    assert (2, 0) in adj_digits


def test_find_adjacent_digits_multi_adjacent():
    lines = [
        ".@123",
        ".../.",
        ".45.#",
    ]
    nodes = utils.parse_schematic(lines)
    adj_digits = utils.find_adjacent_digits(nodes)

    assert len(adj_digits) == 4
    assert (2, 0) in adj_digits
    assert (3, 0) in adj_digits
    assert (4, 0) in adj_digits
    assert (2, 2) in adj_digits


def test_collect_numbers_empty_set():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 0


def test_collect_numbers_start_cell():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {(2, 0)}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 1
    assert 123 in numbers


def test_collect_numbers_end_cell():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {(4, 0)}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 1
    assert 123 in numbers


def test_collect_numbers_no_duplication():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {(2, 0), (4, 0)}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 1
    assert 123 in numbers


def test_collect_numbers_symbol_prefix():
    lines = [
        "..123",
        ".....",
        "#45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {(2, 0), (2, 2)}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 2
    assert 123 in numbers
    assert 45 in numbers


def test_collect_numbers_multi_numbers():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)

    cells = {(2, 0), (2, 2)}
    numbers = utils.collect_numbers(nodes, cells)

    assert len(numbers) == 2
    assert 123 in numbers
    assert 45 in numbers


def test_part_1_input_data():
    input_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    result = solve.part_1(input_data)

    assert result == 4361


def test_find_gear_ratios_no_symbols():
    lines = [
        "..123",
        ".....",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)
    gear_ratios = utils.find_gear_ratios(nodes)

    assert gear_ratios == []


def test_find_gear_ratios_no_gears():
    lines = [
        "..123",
        "....*",
        ".45..",
    ]
    nodes = utils.parse_schematic(lines)
    gear_ratios = utils.find_gear_ratios(nodes)

    assert gear_ratios == []


def test_find_gear_ratios_one_gear():
    lines = [
        "....4",
        "....*",
        ".45.5",
    ]
    nodes = utils.parse_schematic(lines)
    gear_ratios = utils.find_gear_ratios(nodes)

    assert len(gear_ratios) == 1
    assert 20 in gear_ratios


def test_find_gear_ratios_multi_gears():
    lines = [
        "8*..4",
        "10..*",
        ".45.5",
    ]
    nodes = utils.parse_schematic(lines)
    gear_ratios = utils.find_gear_ratios(nodes)

    assert len(gear_ratios) == 2
    assert 20 in gear_ratios
    assert 80 in gear_ratios


def test_part_2_input_data():
    input_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    result = solve.part_2(input_data)

    assert result == 467835
