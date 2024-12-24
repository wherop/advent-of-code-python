# Advent of Code 2024, day 5
from utils.input import read_input
from aocd import data


def parse_section(separator: str, section: str):
    return [
        tuple([int(page) for page in line.split(separator)])
        for line in section.splitlines()
    ]


def parse_input(raw_input: str):
    rules_str, updates_str = raw_input.strip().split("\n\n", 1)
    rules = parse_section("|", rules_str)
    updates = parse_section(",", updates_str)
    return tuple([rules, updates])


def collapse_rules(rules: list[tuple[int, ...]]) -> dict[int, list[int]]:
    collapsed_rules = {}
    for rule in rules:
        collapsed_rules.setdefault(rule[0], [])
        collapsed_rules[rule[0]].append(rule[1])
    return collapsed_rules


def is_1_before_2(n1: int, n2: int, update: list):
    i = update.index(n1)
    j = update.index(n2)
    return i < j


def is_correct(update_tuple: tuple[int, ...], rules: dict[int, list[int]]):
    update = list(update_tuple)
    for page1 in update:
        if page1 in rules:
            for page2 in update:
                if page2 in rules[page1]:
                    if not is_1_before_2(page1, page2, update):
                        return False
    return True


def is_incorrect(update_tuple: tuple[int, ...], rules: dict[int, list[int]]):
    update = list(update_tuple)

    for page1, dependent_pages in rules.items():
        if page1 not in update:
            continue
        incorrect_pages = [
            page2
            for page2 in dependent_pages
            if page2 in update and not is_1_before_2(page1, page2, update)
        ]
        if incorrect_pages:
            return True
    return False


def get_middle(update: tuple[int, ...]):
    middle = float(len(update)) / 2
    if middle % 2 != 0:
        return update[int(middle - 0.5)]
    else:
        return update[int(middle - 1)], update[int(middle)]


def get_corrected_middles(incorrect_updates, rules):
    middle_pages = []
    for update_tuple in incorrect_updates:
        update = list(update_tuple)
        change_count = 0
        while is_incorrect(tuple(update), rules) and change_count < 100:
            for page1, dependent_pages in rules.items():
                if page1 not in update:
                    continue
                for page2 in dependent_pages:
                    if page2 not in update:
                        continue
                    i = update.index(page1)
                    j = update.index(page2)
                    if i > j:
                        update.insert(i, update.pop(j))
            change_count += 1

        if 100 <= change_count:
            print(f"Error: Could not resolve in {change_count} changes.")
            return

        middle_page = get_middle(tuple(update))
        if isinstance(middle_page, int):
            middle_pages.append(middle_page)
        else:
            print("Error: Update has even number of pages!")

    return middle_pages


def part1(raw_input: str):
    rules, updates = parse_input(raw_input)
    collapsed_rules = collapse_rules(rules)

    middle_pages = []
    for update in updates:
        if not is_incorrect(update, collapsed_rules):
            middle_page = get_middle(update)
            if isinstance(middle_page, int):
                middle_pages.append(middle_page)
            else:
                print("Error: Update has even number of pages!")
    return sum(middle_pages)


def part2(raw_input: str):
    rules_long, updates = parse_input(raw_input)
    rules = collapse_rules(rules_long)

    incorrect_updates = [update for update in updates if is_incorrect(update, rules)]

    middle_pages = get_corrected_middles(incorrect_updates, rules)

    if not middle_pages:
        return 0

    return sum(middle_pages)


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
    example = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    # input_file = read_input("./days/day00_input.txt")

    # data = example
    # data = input_file

    solution1 = part1(data)
    print(f"Solution 1: {solution1}")

    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
