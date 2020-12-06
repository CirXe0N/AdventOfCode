def calculate_valid_passwords(lines):
    amount_valid = 0

    for line in lines:
        policy, password = line.split(': ')
        letter = policy[-1]
        pos_1, pos_2 = policy[:-2].split('-')
        is_pos_1_valid = letter == password[int(pos_1) - 1]
        is_pos_2_valid = letter == password[int(pos_2) - 1]
        is_both_valid = is_pos_1_valid and is_pos_2_valid

        if not is_both_valid and (is_pos_1_valid or is_pos_2_valid):
            amount_valid += 1

    return amount_valid


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    answer = calculate_valid_passwords(lines)
    print(f'The answer is {answer}')

