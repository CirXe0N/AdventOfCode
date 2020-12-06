import math


def calculate_trees_encountered(lines, right, down):
    amount_trees = 0
    initial_length = len(lines[0])

    for y, line in enumerate(lines):
        if y % down != 0:
            continue

        x = int((y * right) / down)

        if x >= initial_length:
            x -= initial_length * math.floor(x / initial_length)

        if '#' in line[x]:
            amount_trees += 1

    return amount_trees


with open('input.txt') as f:
    lines = list(f.read().splitlines())

    strategies = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    answers = []
    for strategy in strategies:
        right, down = strategy
        amount_trees = calculate_trees_encountered(lines, right, down)
        answers.append(amount_trees)

    answer = math.prod(answers)
    print(f'The answer is {answer}')

