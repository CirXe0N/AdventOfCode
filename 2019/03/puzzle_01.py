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


def move(commands: list) -> list:
    positions = []
    x, y = 0, 0

    for command in commands:
        direction = command['direction']
        steps = command['steps']

        for n in range(1, steps + 1):
            if direction == 'R':
                x += 1

            if direction == 'L':
                x -= 1

            if direction == 'U':
                y += 1

            if direction == 'D':
                y -= 1

            positions.append((x, y))

    return positions


wire_paths = load_input()

p1 = move(wire_paths[0])
p2 = move(wire_paths[1])

intersections = set(p1).intersection(set(p2))

answer = min([abs(pos[0]) + abs(pos[1]) for pos in intersections])
print(f'The answer is {answer}')
