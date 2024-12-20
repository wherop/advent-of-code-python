# Advent of Code 2024, day 3
from utils.input import read_input
from aocd import data
import re

RESULT = 'result'
regex_mul = r"mul\(\d{1,3},\d{1,3}\)"
regex_do = r"do\(\)"
regex_do_not = r"don't\(\)"

def mul(a, b):
    return a * b


def exec_mul(instruction, context=None):
    if context is None:
        context = {}
    exec(instruction, globals(), context)
    return context.get(RESULT)

def parse_input(raw_input):
    return raw_input


def part1(raw_input: str):
    input = parse_input(raw_input)

    valid_instructions = re.findall(regex_mul, input)

    results:list = list(map(lambda x: exec_mul(f"{RESULT} = {x}"), valid_instructions))
    return sum(results)


def part2(raw_input: str):
    input = parse_input(raw_input)
    controlled_sections = re.split(regex_do,input)
    print(controlled_sections)
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
    # print(parameters)
    example = (
        """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    )
    # example = '''hen()%&$~)mul(926,673)$what()!select(),do()~select()#^mul(272,306)~%'mul(22,647)$mul(904,943)^>-from()mul(635,212)when()how()[mul(314,335)%(-  + ~mul(635,915)~[[do(){where(307,78)(who()(why()where();mul(450from()mul(903,662)>$mul(924,200),why()select()$mul(418,533)where()[where()mul(266,643):~^/#(:[from()mul(81,715),who()@:~+who()'%mul(79?who()select();# mul(436,105)#*why() #~[,where()'mulwho()[(~)[mul(119,92)]where(),'''

    # input_file = read_input("./days/day03_input.txt")

    data = example
    # data = input_file

    solution1 = part1(data)
    print(f"Solution 1: {solution1}")

    solution2 = part2(data)
    print(f"Solution 2: {solution2}")
    # 431 too high
