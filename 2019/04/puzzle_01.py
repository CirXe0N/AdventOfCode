def has_increasing_digits(num: int) -> bool:
    num_string = str(num)
    is_valid = []

    for index, char in enumerate(num_string):
        if index == 0:
            continue

        prev_digit = int(num_string[index - 1])
        is_increasing = int(char) >= prev_digit
        is_valid.append(is_increasing)

    return all(is_valid)


def has_same_adjacent_digits(num: int) -> bool:
    num_string = str(num)
    is_valid = []

    for index, char in enumerate(num_string):
        if index == 0:
            continue

        is_same = char == num_string[index - 1]
        is_valid.append(is_same)

    return any(is_valid)


approved_passwords = []
for num in range(108457, 562041):
    is_valid = [
        has_increasing_digits(num),
        has_same_adjacent_digits(num),
    ]

    if all(is_valid):
        approved_passwords.append(num)


answer = len(approved_passwords)
print(f'The answer is {answer}')
