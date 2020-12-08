def run_instructions(instructions):
    accumulator = 0
    position = 0
    visited = []

    while True:
        try:
            instruction = instructions[position]
            operation, argument = instruction.split(' ')

            if operation == 'acc':
                accumulator += int(argument)

            elif operation == 'jmp':
                position += int(argument) - 1

            if position in visited:
                accumulator = None
                break

            visited.append(position)
            position += 1

        except IndexError:
            break

    return accumulator


def switch(instructions):
    index = 0
    while index < len(instructions):
        items = instructions.copy()

        instruction = items[index]

        if 'jmp' in instruction:
            items[index] = instruction.replace('jmp', 'nop')

        accumulator = run_instructions(items)

        if accumulator:
            return accumulator

        index += 1


with open('input.txt') as f:
    instructions = list(f.read().splitlines())
    answer = switch(instructions)
    print(f'The answer is {answer}')
