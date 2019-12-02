def load_input() -> list:
    codes = []
    with open('input.txt') as f:
        for line in f.readlines():
            codes += line.split(',')

    return list(map(int, codes))


def run_program(int_codes: list) -> list:
    index = 0
    int_codes[1] = 12
    int_codes[2] = 2

    while True:
        int_code = int_codes[index]

        if int_code == 99:
            break

        value_1_index = int_codes[index + 1]
        value_2_index = int_codes[index + 2]
        output_index = int_codes[index + 3]
        value_1 = int_codes[value_1_index]
        value_2 = int_codes[value_2_index]

        if int_code == 1:
            int_codes[output_index] = value_1 + value_2

        if int_code == 2:
            int_codes[output_index] = value_1 * value_2

        index += 4

    return int_codes


int_codes_list = load_input()
output = run_program(int_codes_list)
print(f'The answer is {output[0]}')
