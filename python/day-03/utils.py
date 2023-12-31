import string


def parse_schematic(lines):
    nodes = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cell = lines[y][x]
            if cell == ".":
                continue
            nodes[(x, y)] = cell
    return nodes


def surrounding_cells(x, y):
    return [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x-1, y),
        (x+1, y),
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1)
    ]


def _adjacent_to_cell(nodes, x, y):
    digit_cells = set()
    # Check surrounding cells
    for coords in surrounding_cells(x, y):
        # Did we find a digit?
        cell_value = nodes.get(coords)
        if cell_value and cell_value in string.digits:
            digit_cells.add(coords)
    return digit_cells


def find_adjacent_digits(nodes):
    digit_cells = set()
    for key, value in nodes.items():
        # If it's a symbol
        if value not in string.digits:
            digits_adjacent = _adjacent_to_cell(nodes, *key)
            digit_cells.update(digits_adjacent)
    return digit_cells
            

def collect_numbers(nodes, coords):
    if not coords:
        return []

    numbers = []
    got_digits = set()
    for coord in coords:
        if coord in got_digits:
            continue
        x, y = coord
        # Find the start digit
        while True:
            value = nodes.get((x - 1, y))
            if not value:
                break
            if value not in string.digits:
                break
            x -= 1
        digits = []
        while True:
            value = nodes.get((x, y))
            if not value:
                break
            if value not in string.digits:
                break
            # Ensure we remove any overlaps
            got_digits.add((x, y))
            digits.append(value)
            x += 1
        numbers.append(int(''.join(digits)))
    return numbers


def find_gear_ratios(nodes):
    ratios = []
    for key, value in nodes.items():
        if value != "*":
            continue
        digit_neighbors = _adjacent_to_cell(nodes, *key)
        part_numbers = collect_numbers(nodes, digit_neighbors)
        if len(part_numbers) == 2:
            ratios.append(part_numbers[0] * part_numbers[1])
    return ratios
