def load_input() -> list:
    wire_paths = []
    with open('input.txt') as f:
        for line in f.readlines():
            wire_path = []

            for wire in line.split(','):
                wire_path.append({
                    'direction': wire[0],
                    'steps': int(wire[1:])
                })

            wire_paths.append(wire_path)

    return wire_paths


def move(commands: list, end_position: tuple = None) -> list:
    positions = []
    x, y = 0, 0

    for command in commands:
        direction = command['direction']
        steps = command['steps']

        for n in range(1, steps + 1):
            if end_position and (x, y) == end_position:
                return positions

            if direction == 'R':
                y += 1

            if direction == 'L':
                y -= 1

            if direction == 'U':
                x += 1

            if direction == 'D':
                x -= 1

            positions.append((x, y))

    return positions


wire_paths = load_input()

p1 = move(wire_paths[0])
p2 = move(wire_paths[1])

intersections = set(p1).intersection(set(p2))

steps = []
for intersection in intersections:
    steps1 = len(move(wire_paths[0], intersection))
    steps2 = len(move(wire_paths[1], intersection))
    total_steps = steps1 + steps2
    steps.append(total_steps)

answer = min(steps)
print(f'The answer is {answer}')
