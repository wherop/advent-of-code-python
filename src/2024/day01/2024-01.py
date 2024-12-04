from read_input import parse_input
from read_input import read_input
from aocd import data
    

example_data = parse_input(read_input("./example.txt"))

input = parse_input(data)


def part1(input):
    left_list, right_list, dist_list = [[],[], []]
    for line in input:
        IDs = line.split()
        left_list.append(int(IDs[0]))
        right_list.append(int(IDs[1]))
    left_list.sort() 
    right_list.sort()
    for left, right in zip (left_list, right_list):
        dist_list.append(abs(left - right))
    return sum(dist_list)

def part2(input):
    left_list, right_list, similarity_list = [[],[], []]
    for line in input:
        IDs = line.split()
        left_list.append(int(IDs[0]))
        right_list.append(int(IDs[1]))
    for left in left_list:
        freq = right_list.count(left)
        similarity_list.append(left * freq)
    return sum(similarity_list)

def main(input):
    answer1 = part1(input)
    print(f"Part 1: {answer1}")
    answer2 = part2(input)
    print(f"Part 2: {answer2}")

main(example_data)
