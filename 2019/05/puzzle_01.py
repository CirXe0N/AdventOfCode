
def load_input() -> list:
    data = []
    with open('input.txt') as f:
        for line in f.readlines():
            data += line.split(',')

    return list(map(int, data))


def get_params_amount(op_code: str) -> int:
    if op_code in ['01', '02']:
        return 3

    if op_code in ['03', '04']:
        return 1

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

        cursor += params_amount + 1

    return output_values


int_codes_list = load_input()
output = run_program(int_codes_list, 1)
print(f'The output is {output}')
print(f'The answer is {output[-1]}')
