def calculate_valid_passwords(lines):
    amount_valid = 0

    for line in lines:
        policy, password = line.split(': ')
        letter = policy[-1]
        min_occurrence, max_occurrence = policy[:-2].split('-')
        min_occurrence = int(min_occurrence)
        max_occurrence = int(max_occurrence)

        counter = password.count(letter)
        if min_occurrence <= counter <= max_occurrence:
            amount_valid += 1

    return amount_valid


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    answer = calculate_valid_passwords(lines)
    print(f'The answer is {answer}')


