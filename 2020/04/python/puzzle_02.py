import re


def validate_birth_year(passport):
    value = passport.get('byr', False)
    return value and 1920 <= int(value) <= 2002


def validate_issue_year(passport):
    value = passport.get('iyr', False)
    return value and 2010 <= int(value) <= 2020


def validate_expiration_year(passport):
    value = passport.get('eyr', False)
    return value and 2020 <= int(value) <= 2030


def validate_height(passport):
    value = passport.get('hgt', '')
    if 'cm' in value:
        value = value.replace('cm', '')
        return value and 150 <= int(value) <= 193

    elif 'in' in value:
        value = value.replace('in', '')
        return value and 59 <= int(value) <= 76

    return False


def validate_hair_color(passport):
    value = passport.get('hcl', '')
    return re.match(r'^#(.){6}$', value)


def validate_eye_color(passport):
    value = passport.get('ecl', '')
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_passport_id(passport):
    value = passport.get('pid', '')
    return len(value) == 9


def count_valid_passports(passports):
    valid_count = 0
    for passport in passports:
        is_valid = all([
            validate_birth_year(passport),
            validate_issue_year(passport),
            validate_expiration_year(passport),
            validate_height(passport),
            validate_hair_color(passport),
            validate_eye_color(passport),
            validate_passport_id(passport)
        ])

        if is_valid:
            valid_count += 1

    return valid_count


def build_passports(passports):
    formatted_passports = []

    for passport in passports:
        formatted_passport = {}
        passport = passport.replace('\n', ' ')
        fields = passport.split(' ')

        for field in fields:
            key, value = field.split(':')
            formatted_passport[key] = value

        formatted_passports.append(formatted_passport)

    return formatted_passports


with open('input.txt') as f:
    passports = f.read().split(sep='\n\n')
    passports = build_passports(passports)
    answer = count_valid_passports(passports)
    print(f'The answer is {answer}')
