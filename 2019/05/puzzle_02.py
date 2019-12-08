
def load_input() -> list:
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            data += line.split(',')

    return list(map(int, data))


def get_params_amount(op_code: str) -> int:
    if op_code in ['03', '04']:
        return 1

    if op_code in ['05', '06']:
        return 2

    if op_code in ['01', '02', '07', '08']:
        return 3

    return 0


def run_program(instructions: list, input_val: int) -> list:
    output_values = []
    cursor = 0

    while True:
        instruction = instructions[cursor]
        instruction = str(instruction).zfill(5)

        op_code = instruction[3:]
        mode_1 = instruction[2]
        mode_2 = instruction[1]

        params_amount = get_params_amount(op_code)

        if params_amount > 0:
            param_1 = instructions[cursor + 1]
            value_1 = param_1 if mode_1 == '1' else instructions[param_1]

        if params_amount > 1:
            param_2 = instructions[cursor + 2]
            value_2 = param_2 if mode_2 == '1' else instructions[param_2]

        if params_amount > 2:
            param_3 = instructions[cursor + 3]

        if op_code == '99':
            break

        if op_code == '01':
            instructions[param_3] = value_1 + value_2

        if op_code == '02':
            instructions[param_3] = value_1 * value_2

        if op_code == '03':
            instructions[param_1] = input_val

        if op_code == '04':
            output_values.append(value_1)

        if op_code == '05' and value_1 != 0:
            cursor = value_2
            continue

        if op_code == '06' and value_1 == 0:
            cursor = value_2
            continue

        if op_code == '07':
            instructions[param_3] = 1 if value_1 < value_2 else 0

        if op_code == '08':
            instructions[param_3] = 1 if value_1 == value_2 else 0

        cursor += params_amount + 1

    return output_values


instructions = load_input()
output = run_program(instructions, 5)
print(f'The answer is {output[-1]}')
