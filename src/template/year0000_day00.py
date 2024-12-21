# Advent of Code {year}, day {day}
from utils.input import read_input
from aocd import data

def parse_input(raw_input):
    return raw_input

def part1(raw_input: str):
    input = parse_input(raw_input)

    return

def part2(raw_input: str):
    input = parse_input(raw_input)

    return

parameters = {{
    "part1": {{
        "tests": [
            # {{
            #     "input": '''''',
            #     "expected": ""
            # }}
        ],
        "solution": part1,
    }},
    "part2": {{
        "tests": [
            # {{
            #     "input": '''''',
            #     "expected": ""
            # }}
        ],
        "solution": part2,
    }},
    "trim_test_inputs": True,
    "only_tests": True,
}}


def run(parameters):
    example = ""
    # input_file = read_input("./days/day00_input.txt")

    data = example
    # data = input_file

    solution1 = part1(data)
    print(f"Solution 1: {{solution1}}")

    solution2 = part2(data)
    print(f"Solution 2: {{solution2}}")