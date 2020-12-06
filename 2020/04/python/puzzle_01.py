def count_valid_passports(passports):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid_count = 0
    for passport in passports:
        is_valid = all(x in passport for x in required)

        if is_valid:
            valid_count += 1

    return valid_count


with open('input.txt') as f:
    passports = f.read().split(sep='\n\n')
    answer = count_valid_passports(passports)
    print(f'The answer is {answer}')
