import math


def calculate_trees_encountered(lines):
    amount_trees = 0
    initial_length = len(lines[0])

    for y, line in enumerate(lines):
        x = y * 3

        if x >= initial_length:
            x -= initial_length * math.floor(x / initial_length)

        if '#' in line[x]:
            amount_trees += 1

    return amount_trees


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    answer = calculate_trees_encountered(lines)
    print(f'The answer is {answer}')
