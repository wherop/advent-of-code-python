# Advent of Code 2024, day 2
from utils.input import read_input
from aocd import data


def parse_input(raw: str):
    result = raw.splitlines()
    # Optional: Remove any empty lines if needed
    return [list(map(int, line.split())) for line in result if line.strip()]


def dampen_problem(report: list[int]):
    return


def is_safe(report: list[int]):
    diff0 = report[0] - report[1]
    if diff0 == 0:
        return False
    # increasing
    if diff0 < 0:
        for a, b in zip(report, report[1:]):
            if not -3 <= a - b <= -1:
                return False
        return True
    else:
        for a, b in zip(report, report[1:]):
            if not 1 <= a - b <= 3:
                return False
        return True


def check_report(report: list[int]):
    if not is_safe(report):
        print("=== Dampening Problem ===")
        for i, level in enumerate(report):
            problem = report.pop(i)
            if is_safe(report):
                print("Safe!")
                print(f"{report} problem '{problem}' at i={i}")
                return True
        print("Unsafe :(")
        return False
    else:
        print("Safe!")
        print(report)
        return True


def part1(raw_input: str):
    input = parse_input(raw_input)

    return sum(is_safe(report) for report in input)


def part2(raw_input: str):
    input = parse_input(raw_input)

    return sum(check_report(report) for report in input)


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
    example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    input_file = read_input("./days/day02_input.txt")

    # data = example
    # data = input_file

    solution1 = part1(data)
    print(f"Solution 1: {solution1}")

    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
    # 431 too high
