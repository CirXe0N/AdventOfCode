def run_instructions(instructions):
    accumulator = 0
    position = 0
    visited = []

    while True:
        instruction = instructions[position]
        operation, argument = instruction.split(' ')

        if operation == 'acc':
            accumulator += int(argument)

        elif operation == 'jmp':
            position += int(argument) - 1

        if position in visited:
            break

        visited.append(position)
        position += 1

    return accumulator


with open('input.txt') as f:
    instructions = list(f.read().splitlines())
    answer = run_instructions(instructions)
    print(f'The answer is {answer}')
