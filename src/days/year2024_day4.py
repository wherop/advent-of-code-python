# Advent of Code 2024, day 4
from utils.input import read_input
from aocd import data


def parse_input(raw_input: str):
    matrix = [list(line) for line in raw_input.splitlines()]
    return matrix


def add_coords(coords1: tuple[int, int], coords2: tuple[int, int]):
    return (coords1[0] + coords2[0], coords1[1] + coords2[1])


def within_range(coords, matrix):
    x, y = coords
    if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
        return True

    return False


def find_letter(letter, matrix: list[list[str]]):
    print(f"First letter is: {letter}")
    return [
        (row, col)
        for row, line in enumerate(matrix)
        for col, char in enumerate(line)
        if char == letter
    ]


def find_direction(
    postition: tuple[int, int], char: str, matrix: list[list[str]]
) -> list[tuple[int, int]]:
    directions = [(-1, -1), (-1, 0), (1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    y, x = postition

    valid_directions = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if within_range((new_x, new_y), matrix) and matrix[new_y][new_x] == char:
            valid_directions.append((dx, dy))
    return valid_directions


def check_letters_recurs(
    word: str,
    position: tuple[int, int],
    direction: tuple[int, int],
    matrix: list[list[str]],
    index=1,
):
    if index >= len(word):
        print("Found word! +1")
        print(f"Direction: {direction}")
        return True

    current_letter = word[index]
    print(f"Current letter: {current_letter}")
    x, y = add_coords(position, direction)

    if not within_range((x, y), matrix) or current_letter != matrix[y][x]:
        return False
    
    return check_letters_recurs(word, (x, y), direction, matrix, index + 1)


def check_letters_iter(
    word: str,
    position: tuple[int, int],
    direction: tuple[int, int],
    matrix: list[list[str]],
):
    x, y = position
    for char in word[1:]:
        x, y = add_coords((x, y), direction)
        if not within_range((x, y), matrix) or char != matrix[y][x]:
            return False
    
    return True


def part1(raw_input: str):
    input = parse_input(raw_input)

    WORD = "XMAS"

    first_char_coord_list = find_letter(WORD[0], input)
    print(f"X's: {len(first_char_coord_list)}")
    word_count = 0
    m_count = 0
    for char_position in first_char_coord_list:
        potential_directions = find_direction(char_position, WORD[1], input)
        m_count += len(potential_directions)
        for direction in potential_directions:
            if check_letters_recurs(WORD, char_position, direction, input):
                word_count += 1
    print(f"M's: {m_count}")
    return word_count


def part2(raw_input: str):
    input = parse_input(raw_input)

    return


parameters = {
    "part1": {
        "tests": [
            # {
            #     "input": '''''',
            #     "expected": ""
            # }
        ],
        "solution": part1,
    },
    "part2": {
        "tests": [
            # {
            #     "input": '''''',
            #     "expected": ""
            # }
        ],
        "solution": part2,
    },
    "trim_test_inputs": True,
    "only_tests": True,
}


def run(parameters):
    example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
    # input_file = read_input("./days/day00_input.txt")

    data = example
    # data = input_file

    solution1 = part1(data)
    print(f"Solution 1: {solution1}")

    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
