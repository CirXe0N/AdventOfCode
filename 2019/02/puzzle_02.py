import itertools


def load_input() -> list:
    codes = []
    with open('input.txt') as f:
        for line in f.readlines():
            codes += line.split(',')

    return list(map(int, codes))


def run_program(noun: int, verb: int, int_codes: list) -> list:
    index = 0
    int_codes[1] = noun
    int_codes[2] = verb

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
result = 19690720
combos = itertools.combinations(range(0, 99), 2)

for noun, verb in combos:
    int_codes = int_codes_list.copy()
    output = run_program(noun, verb, int_codes)

    if output[0] == result:
        answer = 100 * noun + verb
        print(f'The answer is {answer}')
